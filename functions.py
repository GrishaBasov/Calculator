
def addition():
    print(float(First)+float(Second),"Yyyees!")

def subtraction():
    Sub = float(First)-float(Second)
    if Sub<0:
        print("Can't subtract")
    else:
        print(float(First)-float(Second),"Wow")

def multiplication():
    print(float(First)*float(Second),"Uhhuuu!")

def division():
    if int(Second)==0:
        print("ooo shit! can't do that!")
    else:
        print(float(First) / float(Second), "Uhhuuu!")
