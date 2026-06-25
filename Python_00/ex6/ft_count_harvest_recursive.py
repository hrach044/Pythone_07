def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def helper(i):
        if i > n:
            return
        else:
            print(f"Day {i}")
        helper(i + 1)
    helper(1)
    print("Harvest time!")
