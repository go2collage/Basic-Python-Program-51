# Python Program

# Super class & Subclass

# Super Class

class Degree():

    # Super Class Method
    def getDegree(self):
        print("I got a degree.")

# Subclass  1
class Undergraduate(Degree):

    # Subclass Method
    def show(self):
        print("I am an Undergraduate.")

# Subclass  2
class Postgraduate(Degree):

    def show(self):
        print("I am a Postgraduate.")

# Creating object

deg = Degree()
under_deg = Undergraduate()
post_deg = Postgraduate()

# Call Methods
deg.getDegree()
under_deg.show()
post_deg.show()

# Call Superclass Method
print("---------------------------------")
under_deg.getDegree()
post_deg.getDegree()


# Thanks for Watching
