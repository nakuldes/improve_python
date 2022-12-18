class Patient:
    def set_id(self, id):
        self.__id = id
    
    def set_name(self, name):
        self.__name = name

    def set_ssn(self, ssn):
        self.__ssn = ssn
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_ssn(self):
        return self.__ssn

p = Patient()
p.set_id(1)
p.set_name('John')
p.set_ssn('112233')
print(p.get_id())
print(p.get_name())
print(p.get_ssn())

p1 = Patient()
p1.set_id(2)
p1.set_name('Jack')
p1.set_ssn('998877')
print(p1.get_id())
print(p1.get_name())
print(p1.get_ssn())