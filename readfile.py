with open("names.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print("hello,",line.strip())

#senior developers
with open("names.txt", "r") as file:
    for line in file:
     print("hello,",line.strip())       