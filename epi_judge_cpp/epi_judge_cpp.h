#include <string>
#include <vector>
using std::string;
using std::vector;
// vector<vector<string>> anagrams(const std::vector<string> &dictionary);

#ifndef _TESTLIB_H
#define _TESTLIB_H

#include <vector>
#ifdef __cplusplus
extern "C" {
#endif

int add(int first, int second);
char *anagrams(const std::vector<string>);

#ifdef __cplusplus
}
#endif
#endif
