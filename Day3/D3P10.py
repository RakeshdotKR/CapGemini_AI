# Class attributes & Instance attributes
class Team:
    slogan = "Team unity" #class attribute: shared 

    def __init__(self,name):
        self.name = name #instance attribute
        self.members = []

t1 = Team("Alpha")
t2 = Team("Beta")
print(t1.name, t2.name, Team.slogan)

t1.name = "NewName"
print(t1.name, t2.name, Team.slogan)