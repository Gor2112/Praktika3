import java.util.Scanner;

public class Main {
    public static boolean isPalindrome(String s, int left, int right) {
        if (left >= right) return true;
        if (s.charAt(left) != s.charAt(right)) return false;
        return isPalindrome(s, left + 1, right - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Введите строку: ");
        String input = sc.nextLine();
        
        if (isPalindrome(input, 0, input.length() - 1))
            System.out.println("Палиндром");
        else 
            System.out.println("Не палиндром");
    }
}

// Пример ввода:

// level

// Вывод:

// Палиндром
