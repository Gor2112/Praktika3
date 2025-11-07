#include <iostream>
#include <string>
using namespace std;

bool isPalindrome(const string &s, int left, int right) {
    if (left >= right) return true;
    if (s[left] != s[right]) return false;
    return isPalindrome(s, left + 1, right - 1);
}

int main() {
    string s;
    cout << "Введите строку: ";
    getline(cin, s);

    if (isPalindrome(s, 0, s.size() - 1))
        cout << "Палиндром";
    else
        cout << "Не палиндром";
}

// Пример ввода:

// madam

// Вывод:

// Палиндром
