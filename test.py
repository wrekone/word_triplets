arr = "I love food. blah blah".split()
print(arr)
its = [iter(arr), iter(arr[1:]), iter(arr[2:])]
print(its)
zip(*its)
print(its)