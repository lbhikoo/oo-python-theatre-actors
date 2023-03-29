from .audition import Audition

        
#Roles should only have a character_name (string), 
# have many auditions, 
# and have many actors through auditions.

class Role:
    all = []

    def __init__(self, character):
        self.character = character
        Role.all.append(self)
        

#Role#auditions returns all 
# of the auditions associated with this role.
        
    @property    
    def auditions(self):
        return [a for a in Audition.all if a.role == self]
    
#Role#actors returns a 
#list of names from the actors associated with this role.

    @property
    def actors(self):
        return [a.actor.character for a in self.auditions]
    
#Role#locations returns a list of 
# locations from the auditions associated with this role.
    
    @property
    def locations(self):
        return [l.location for l in self.auditions]
    

    
    @classmethod
    def silver_screen(cls):
        return f"Hired Characters are { [ a.role.character for a in Audition.all if a.hired == True]} "
    
