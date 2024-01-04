#Write a Python script to Display all the prime numbers between 1 to 250 and Store the results in a results.txt file.
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

def save_to_file(primes, filename='results.txt'):
    with open(filename, 'w') as file:
        for prime in primes:
            file.write(str(prime) + '\n')

if __name__ == "__main__":
    start_range = 1
    end_range = 250

    prime_numbers = find_primes(start_range, end_range)

    print("Prime numbers between {} and {}: {}".format(start_range, end_range, prime_numbers))

    save_to_file(prime_numbers)
