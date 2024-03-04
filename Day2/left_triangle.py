def left_triangle_pattern(n):
    for i in range(1, n + 1): #print space         
        for j in range(n - i):
            print("  ", end="")
        for k in range(i):
            print("* ", end="")
        print()
n = 5
left_triangle_pattern()
