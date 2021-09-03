# A simple example class
class Employee:
    num=0
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'
        Employee.num+=1
    def fullname(self):
        print('{} {}'.format(self.first,self.last))
    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount
    @classmethod
    def from_string(cls,emp):
         first,last,pay=emp.split('-')
         return cls(first,last,pay)
    @staticmethod
    def is_working(day):
        if day.weekday()==5 or day.weekday==6:
            return False
        return True
emp1=Employee('Vinayak','Ravva',50000)
emp2=Employee('Mahesh','Ravva',60000)
emp3='Vishnu-Ravva-458520'
import datetime
my_date = datetime.date(2021,3,28)
print(Employee.is_working(my_date))
print(my_date)
a,b,*c=[1,2,3,4,5]
print(a,b,c)


