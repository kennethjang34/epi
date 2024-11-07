use crate::test_failure::PropertyName;
use core::panicking::{panic_fmt, panic_str};
use regex::Regex;
use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io::{self, BufRead};
use std::path::{Path, PathBuf};

use crate::test_failure::TestFailure;

#[derive(Debug, Clone, PartialEq)]
enum TriBool {
    FALSE,
    TRUE,
    INDETERMINATE,
}

impl TriBool {
    fn get_or_default(&self, default_value: bool) -> bool {
        match self {
            TriBool::FALSE => false,
            TriBool::TRUE => true,
            TriBool::INDETERMINATE => default_value,
        }
    }
}

// Define the Value type
type Value = i32; // You may need to adjust this type based on the actual type used in your code

fn split_tsv_file(tsv_file: &str) -> Result<Vec<Vec<&str>>, io::Error> {
    let row_delim = '\n';
    let field_delim = '\t';

    let file = File::open(tsv_file)?;
    let lines = io::BufReader::new(file).lines();

    Ok(lines
        .map(|line| {
            line.unwrap_or_default()
                .replace(row_delim, "")
                .split(field_delim)
                .collect::<Vec<_>>()
        })
        .collect())
}

fn get_default_test_data_dir_path() -> String {
    const MAX_SEARCH_DEPTH: usize = 4;

    let mut path = PathBuf::from("test_data");

    for _ in 0..MAX_SEARCH_DEPTH {
        if path.is_dir() {
            return path.to_string_lossy().into_owned();
        }
        path = path.join("..");
    }

    panic!("Can't find test data directory. Please start the program with \"--test_data_dir <path>\" command-line option");
}

fn get_file_path_in_judge_dir(file_name: &str) -> PathBuf {
    let dir_path = get_default_test_data_dir_path();
    Path::new(&dir_path).join("..").join(file_name)
}

fn filter_bracket_comments(s: &str) -> String {
    let re = Regex::new(r"(\[[^\]]*\])").unwrap();
    let result = re.replace_all(s, "");
    result.replace(" ", "").to_string()
}

fn assert_all_values_present(reference: &[&str], result: &[&str]) {
    let mut reference_set: HashMap<&str, i32> = HashMap::new();

    for x in reference {
        *reference_set.entry(x).or_insert(0) += 1;
    }

    for x in result {
        if let Some(count) = reference_set.get_mut(x) {
            *count -= 1;
        }
    }

    let excess_items: Vec<_> = reference_set
        .iter()
        .filter(|(_, &count)| count < 0)
        .flat_map(|(x, &count)| vec![x; -count as usize])
        .cloned()
        .collect();

    let missing_items: Vec<_> = reference_set
        .iter()
        .filter(|(_, &count)| count > 0)
        .flat_map(|(x, &count)| vec![x; count as usize])
        .cloned()
        .collect();

    if !excess_items.is_empty() || !missing_items.is_empty() {
        let mut test_failure = TestFailure::new("Value set changed");
        if !excess_items.is_empty() {
            test_failure =
                test_failure.with_property(PropertyName::ExcessItems, &excess_items.join(", "));
        }
        if !missing_items.is_empty() {
            test_failure =
                test_failure.with_property(PropertyName::MissingItems, &missing_items.join(", "));
        }
        panic!("{:?}", test_failure);
    }
}

fn completely_sorted<T: Ord + Clone>(x: Option<T>) -> T {
    if let Some(list) = x
        .as_ref()
        .cloned()
        .and_then(|x| downcast_ref::<Vec<T>>(x).cloned())
    {
        return list.into_iter().map(completely_sorted).collect();
    } else {
        return x;
    }
}

fn unordered_compare<T: PartialEq>(a: T, b: T) -> bool {
    completely_sorted(a) == completely_sorted(b)
}

fn has_executor_hook<T: Fn()>(func: T) -> bool {
    func.executor_hook
}

fn enable_executor_hook<T: Fn()>(func: T) -> T {
    func.executor_hook = true;
    func
}

fn flatten_list<T: Clone>(l: Vec<Vec<T>>) -> Vec<T> {
    l.into_iter().flatten().collect()
}
