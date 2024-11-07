#![allow(non_upper_case_globals)]
#![allow(non_camel_case_types)]
#![allow(non_snake_case)]

include!(concat!(env!("OUT_DIR"), "/bindings.rs"));

// use std::ffi::c_char;
//
// #[no_mangle]
// pub extern "C" fn add(first: i32, second: i32) -> i32 {
//     first + second
// }
// pub extern "C" fn anagrams(first: &Vec<*const i32>) -> *const c_char {
//     return first.clone().remove(0);
// }
