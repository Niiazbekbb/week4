def num_divide3(num):
    count = 0
    for x in range(1, num + 1):
        if x % 3 == 0:
            count += 1
    return count
while True:
    user_input = input("Enter a positive integer (or 'done' to exit): ")
    if user_input == 'done':
        print("bye !!")
        break
    try:
        num = int(user_input)
        if num > 0:
            divisible_count = num_divide3(num)
            print(f"Numbers divisible by 3 among numbers from 1 to {num} : {divisible_count}")
        else:
            print("Please enter a positive number")
    except ValueError:
        print("Please enter a positive integer or 'done' to exit")
