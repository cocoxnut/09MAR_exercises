msum = 0
for i in range(1,10):
    if i % 3 == 0 or i % 5 == 0:
        msum += i
        print(i)
print(msum)
