from collections import defaultdict

# Initialize an empty dictionary to store item counts
items = defaultdict(int)

# Prompt the user for input
print("Enter your grocery list, one item per line:")
while True:
    try:
        item = input().strip().lower()
        if not item:
            break
        items[item] += 1
    except EOFError:
        break

# Print the grocery list
print("Here is your grocery list:")
for item in sorted(items.keys()):
    count = items[item]
    print(f"{count} {item.upper()}")