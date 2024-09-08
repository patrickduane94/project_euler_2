
def fibonacci_sum(prev, curr, curr_sum):
    if curr < 4000000:
        temp = prev
        prev = curr
        curr = curr + temp
        if prev % 2 == 0:
            curr_sum += prev
        fibonacci_sum(prev, curr, curr_sum)
    else:
        print(curr_sum)


fibonacci_sum(0, 1, 0)
