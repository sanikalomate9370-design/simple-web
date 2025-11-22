#create a class student having attribute as first name,last name,qualification and
# methods as update quali,show details 
class student:
    def __init__(self,first_name,last_name,qualification):
        self.first_name
        self.last_name
        self.qualification
    def upd_qua(quali):
        self.qualification = quali
    def display(self):
        print("first name os student:",self.first_name)
        print("last name os student:",self.last_name)
        print("qualification of student:",self.qualification)
name=input("enter a name")
surname=input("enter a surname")
qua=input("enter a qualification")
s1=student(name,surname,qua)
s1.display()
n=input("enter a new qualification")
s1.upd_qua(n)
s1.display()
