def main():
    grt = str(input("greetings:"))
    answer(grt)
def answer(grt):
    if grt == "hello":
        print("$0")
    elif grt[0]== "h":
        print ("$20")
    else:
            print("$100")
main()