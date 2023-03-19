# Write your code below this line 👇

def prime_checker(number):
    count = 0
    for i in range(2, number+1):
        if number % i == 0:
            count += 1
    if count == 1:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

def prime_checker2(number):
    is_prime = True
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
prime_checker2(number = n)

