##Lower Triangular Pattern
rows = 5
for i in range(1, rows + 1):
    print("* " * i)


##Upper Triangular Pattern
rows = 5
for i in range(rows, 0, -1):
    print("* " * i)


##Pyramid Pattern
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
