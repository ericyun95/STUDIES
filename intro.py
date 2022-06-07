
# 3-1
"""
change = int(input())
if change % 10 != 0:
    print("wrong")
coins = [500, 100, 50, 10]
number = 0
for i in range(len(coins)):
    if change == 0:
        break
    elif change >= coins[i]:
        number += change // coins[i]
        change = change % coins[i]
    else:
        continue
print(number)
"""

# 3-2
"""
from random import *
n, m, k = map(int, input("numbers?").split())
data = []
for i in range(n):
    data.append(randint(1, 50))
print(data)
data.sort()
first = data[-1]
second = data[-2]

result = 0
count = 0
if first == second:
    result +=  m*first
else :
    while m > 0:
        if count >= k:
            result += second
            m -= 1
            count = 0
        else:
            result += first
            m -= 1
            count += 1
print(result)
"""

#3-3
"""
from random import *

m, n = map(int, input().split())
deck = []
for i in range(n):
    cards = []
    for j in range(m):
        cards.append(randint(1,50))
    deck.append(cards)
print(deck)
for cards in deck:
    cards.sort()

max = deck[0][0]
belong = 1
for i in range(n-1):
    if deck[i][0] < deck[i+1][0]:
        max = deck[i+1][0]
        belong = i+2
    else:
        continue
print(max, belong)
"""

#3-4
"""
n, k = map(int, input().split())
count = 0
while True:
    if n == 1:
        print(n, count)
        break
    elif n%k == 0:
        n /= k
        count += 1
        print(n, count)
    else:
        n -= 1
        count += 1
        print(n, count)
"""

#4-1
x = 1
y = 1
commands = ["L", "R", "U", "D"]
movements = [[-1, 0], [1, 0], [0, -1], [0, 1]]

n = int(input("map size?"))
print(n)
plans = input("plans?").split()
print(plans)
for plan in plans:
    for i in range(len(commands)):
        if plan == commands[i]:
            x += movements[i][0]
            y += movements[i][1]
            if (x>=1 and x <= n) and (y>=1 and y <= n):
                print(x, y)
                continue
            else:
                x -= movements[i][0]
                y -= movements[i][1]
                print(x, y)

