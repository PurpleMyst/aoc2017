#include <algorithm>
#include <array>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <vector>

constexpr size_t DATA_SIZE = 256;

int main() {
    size_t skip_size = 0;
    size_t current = 0;

    std::array<uint8_t, DATA_SIZE> data;
    std::iota(data.begin(), data.end(), 0);

    std::vector<char> lengths;
    char inp_length;

    while (std::cin >> inp_length) {
        if (inp_length == '\n') continue;
        lengths.push_back(inp_length);
    }

    for (char extra_length : {17, 31, 73, 47, 23}) {
        lengths.push_back(extra_length);
    }

    for (size_t i = 0; i < 64; ++i) {
        for (char length : lengths) {
            std::vector<uint8_t> sublist;

            for (size_t j = current; j < current + length; ++j) {
                sublist.push_back(data.at(j % DATA_SIZE));
            }

            std::reverse(sublist.begin(), sublist.end());

            auto it = sublist.begin();
            for (size_t j = current; j < current + length; ++j) {
                data.at(j % DATA_SIZE) = *(it++);
            }

            current += length + (skip_size++);
        }
    }

    std::cout << std::hex
              << std::setfill('0');

    for (size_t i = 0; i < DATA_SIZE; i += 16) {
        uint8_t accumulator = 0;

        for (size_t j = i; j < i + 16; ++j) {
            accumulator ^= data.at(j);
        }

        std::cout << std::setw(2) << (int)accumulator;
    }

    std::cout << std::endl;
}
