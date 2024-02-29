def prime_number(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

choice = int(input("Enter a number to check weather it's prime or not\n"))
prime_number(number=choice)