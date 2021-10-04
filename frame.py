def Frame(size):
    print("*" * size)
    for i in range(size-2):
        print("*", " "*(size-4), "*")

    print("*" * size)


Frame(4)
