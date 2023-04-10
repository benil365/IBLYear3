import sys

def format_names(names):
    n = len(names)
    if n == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif n == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        middle = ", ".join(names[1:-1])
        return f"Adieu, adieu, to {names[0]}, {middle}, and {names[-1]}"

names = []
for line in sys.stdin:
    name = line.strip()
    if name:
        names.append(name)

print("\n".join(format_names(names) for names in (names[:i] for i in range(1, len(names) + 1))))