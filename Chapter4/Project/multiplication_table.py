for element1 in range(1, 10):
    for element2 in range(1, element1 + 1):
        product = element2 * element1
        print(" %d * %d = %d" % (element2, element1, product), end="")
    print()