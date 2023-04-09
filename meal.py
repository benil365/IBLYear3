def main():
    time = input("what is the time?:")
    if 7.0<= convert(time)<=8.00:
        print("breakfast")
    elif convert(time) >= 12.0 and convert(time) <= 13.00:
     print("lunch")
    elif convert(time) >=18.0 and convert(time) <=19.00:
      print("supper")
    else:
        print("not time to eat!!")

def convert(time):
    hours, minutes =time.split(":")
    hours= float(hours)
    minutes=float(minutes)
    minutes=minutes / 60
    return hours + minutes
main()