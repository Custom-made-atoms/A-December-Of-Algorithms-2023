b = int(input("Enter the width of the rectangle: "))
h = int(input("Enter the height of the rectangle: "))
r = int(input("Enter the radius of the circle: "))
def rec_in_cir(b,h,r):
    diag = (b**2+h**2)**0.5
    if diag<=2*r:
        print("true")
    else:
        print("false")
rec_in_cir(b,h,r)
