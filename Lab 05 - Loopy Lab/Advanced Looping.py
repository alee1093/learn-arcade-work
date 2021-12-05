for row in range(10):
    print("* ", end="")
print("")
print("")

for row in range(10):
    print("* ", end="")
print("")
for row in range(5):
    print("* ", end="")
print("")
for row in range(21):
    print("* ", end="")
print("")
print("")

for row in range(10):
    for column in range(10):
        print("* ", end="")
    print("")
print("")

for row in range(10):
    for column in range(5):
        print("* ", end="")
    print("")
print("")

row = 0
while row < 5:
    column = 0
    while column < 20:
        print("* ", end="")
        column += 1
    row += 1
    print("")
print("")

row = 0
while row < 10:
    column = 0
    while column < 10:
        print(column, " ", end="")
        column += 1
    row += 1
    print("")
print("")

row = 0
while row < 10:
    column = 0
    while column < 10:
        print(row, " ", end="")
        column += 1
    row += 1
    print("")
