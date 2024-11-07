use bindgen::CargoCallbacks;
use std::env;
use std::path::PathBuf;

fn main() {
    println!("cargo:rerun-if-changed=wrapper.hpp");
    println!("cargo:rustc-link-lib=memory");

    // pkg_config::Config::new().probe("memory").unwrap();
    // Tell cargo to look for shared libraries in the specified directory
    // println!("cargo:rustc-link-search=/opt/homebrew/op/llvm/lib");
    // println!("cargo:rustc-link-search=native=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX.sdk/usr/include/c++/v1/memory.h");
    //     export LDFLAGS="-L/opt/homebrew/opt/llvm/lib"
    // export CPPFLAGS="-I/opt/homebrew/opt/llvm/include"

    // Tell cargo to tell rustc to link the system bzip2
    // shared library.
    // println!("cargo:rustc-link-lib=bz2");
    // println!("cargo:rustc-link-lib=memory");
    // This is the path to the intermediate object file for our library.
    let libdir_path = PathBuf::from("./")
        .canonicalize()
        .expect("cannot canonicalize path");
    let headers_path = libdir_path.join("wrapper.hpp");
    let headers_path_str = headers_path.to_str().expect("Path is not a valid string");
    let obj_path = libdir_path.join("wrapper.o");
    // This is the path to the static library file.
    let lib_path = libdir_path.join("libwrapper.a");

    // if !std::process::Command::new("ar")
    //     .arg("rcs")
    //     .arg(lib_path)
    //     .arg(obj_path)
    //     .output()
    //     .expect("could not spawn `ar`")
    //     .status
    //     .success()
    // {
    //     // Panic if the command was not successful.
    //     panic!("could not emit library file");
    // }
    //
    let bindings = bindgen::Builder::default()
        // The input header we would like to generate
        // bindings for.
        .header(headers_path_str)
        .enable_cxx_namespaces()
        .allowlist_recursively(true)
        .clang_args(&["-x", "c++", "--std=c++14", "-fkeep-inline-functions"])
        .opaque_type("std::.*")
        .generate_inline_functions(true)
        .derive_copy(true)
        // .no_copy("[u8*")
        // Tell cargo to invalidate the built crate whenever any of the
        // included header files changed.
        .parse_callbacks(Box::new(CargoCallbacks))
        // Finish the builder and generate the bindings.
        .generate()
        // Unwrap the Result and panic on failure.
        .expect("Unable to generate bindings");

    // Write the bindings to the $OUT_DIR/bindings.rs file.
    let out_path = PathBuf::from(env::var("OUT_DIR").unwrap()).join("bindings.rs");
    bindings
        .write_to_file(out_path)
        .expect("Couldn't write bindings!");
}
