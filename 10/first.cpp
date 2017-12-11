#include <array>
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

constexpr size_t DATA_SIZE = 256;

int main() {
    size_t skip_size = 0;
    size_t current = 0;

    std::array<uint8_t, DATA_SIZE> data;
    std::iota(data.begin(), data.end(), 0);

    int length;
    while (std::cin >> length) {
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

    std::cout << data[0] * data[1] << std::endl;
}
