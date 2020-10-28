class Pair():
    def __init__(self, val1=0, val2=0):
        self.val1 = val1
        self.val2 = val2

    def __str__(self):
        return "Value 1: {}, Value 2: {}".format(self.val1, self.val2)

    def __repr__(self):
        return "Pair({},{})".format(self.val1, self.val2)

    def __add__(self, other):
        return Pair(self.val1 + other.val1, self.val2 + other.val2)
        
pair1 = Pair(20,30)
print(pair1)          # Value 1: 20, Value 2: 30
pair2 = Pair(40,50)
pair3 = pair1 + pair2
print(pair3)          # Value 1: 60, Value 2: 80
        
#-------------------------------------------------------------------------------------

class MyString():
    def __init__(self, sentence=""):
        self.sentence = sentence

    def __repr__(self):
        return "{}".format(self.sentence)
    
    def __str__(self):
        return "{}".format(self.sentence)

    def __lt__(self, other):
        return len(self.sentence) < len(other.sentence)

    def __sub__(self, other):
        if (other > self):
            return len(other.sentence) - len(self.sentence)
        else:
            return len(self.sentence) - len(other.sentence)
            
str1 = MyString('this is a string')
str2 = MyString('this is another one')
print(str1 > str2)    # False
print(str1 - str2)    # 3
            
#-------------------------------------------------------------------------------------

class Rectangle():
    def __init__(self, val1=1, val2=1):
        self.val1 = val1
        self.val2 = val2
        if self.val1 < 0:
          self.val1 = 1
        if self.val2 < 0:
          self.val2 = 1

    def __repr__(self):
        return "Rectangle({},{})".format(self.val1, self.val2)

    def __str__(self):
        return "Length: {}, Width: {}".format(self.val1, self.val2)

    def area(self):
        return self.val2 * self.val1

    def perimeter(self):
        return 2*self.val2 + 2*self.val1

    def __eq__(self, other):
      rec1 = self.val1 * self.val2
      rec2 = other.val2 * other.val1
      return rec1 == rec2
      
rec1 = Rectangle()
rec2 = Rectangle(2,3)
print(rec1)             # Length: 1, Width: 1
print(rec2.area())      # 6
print(rec2.perimeter()) # 10
print(rec2.__repr__())  # Rectangle(2,3)
print(rec1 == rec2)     # False
      
#-------------------------------------------------------------------------------------

class CashRegister():
    def __init__(self, taxes=0):
        self.taxes = taxes
        self.balance = 0
        self.balancetaxed = 0
        self.counter = 0

    def add_item(self, cost, tax):
        self.cost = cost
        if tax == True:
          self.balance += self.cost
          self.cost = self.cost * (self.taxes * 0.01)
          self.balancetaxed += self.cost
          self.counter += 1
        else:
          self.balance += self.cost
          self.counter += 1
    
    def get_count(self):
        return self.counter

    def get_total(self):
        return round(self.balance, 2)

    def get_total_with_tax(self):
        return round((self.balancetaxed + self.balance), 2)

    def clear(self):
        self.balance = 0
        self.balancetaxed = 0
        self.counter = 0
        self.taxes = 0

    def __str__(self):
        return "Items: {}, total price: {:.2f}, including tax: {:.2f}".format(self.get_count(), self.get_total(), self.get_total_with_tax())
        
register1 = CashRegister(10.0)        # 10% tax rate
register1.add_item(3.5, False)        # The price of the item is 3.5, no tax
register1.add_item(10.0, True)        # The price of the item is 10.0, taxable 
print(register1)                      # Items: 2, total price: 13.50, including tax: 14.50

print(register1.get_count())          # 2
print(register1.get_total())          # 13.5
print(register1.get_total_with_tax()) # 14.5

register1.clear()
print(register1)                      # Items: 0, total price: 0.00, including tax: 0.00
