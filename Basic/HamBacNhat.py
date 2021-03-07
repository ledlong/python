def hamBacNhat(a,b):
    # This function is to solve the first order equation
    if a is not 0:
        c = -b/a
        print("This equation has only one solution x = {0}".format(c))
    else:
        if b == 0:
            print("This equation has many solutions")
        else:
            print("This equation has no solution")
