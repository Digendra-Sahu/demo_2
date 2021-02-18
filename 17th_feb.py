#Class Complex
class complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        if self.imaginary >= 0:
            return f"{self.real} + {self.imaginary}j"
        return f"{self.real} {self.imaginary}j"
    
    def __add__(self, other):
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return complex(r, i)
    
    def __sub__(self, other):
        r = self.real - other.real
        i = self.imaginary - other.imaginary
        return complex(r, i)
    
    def __mul__(self, other):
        r = self.real * other.real - self.imaginary * other.imaginary
        i = self.real * other.imaginary + self.imaginary * other.real
        return complex(r, i)
    
    def __eq__(self, other):
        if self.real == other.real and self.imaginary == other.imaginary:
            return True
        return False

    def mod_comp(self):
        return  pow((self.real**2 + self.imaginary**2), 0.5)
    
    def __gt__(self, other):
        if self.mod_comp() > other.mod_comp():
            return True
        return False
    
    def __le__(self, other):
        if self.mod_comp() < other.mod_comp():
            return True
        return False
    
#Class Time
class time:
    def __init__(self, h,m,s):
        self.hr = h
        self.min = m
        self.sec = s
        if self.sec > 60:
            self.min += self.sec // 60
            self.sec %= 60
        if self.min > 60:
            self.hr += self.hr // 60
            self.min %= 60
    
    def __str__(self):
        return f"{self.hr}:{self.min}:{self.sec}"
    
    def __eq__(self, other):
        if self.hr > other.hr:
            return True
        return False
    
    def __add__(self, other):
        a = self.hr + other.hr
        b = self.min + other.min
        c = self.sec = other.sec
        return time(a,b,c)
    
    def __le__(self, other):
        pass
    
    def __gt__(self, other):
        pass

#Class Employee
class Employee:
    inc = 0
    salary = 0
    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email
    
    def apply_raise(self):
        self.salary *= 1 + (self.inc)/100
    
    def __str__(self):
        return f"{self.first} {self.last}"


class Engineer(Employee):
    def __init__(self,first,last, email, salary, interns=[]):
        super().__init__(first, last, email)
        self.salary = salary
        self.inc = 5
        self.interns = interns

    def add_int(self, n):
        if n not in self.interns:
            self.interns.append(n)

    def rem_int(self,n):
        if n not in self.interns:
            self.interns.remove(n)
        

class Manager(Employee):
    def __init__(self,first,last, email, salary, emps=[]):
        super().__init__(first, last, email)
        self.salary = salary
        self.inc = 10
        self.emps = emps
    
    def add_eng(self, n):
        if n not in self.emps:
            self.emps.append(n)
    
    def rem_eng(self, n):
        if n in self.emps:
            self.emps.remove(n)
    
    def dis_emps(self):
        for e in self.emps:
            print(f"Manager {self} has {e} as his employee")
    

class Trainee(Employee):
    def __init__(self,first,last, email, salary):
        super().__init__(first, last, email)
        self.salary = salary
        self.inc = 0
#Stack class
class Stack:
    def __init__(self, elements=None, max_ele):
        self.max_ele = max_ele
        if elements is None:
            self.elements = []
        else:
            self.elements = elements
    
    def pop_ele(self,n):
        pass
    
    def push_ele(self, n):
        if self.isfull():
            raise 

    def isempty(self):
        if len(self.elements) == 0 or self.elements == None:
            return True
        else:
            return False

    def isfull(self):
        pass