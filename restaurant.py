def main():
    dollar=dollar_to_float(input("what is the cost:"))
    percent= percent_to_float(input("percentage to convert:"))
    tip = dollar * percent
    print(f"leave ${tip:.2f}")

def dollar_to_float(d):
    d =d.replace("$","")
    d=float(d)
    return d

def percent_to_float(p):
    p= p.replace("%","")
    p= float(p)/100
    return p

main()