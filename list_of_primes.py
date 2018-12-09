# This function gets an integer and returns a list of prime numbers between 2 and the integer-1.
def list_of_primes(n):
    list_of_prime_numbers=[]
    for number in range(2,n):
        list_of_prime_numbers.append(number)
        for devisor in range(2,number):
            if number%devisor==0 and devisor!=number:
                list_of_prime_numbers.remove(number)
                break
    return(list_of_prime_numbers)

print(list_of_primes(20))
