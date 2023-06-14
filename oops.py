class Plane:
    def __init__(self,plane_have_wings,colour):
        self.plane_have_wings=plane_have_wings
        self.colour=colour
        
    def planefly(self):
        if self.plane_have_wings==2:
            print("The plane should be able to fly")
        else:
            pass
class Jet(Plane):
    def __init__(self,colour):
        self.colour=colour
    def colourofjet(self):
        print(self.colour)
              
class Passenger(Plane):
    def __init__(self,colour):
        self.colour=colour
    def colourofpassenger(self):
        print(self.colour)
obj1plane=Plane(2,'pink')
obj2ofjet=Jet('orange')
obj3ofpassenger=Passenger('green')
obj1plane.planefly()
obj2ofjet.colourofjet()
obj3ofpassenger.colourofpassenger()



