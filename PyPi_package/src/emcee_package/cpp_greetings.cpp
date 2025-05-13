#include <iostream>
using namespace std;

extern "C" {
    int cpp_hey() {
        std::cout << "Heya! From Emcee in C++" << std::endl;
        return 0;
    }
}

extern "C" {
    int cpp_laters() {
        std::cout << "See ya later! From Emcee in C++" << std::endl;
        return 0;
    }
}