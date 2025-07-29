class Parent:
    parentAttr = 100;

    def __init__(self):
        print("Calling Parent Contractor")

    def parentMethod(self):
        print("Calling Parent Method")

    def setAttr(self, attr):
        Parent.parentAttr = attr;

    def getAttr(self):
        print("Get Parent Attribute", Parent.parentAttr);

