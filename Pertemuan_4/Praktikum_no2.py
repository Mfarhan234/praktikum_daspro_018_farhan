X, Y = map(int, input().split())
x, y = map(int, input().split())
M = int(input())

if (x == 0 and y == 0) or (x == 0 and y == Y) or (x == X and y == 0) or (x == X and y == Y):
    kk = 3
elif (x == 0) or (y == 0) or (x == X) or (y == Y):
    kk = 5
else:
    kk = 8

if M == 0:
    kk = 0

if M >= 1:
    x1, y1 = map(int, input().split())
    if (x + 1 == x1 or x - 1 == x1) or (y + 1 == y1 or y - 1 == y1):
        kk -= 1

if M >= 2:
    x2, y2 = map(int, input().split())
    if (x + 1 == x2 or x - 1 == x2) or (y + 1 == y2 or y - 1 == y2):
        kk -= 1

if M >= 3:
    x3, y3 = map(int, input().split())
    if (x + 1 == x3 or x - 1 == x3) or (y + 1 == y3 or y - 1 == y3):
        kk -= 1

if M >= 4:
    x4, y4 = map(int, input().split())
    if (x + 1 == x4 or x - 1 == x4) or (y + 1 == y4 or y - 1 == y4):
        kk -= 1

if M >= 5:
    x5, y5 = map(int, input().split())
    if (x + 1 == x5 or x - 1 == x5) or (y + 1 == y5 or y - 1 == y5):
        kk -= 1

if M >= 6:
    x6, y6 = map(int, input().split())
    if (x + 1 == x6 or x - 1 == x6) or (y + 1 == y6 or y - 1 == y6):
        kk -= 1

if M >= 7:
    x7, y7 = map(int, input().split())
    if (x + 1 == x7 or x - 1 == x7) or (y + 1 == y7 or y - 1 == y7):
        kk -= 1

if M >= 8:
    x8, y8 = map(int, input().split())
    if (x + 1 == x8 or x - 1 == x8) or (y + 1 == y8 or y - 1 == y8):
        kk -= 1

if kk > 0:
    print("Senshi makan hari ini!")
else:
    print("Senshi makannya besok aja deh.")
