"""
Method for finding primitive Pythagorean triples {x, y, z}:
x = q^2 - p^2
y = 2qp
z = q^2 + p^2
"""


def compute_primitive_pythagorean_triple_sum(p, q):
    return ((q ** 2) - (p ** 2)) + (2 * p * q) + ((p ** 2) + (q ** 2))


def find_pythagorean_triples():
    counts_array = [0] * 1001

    for p in range(1, 21):
        for q in range(p + 1, 22):
            x = (q ** 2) - (p ** 2)
            y = 2 * p * q
            if (x - y) % 2 == 1:
                pythagorean_triple_sum = compute_primitive_pythagorean_triple_sum(p, q)

                # Add all multiples of the triple sum, ensuring it's <= 1000
                k = 1
                while k * pythagorean_triple_sum <= 1000:
                    counts_array[k * pythagorean_triple_sum] += 1
                    k += 1

    val = max(counts_array)
    return counts_array.index(val)


print(find_pythagorean_triples())
