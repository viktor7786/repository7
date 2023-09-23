class Student:
    def __init__(self, name, address, phone, course, index_number):
        self.name = name
        self.address = address
        self.phone = phone
        self.course = course
        self.index_number = index_number

    def getinfo(self):
        return "Name:" + self.name + "\nAddress: " + self.address + "\nPhone: " + self.phone + "\nCourse: " + self.course + "\nIndex Number: " + self.index_number
    
  

student1 = Student("Viktor Disevic", "S.Plainfield Road Chicago Il 60525", "(202)812 30 69", "Solidity","001234275")
student2 = Student("Victor Di Sevich", "Rivermont Terrace Ashburn Va 44072", "(202)473 38 38", "Blockchain Tehnology", "10011010")
student3 = Student("Satoshi Nakamoto","West Forster Ave 46852 Los Angeles Ca", "(506)263 343","How to create Bitcoin","00001")

print(student1.getinfo())
print(student2.getinfo())
print(student3.getinfo())



        































