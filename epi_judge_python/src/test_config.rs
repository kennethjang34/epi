use serde_json::Value;
use std::env;
use std::path::PathBuf;

use crate::tri_bool::TriBool;

#[derive(Debug, Clone)]
pub struct TestConfig {
    pub test_data_dir: String,
    pub test_file: String,
    pub test_data_file: String,
    pub tty_mode: TriBool,
    pub color_mode: TriBool,
    pub update_js: bool,
    pub timeout_seconds: f64,
    pub num_failed_tests_before_stop: usize,
    pub analyze_complexity: bool,
    pub complexity_timeout: usize,
    pub metric_names_override: Box<dyn Fn(Vec<String>) -> Vec<String>>,
    pub metrics_override: Box<dyn Fn(Vec<usize>, &dyn Fn() -> Vec<Value>) -> Vec<usize>>,
}

impl TestConfig {
    pub fn new(
        test_file: String,
        test_data_file: String,
        timeout_seconds: f64,
        num_failed_tests_before_stop: usize,
    ) -> Self {
        TestConfig {
            test_data_dir: String::new(),
            test_file,
            test_data_file,
            tty_mode: TriBool::INDETERMINATE,
            color_mode: TriBool::INDETERMINATE,
            update_js: true,
            timeout_seconds,
            num_failed_tests_before_stop,
            analyze_complexity: false,
            complexity_timeout: 20,
            metric_names_override: Box::new(|names| names),
            metrics_override: Box::new(|metrics, _func_args| metrics),
        }
    }

    pub fn from_command_line(
        test_file: String,
        test_data_file: String,
        timeout_seconds: f64,
        num_failed_tests_before_stop: usize,
        commandline_args: Vec<String>,
    ) -> Result<Self, String> {
        // Set num_failed_tests_before_stop to 0, means users want to run as many tests in one run.
        let num_failed_tests_before_stop = if num_failed_tests_before_stop == 0 {
            usize::max_value()
        } else {
            num_failed_tests_before_stop
        };

        let mut config = TestConfig::new(
            test_file.clone(),
            test_data_file.clone(),
            timeout_seconds,
            num_failed_tests_before_stop,
        );

        let mut args = env::args();
        args.next(); // skip the first argument (program name)

        while let Some(arg) = args.next() {
            match arg.as_str() {
                "--test-data-dir" => {
                    if let Some(dir) = args.next() {
                        config.test_data_dir = dir;
                    } else {
                        return Err("--test-data-dir requires a directory path".to_string());
                    }
                }
                "--force-tty" => config.tty_mode = TriBool::TRUE,
                "--no-tty" => config.tty_mode = TriBool::FALSE,
                "--force-color" => config.color_mode = TriBool::TRUE,
                "--no-color" => config.color_mode = TriBool::FALSE,
                "--no-update-js" => config.update_js = false,
                "--no-complexity" => config.analyze_complexity = false,
                _ => {
                    return Err(format!("Unknown argument: {}", arg));
                }
            }
        }

        if !config.test_data_dir.is_empty() {
            if !PathBuf::from(&config.test_data_dir).is_dir() {
                return Err(format!(
                    "CL: --test-data-dir argument ({}) is not a directory",
                    config.test_data_dir
                ));
            }
        } else {
            config.test_data_dir = get_default_test_data_dir_path();
        }

        Ok(config)
    }
}
