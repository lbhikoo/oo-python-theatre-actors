# Auditions should have a location (string), 
# hired (boolean), 
# belong to a role, 
# and belong to an actor.


class Audition:

    all = []
    def __init__(self, location, hired,role,actor):
        self.location = location
        self.hired = hired
        self.role = role
        self.actor = actor
        Audition.all.append(self)


    def call_back(self):
        self.hired = True
# Audition#call_back()
# will change the the hired attribute to True.