from .audition import Audition


#Actors should only have name ( string ), 
# have many auditions, 
# and have many roles through auditions.

class Actor:
    all = []
    def __init__(self, name):
        self.name = name
        Actor.all.append(self)
      
#Actor#auditions returns a list of 
# auditions this actor attended.
    @property
    def auditions(self):
        audition_list = [a for a in Audition.all if a.actor == self]
        return audition_list


#Actor#roles returns a list of 
# roles the actor auditioned for.

    @property
    def roles(self):
       role_list = [a.role for a in self.auditions ]
       return role_list
    

   
    @property
    def characters(self):
       return [a.role.character for a in self.auditions ]
    
    @property
    def paycheck(self):
        return [ a.role.character for a in self.auditions if a.hired == True]
       
    
    