use std::collections::HashMap;

use crate::timeout_exception::TestTimer;

pub struct TestOutput {
    timer: Option<TestTimer>,
    metrics: Option<HashMap<String, f64>>,
}

impl TestOutput {
    fn new(timer: Option<TestTimer>, metrics: Option<HashMap<String, f64>>) -> Self {
        TestOutput { timer, metrics }
    }
}
