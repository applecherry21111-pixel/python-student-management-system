# Student Management Program

students = []  # all students stored here


# --- helper functions ---

def calculate_total(marks):
    # add up all marks
    total = 0
    for m in marks:
        total += m
    return total


def calculate_average(marks):
    # average = total / number of subjects
    return calculate_total(marks) / len(marks)


def is_pass(average_mark):
    # pass if average is 50 or more
    return average_mark >= 50


def get_grade(average_mark):
    # grade based on average marks
    if average_mark >= 90:
        return "A+"
    elif average_mark >= 80:
        return "A"
    elif average_mark >= 70:
        return "B"
    elif average_mark >= 60:
        return "C"
    elif average_mark >= 50:
        return "D"
    else:
        return "F"


def get_age_category(age):
    # category based on age
    if age < 13:
        return "Child"
    elif 13 <= age <= 18:
        return "Teenager"
    else:
        return "Adult"


def is_prime(num):
    # check if number is prime
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_palindrome(s):
    # check if name reads same forward and backward
    cleaned = s.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def reverse_roll(roll_no):
    # reverse the roll number using while loop
    reversed_num = 0
    temp = roll_no
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp //= 10
    return reversed_num


def fibonacci(n):
    # first n fibonacci numbers
    fibs = []
    a, b = 0, 1
    for _ in range(n):
        fibs.append(a)
        a, b = b, a + b
    return fibs


def primes_in_range(start, end):
    # all primes between start and end
    result = []
    for num in range(start, end + 1):
        if is_prime(num):
            result.append(num)
    return result


# --- input section ---

def input_marks():
    # take 5 marks in one line, space separated
    while True:
        try:
            raw = input("  Enter 5 marks separated by spaces (0-100): ")
            values = list(map(int, raw.strip().split()))
            if len(values) != 5:
                print("  Please enter exactly 5 marks.")
                continue
            if all(0 <= m <= 100 for m in values):
                return values
            else:
                print("  All marks must be between 0 and 100.")
        except ValueError:
            print("  Please enter valid numbers only.")


def input_students():
    # get data for at least 3 students
    while True:
        try:
            count = int(input("How many students do you want to enter? (minimum 3): "))
            if count >= 3:
                break
            else:
                print("Please enter at least 3 students.")
        except ValueError:
            print("Enter a valid number.")

    for i in range(count):
        print(f"\n--- Student {i + 1} ---")

        name = input("Name: ").strip()
        while not name:
            print("Name cannot be empty.")
            name = input("Name: ").strip()

        while True:
            try:
                roll_no = int(input("Roll Number: "))
                if roll_no > 0:
                    break
                else:
                    print("Roll number must be positive.")
            except ValueError:
                print("Enter a valid roll number.")

        while True:
            try:
                age = int(input("Age: "))
                if age > 0:
                    break
                else:
                    print("Age must be positive.")
            except ValueError:
                print("Enter a valid age.")

        print("Enter marks for 5 subjects:")
        marks = input_marks()

        students.append({
            "name": name,
            "roll_no": roll_no,
            "age": age,
            "marks": marks
        })

    return count


# --- report section ---

def print_report():
    print("\n" + "=" * 60)
    print("           STUDENT SUMMARY REPORT")
    print("=" * 60)

    for s in students:
        name      = s["name"]
        roll_no   = s["roll_no"]
        age       = s["age"]
        marks     = s["marks"]

        total     = calculate_total(marks)
        avg       = calculate_average(marks)
        grade     = get_grade(avg)
        passed    = is_pass(avg)
        age_cat   = get_age_category(age)
        prime     = is_prime(roll_no)
        palindrome = is_palindrome(name)
        rev_roll  = reverse_roll(roll_no)
        highest   = max(marks)
        lowest    = min(marks)

        print(f"\n  Name        : {name}")
        print(f"  Roll Number : {roll_no}")
        print(f"  Age         : {age} ({age_cat})")
        print(f"  Marks       : {marks}")
        print(f"  Total       : {total}")
        print(f"  Average     : {avg:.2f}")
        print(f"  Grade       : {grade}")
        print(f"  Result      : {'PASS' if passed else 'FAIL'}")
        print(f"  Roll Prime  : {'Yes' if prime else 'No'}")
        print(f"  Palindrome  : {'Yes' if palindrome else 'No'}")
        print(f"  Reversed Roll: {rev_roll}")
        print(f"  Highest Mark: {highest}")
        print(f"  Lowest Mark : {lowest}")
        print("-" * 60)


def print_extras(student_count):
    # fibonacci up to student count
    print(f"\n  Fibonacci (first {student_count} numbers): {fibonacci(student_count)}")

    # roll numbers 100-200 divisible by both 3 and 5
    print("\n  Roll numbers (100-200) divisible by 3 and 5:")
    multiples = [n for n in range(100, 201) if n % 3 == 0 and n % 5 == 0]
    print(" ", multiples)

    # bonus: all primes between 1 and 100
    print("\n  Prime numbers (1-100):")
    print(" ", primes_in_range(1, 100))


# --- main ---

def main():
    print("=== Student Management System ===\n")
    count = input_students()
    print_report()
    print("\n" + "=" * 60)
    print("           EXTRA INFORMATION")
    print("=" * 60)
    print_extras(count)
    print("\n=== Done ===")


main()