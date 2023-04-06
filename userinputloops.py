def main():
    number =get_number()
    helloworld(number)
def get_number():
    while True:
        x=int(input("enter value of x\n:"))
        if x >0:
            break
    return x
def helloworld(x):
        for _ in range(x):
            print("helloworld")
main()