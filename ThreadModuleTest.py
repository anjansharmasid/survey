
class ClassA:
    attributeA = "Some attributeA value"
    attributeB = "Some attributeB value"

    def __init__(self,name,address):
        self.attributeA=name
        self.attributeB=address

    def printme(self):
        print(f'attributeA: {self.attributeA}')
        print(f'attributeB: {self.attributeB}')



class PII:
    attributeA_PII = "Some PII data field"
    attributeB_PII = "Some more PII data field"

    def __init__(self,email,phomenumber):
        self.attributeA_PII=email
        self.attributeB_PII=phomenumber

    def printme(self):
        i_am_a_local_variable = "i_am_a_local_variable"
        print(f'self.attributeA_PII: {self.attributeA_PII}')
        print(f'self.attributeB_PII:{self.attributeB_PII}')
        print(f'local variable:{i_am_a_local_variable}')



class Person(ClassA,PII):
    pass
    person_attributeA="Some default person_attributeA"

    def __init__(self, ClassA, PII, Bank_name ):
        self.ClassA=ClassA
        self.PII=PII
        self.person_attributeA = Bank_name

    def printme(self):
        print(self.person_attributeA)


instanceClassA = ClassA("John","London")
instanceClassPII = PII("John@john.net","07756453420")
bank_Name = "HSBC London UK"
person = Person(instanceClassA,instanceClassPII,bank_Name)
person.printme()
person.ClassA.printme()
person.PII.printme()

