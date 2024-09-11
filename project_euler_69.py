
def compute_totients():
    totients = list(range(1000001))  # totients[i] = i initially

    #Reduce totient values by multiplying by (1 - 1/i) for all multiples of i <= 1000000
    for i in range(2, 1000001):
        if totients[i] == i:  #if i is a prime number
            for j in range(i, 1000001, i):
                totients[j] *= (i - 1)
                totients[j] //= i
    return totients


def find_max_totient_ratio():
    totients = compute_totients()

    max_ratio = 0
    max_n = 0

    #Find the integer with the maximum n/phi(n)
    for n in range(2, 1000001):
        ratio = n / totients[n]
        if ratio > max_ratio:
            max_ratio = ratio
            max_n = n

    return max_n, max_ratio


print(find_max_totient_ratio())

