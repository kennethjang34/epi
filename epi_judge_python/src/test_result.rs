use num_derive::FromPrimitive;
use num_traits::FromPrimitive;

#[derive(Debug, Copy, Clone, PartialEq, FromPrimitive)]
#[repr(i32)]
pub enum TestResult {
    PASSED = 0,
    FAILED = 1,
    TIMEOUT = 2,
    UNKNOWN_EXCEPTION = 3,
    STACK_OVERFLOW = 4,
    RUNTIME_ERROR = 5,
}
