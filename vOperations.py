from math import acos, degrees #FROM MATH JUST IMPORT acos AND degrees
#acos: cos^-1 FOR GET THE ANGLE BETWEEN VECTORS
#degrees: THE FUNCTIONS WORK ON RAD, THIS IS A WAY TO PASS RAD TO DEG

def vInnerProduct(vOne, vTwo): #GET THE INNER PRODUCT OF VECTORS

    if len(vOne) != len(vTwo): #CHECK IF THE VETORS ARE IN THE SAME SPACE

        print('MATCH ERROR: vectors in different Rn')

        return

    n            = len(vOne)#GET THE LENGTH OF THE VECTOR
    innerProduct = 0        #INIT RESULT VARIABLE

    if isinstance(vOne, complex) or isinstance(vTwo, complex):
        #INNER PRODUCT OF COMPLEX VECTORS
        for i in range(0, n):
            innerProduct += vOne[i] * vTwo[i].conjugate()
    else:
        #INNER PRODUCT OF REAL NUMBERS
        for i in range(0, n): #DO THIS rn TIMES
            innerProduct += vOne[i] * vTwo[i]

    return innerProduct

def vNorm(v): #GET THE NORM OF A VECTOR

    if isinstance(v, complex):
        print("Simon")
    return (vInnerProduct(v, v))**(1/2) #WE KNOW THAT THE NORM IS THE SQRT OF THE INNER PRODUCT OF THE VECTOR WITH ITSELF

def vAngle(vOne, vTwo): #GET THE ANGLE BETWEEN TWO VECTORS

    if len(vOne) != len(vTwo):

        print('MATCH ERROR: vectors in different Rn')

        return

    innerProduct = vInnerProduct(vOne, vTwo) #SET THE INNER PRODUCT BETWEEN THE TWO VECTORS
    norms        = vNorm(vOne) * vNorm(vTwo) #SET THE PRODUCT BETWEEN THE NORM OF THE VECTORS


    if norms == 0: #JUST IN CASE WE ARE DEALING WITH A VECTOR ZERO

        print("ERROR: divided by zero")

        return

    return degrees(acos(innerProduct/norms)) #PASS THE RESULT FROM RAD TO DEGREES


a = [1+2j]
b = [2+3j]

print(vInnerProduct(a,b))
