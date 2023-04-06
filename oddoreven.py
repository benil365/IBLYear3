def main():
    x=int(input("what is the value of x:"))
    if mod(x):
        print ("even")
    else:
        print("odd")
def mod(n):
      if n%2==0:
            return True
      else:
            return False
main()        