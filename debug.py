import ipdb
from lib import *



actor1 = Actor ('Brad Pitt' )
actor2 = Actor ('Al Pacino' )
actor3 = Actor ('Denzel Washington' )
actor4= Actor ('Oscar The Grouch')


role1 = Role('American Gansta')
role2 = Role('John Wick')
role3 = Role('IT')


aud1 = Audition ('Queens', False,  role1, actor1)
aud2 = Audition ('Brooklyn', False,  role2 , actor2)
aud3 = Audition ('Long Island', True,  role3, actor4)
aud3 = Audition ('Bronx', True,  role1, actor1)

# the below line allows us to stop & try stuff!
ipdb.set_trace()