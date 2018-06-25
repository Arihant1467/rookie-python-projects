class PartyAnimal:
    age=0
    name=""
    points=0
    def __init__(self,z,t):
        self.name=z
        self.age=t
        print (z,"constructed")
    def __del__(self):
        print(self.name,"deleted")
    def party(self):
        self.points=7
an=PartyAnimal("Arihant",21)
an.party()
print (dir(an))