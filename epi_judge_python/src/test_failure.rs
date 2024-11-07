use std::fmt::Display;

use strum::AsStaticRef;
use strum_macros::{self, AsStaticStr};
#[derive(Debug, Clone, Copy, PartialEq, Eq, PartialOrd, Ord, AsStaticStr)]
pub enum PropertyName {
    ExceptionMessage, // message of unhandled exception
    Explanation,      // explanation from TSV file
    Command,          // last command, that caused the error, in API-testing programs
    State,            // state of the user-defined collection (for instance, in API testing)
    Expected,         // expected result
    Result,           // user-produced result
    MissingItems,     // list of items from input that are missing in the result set
    ExcessItems,      // list of items from result that are missing in the input set
    MismatchIndex, // for collections: index of the wrong item in result for binary trees: instance of TreePath describing the position of the wrong item
    ExpectedItem,  // value of the expected item in collection (not the whole collection)
    ResultItem,    // value of the result item in collection (not the whole collection)
}
impl Display for PropertyName {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_str(self.as_static())
    }
}

#[derive(Debug, Clone)]
pub struct Property {
    pub name: PropertyName,
    pub value: String, // Assuming the value is a string; you can adjust the type as needed
}

#[derive(Debug)]
pub struct TestFailure {
    pub properties: Vec<Property>,
    pub description: String,
}
impl Display for TestFailure {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        let max_property_name_length = self.get_max_property_name_length();
        let properties = self.get_properties();
        writeln!(f, "Description: {}", self.get_description())?;
        writeln!(f, "Max Property Name Length: {}", max_property_name_length)?;
        for prop in properties {
            writeln!(f, "Property: {:?} - Value: {}", prop.name, prop.value)?;
        }
        Ok(())
    }
}

impl TestFailure {
    pub fn new(description: &str) -> Self {
        TestFailure {
            properties: Vec::new(),
            description: description.to_string(),
        }
    }

    pub fn with_property(mut self, name: PropertyName, value: &str) -> Self {
        self.properties.push(Property {
            name,
            value: value.to_string(),
        });
        self
    }

    pub fn with_mismatch_info(
        self,
        mismatch_index: &str,
        expected_item: &str,
        result_item: &str,
    ) -> Self {
        self.with_property(PropertyName::MismatchIndex, mismatch_index)
            .with_property(PropertyName::ExpectedItem, expected_item)
            .with_property(PropertyName::ResultItem, result_item)
    }

    pub fn get_description(&self) -> &str {
        &self.description
    }

    pub fn get_max_property_name_length(&self) -> usize {
        self.properties
            .iter()
            .map(|prop| prop.name.to_string().len())
            .max()
            .unwrap_or(0)
    }

    pub fn get_properties(&self) -> Vec<Property> {
        let mut props = self.properties.clone();
        props.sort_by_key(|prop| prop.name);
        props
    }
}

// fn main() {
//     // Example usage
//     let failure = TestFailure::new("Example failure")
//         .with_property(PropertyName::Explanation, "This is an example")
//         .with_mismatch_info("index", "expected", "actual");
//
//     println!("Description: {}", failure.get_description());
//     println!(
//         "Max Property Name Length: {}",
//         failure.get_max_property_name_length()
//     );
//
//     let properties = failure.get_properties();
//     for prop in properties {
//         println!("Property: {:?} - Value: {}", prop.name, prop.value);
//     }
// }
