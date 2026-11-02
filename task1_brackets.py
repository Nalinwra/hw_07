
line = input(" ")

stack = []
pairs = {")": "(", "]": "[", "}": "{"}

problem = None

for i, char in enumerate(line):
    if char in "([{":
        stack.append((char, i))

    elif char in ")]}":
        if len(stack) == 0:
            problem = i
            break

        bracket, position = stack.pop()

        if bracket != pairs[char]:
            problem = i
            break

if problem is None and len(stack) > 0:
    bracket, position = stack[-1]
    problem = position

if problem is None:
    print("Balanced")
else:
    print("Problem at position", problem, ":", line[problem])
    print(line)
    print(" " * problem + "^")
