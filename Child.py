from Parent import Parent


class Child(Parent):

    def __init__(self):
        print("Calling Child Contractor");

    def childMethod(self):
        print("Calling Child Method")

    def parentMethod(self):
        print("Calling from Child");


c = Child();

c.childMethod()
c.parentMethod();
