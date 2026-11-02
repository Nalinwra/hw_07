
from collections import deque

names = input("Names: ").split(",")

players = deque()

for name in names:
    players.append(name.strip())

passes = int(input("Passes: "))

while len(players) > 1:

    for i in range(passes):
        player = players.popleft()
        players.append(player)

    out = players.popleft()

    print(out, "is out")

print("Winner:", players[0])
