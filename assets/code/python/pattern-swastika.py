def pattern(mag):
    if mag % 2 != 1:
        return "Line magnitude must be an odd number"
    mid = mag // 2 + 1

    for i in range(1, mag + 1):
        for j in range(1, mag + 1):
            if (
                i == mid
                or j == mid
                or (i == 1 and j > mid)
                or (i == mag and j < mid)
                or (j == 1 and i < mid)
                or (j == mag and i > mid)
            ):
                print("* ", end="")
            else:
                print("  ", end="")

        print()


pattern(int(input("Enter magnitude: ")))
