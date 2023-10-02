while True:
    user_input = input("Please_enter_a_positive_number: ")
    if user_input == 'done':
        print("Bye !!")
        break

    try:
        num = int(user_input)

        def num_divide3(num):
            count = 0

            for i in range(1, num + 1):
                if i % 3 == 0:
                    count = count + 1

            return count

        if num < 1:
            print("Please enter a positive number.")
        else:
            result = num_divide3(num)
            print("Numbers divisible by 3 among numbers from 1 to", num, ":", result)
    except ValueError:
        print("Invalid input. Please enter a positive number or 'done' to exit.")