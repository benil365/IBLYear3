def main():
    answer= input("great question of universe,life,and everything?:")
    if great_question(answer) ==True:
        print("Yes.")
    else:
        print("No.")
def great_question(answer):
    return answer=="42" or answer=="forty-two" or answer ==" forty two"
main()