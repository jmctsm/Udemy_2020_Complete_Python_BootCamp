from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets


# very basic function
def f(x):
    return x


# Generate a slider to interact with
interact(f, x=10)
interact(f, x=True)
interact(f, x="Hi There!")

# using a decorator
@interact(x=True, y=1.0)
def g(x, y):
    return (x,y)



