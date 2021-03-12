2. შექმენით კლასი Calculator და განუსაზღვრეთ ისეთი ფუნქციები რომ კლასმა
შეძლოს შემდეგი ოპერაციების შესრულება
a. შეკრიბოს ორი რიცხვი
b. გამოაკლოს ორი რიცხვი
c. გაყოს ორი რიცხვი
d. გაამრავლოს ორი რიცხვი

"""
class Calculator:

    def __init__(self, a, b):
        self.a, self.b = a, b

    def addition(self):
        print(f'{self.a} + {self.b} = {self.a + self.b}')

    def subtract(self):
        print(f'{self.a} - {self.b} = {self.a - self.b}')

    def multiplication(self):
        print(f'{self.a} * {self.b} = {self.a * self.b}')

    def division(self):
        print(f'{self.a} / {self.b} = {self.a / self.b}')


if __name__ == '__main__':
    a = Calculator(3, 5)
    a.addition()
    a.subtract()
    a.multiplication()
    a.division()

"""

3. შექმენით კლასი Rectangle. ინიციალიზაციის დროს განუსაზღვრეთ პარამეტრები
width და length. კლასს შეუქმენით შემდეგი მეთოდები:
a. area() -> უნდა ითვლიდეს მართკუთხედის ფართო
b. perimeter() -> უნდა ითვლიდეს მართკუთხედის პერიმეტრს
c. print_info() -> უნდა ბეჭდავდეს მართკუთხედის სიგრძეს, სიგანეს, ფართობს
და პერიმეტრს თვალისთვის ადვილად აღსაქმელ ფორმატში.

"""
class rectangle():
    def init(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(a,b)
print("Area of rectangle:",obj.area())
 
print()

"""

4. შექმენით კლასი Employee. ინიციალიზაციის დროს განუსაზღვრეთ პარამეტრები
name, surname, age, salary. კლასს განუსაზღვრეთ მეთოდები საჭიროებისამებრ.
წაიკითხეთ ინფორმაცია თანამშრომლების შესახებ თანდართული csv
ფაილიდან(dataset1.csv) და შექმენით Employee კლასის ობიექტების სია. ამ სიაში
იპოვეთ ისეთი თანამშრომელი რომელსაც აქვს ყველაზე დაბალი ხელფასი და
დაბეჭდეთ ინფორმაცია ამ თანამშრომლის შესახებ. ამავე სიაში იპოვეთ ყველაზე
ხანდაზმული თანამშრომელი და დაბეჭდეთ ინფორმაცია მის შესახებ.

"""

class Employee:
    def __init__(self, name, surname, age, salary):
        self.name, self.surname, self.age, self.salary = name, surname, age, salary

    def info(self):
        return f'სახელი {self.name}, გვარი {self.surname}, ასაკი {self.age}, ხელფასი {self.salary}'


employees = []

with open("dataset1.csv", "r") as dataset:
    data = [line.split(",") for line in dataset.read().split("\n")][1:-1]
    employees = [Employee(name, surname, age, salary) for [name, surname, age, salary] in data]

print(f'თანამშრომელი ყველაზე დაბალი ხელფასით - {min(employees, key=lambda employee: employee.salary).info()}')
print(f'თანამშრომელი ყველაზე მაღალი ასაკით - {max(employees, key=lambda employee: employee.age).info()}')

"""