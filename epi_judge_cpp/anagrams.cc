// namespace std {
// typedef decltype(nullptr) nullptr_t;
// }
#include <iostream>
#include <string>
#include <vector>

// #include "epi_judge_cpp.h"
#include "test_framework/generic_test.h"
using std::string;
using std::vector;

vector<vector<string>> FindAnagrams(const vector<string> &dictionary) {
  // std::cout << add(10, 20) << std::endl;
  // string x = anagrams(dictionary);
  // std::cout << x << std::endl;
  return vector<vector<string>>();
}

int main(int argc, char *argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"dictionary"};
  return GenericTestMain(args, "anagrams.cc", "anagrams.tsv", &FindAnagrams,
                         UnorderedComparator{}, param_names);
}
