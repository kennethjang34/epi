#[derive(Debug, Copy, Clone, PartialEq)]
pub enum TriBool {
    FALSE,
    TRUE,
    INDETERMINATE,
}

impl TriBool {
    pub fn get_or_default(&self, default_value: bool) -> bool {
        match self {
            TriBool::FALSE => false,
            TriBool::TRUE => true,
            TriBool::INDETERMINATE => default_value,
        }
    }
}
