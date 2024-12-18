class CustomString:
    def __init__(self,name):
        self.name = name

    def __add__(self,other):
        return CustomString(self.name+other.name)
    def __str__(self):
        return self.name
    
ob1 = CustomString('sum')
ob2 = CustomString('shr')
print(ob1.__add__(ob2))
print(ob1+ob2)