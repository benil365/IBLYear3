class Student:
    def __init__(self, name, estates, course):
        if not name:
            raise ValueError("Please provide your name")
        self.name = name
        self.course = course
        self.estates = estates

    def __str__(self):
        return f"{self.name} is from {self.estates} and is doing {self.course}"

    #Getter for the estate
    @property
    def estates(self):
        return self._estates

    #Setter for the estate
    @estates.setter
    def estates(self, estate):
        self._estates = estate

def main():
    student = get_student()
    print(student)

def get_student():
    name = input("What is your name? ").strip()
    estates = input("Which estate do you come from? ").strip()
    course = input("Which course do you do? ").strip()
    return Student(name, estates, course)

if __name__ == "__main__":
    main()

