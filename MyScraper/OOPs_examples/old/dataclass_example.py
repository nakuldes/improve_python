from dataclasses import dataclass

@dataclass
class Employee:
    name : str
    emp_no : int
    user_id : str
    age : int
    

instance1 = Employee('n1', 1, 'u1', 25)
instance2 = Employee('n2', 2, 'u2', 22)
instance3 = Employee('n3', 3, 'u3', 23)
instance4 = Employee('n4', 4, 'u4', 24)

print(instance1)
print(instance2)
print(instance3)
print(instance4)


class ClassWithRepr:
    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:

        return "class Classwithreppr {0}".format(self.name)

ins1= ClassWithRepr('nakul')
print(ins1)