class Employee():
    count=0
    def __init__(self,name,email):
        self.name=name
        self.email=email
        Employee.count+=1
    def show(self):
        print('Name: ',self.name)
        print('Email ID: ',self.email)
class Manager(Employee):
    def __init__(self,name,email,project):
        self.project=project
        super().__init__(name,email)
    def show(self):
        super().show()
        print('Manager owned the project',self.project)

ob=Manager('Chandra','chandra_p@hcl.com','STAR')
ob1=Manager('mahesh','mahesh_k@hcl.com','STAR')
#print('dict',ob.__dict__)
ob.show()
'''print('Name:',ob.name)
print('Email:',ob.email)'''
print('Count',Manager.count)

