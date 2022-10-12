# We import mod1 as the whole or we can import some of the members.
# if you import the whole module then from keyword is not useful.
import functions.mod1 as mod1
from functions.mod1 import my_function as mdf
from functions.mod1 import get_time as timef
# when import the whole module
mod1.my_function()
mod1.get_time()

# when using from keyword
mdf()
timef()


