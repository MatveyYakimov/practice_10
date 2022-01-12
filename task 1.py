def finabochi(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return finabochi(n - 1) + finabochi(n - 2)


print(finabochi(0))
print(finabochi(1))
print(finabochi(3))
