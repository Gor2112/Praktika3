def is_palindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return is_palindrome(s, left + 1, right - 1)

s = input("Введите строку: ")
if is_palindrome(s, 0, len(s)-1):
    print("Палиндром")
else:
    print("Не палиндром")

# Пример ввода:
# abba
# Вывод:
# Палиндром
