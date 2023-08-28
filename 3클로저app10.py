def counter(init_count = 0):
    current_counter = init_count
    def increase(cnt = 1):
        nonlocal current_count
        current_count += cnt
        return current_counter
    return increase

mycounter = counter(0)
yourcounter = counter(100)
print(mycounter())
print(yourconuter())
print(mycounter())
print(yourcounter())
del mycounter
del(yourcounter)
