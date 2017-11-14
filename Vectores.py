from math import acos, degrees #FROM MATH JUST IMPORT acos AND degrees
#acos: cos^-1 FOR GET THE ANGLE BETWEEN VECTORS
#degrees: THE FUNCTIONS WORK ON RAD, THIS IS A WAY TO PASS RAD TO DEG

def checkLen(vectorOne, vectorTwo):
    
    if len(vectorOne) != len(vectorTwo): #CHECK IF THE VETORS ARE IN THE SAME SPACE

        print('MATCH ERROR: vectors in different Rn')

        return False

    return True

def checkSpace(complex: vector):

    if isinstance(vector, complex):
        return True
    else:
        return False

def checkSpace(vector):

    if isinstance(vector, complex):
        return True
    else:
        return False

def vectorInnerProduct(vectorOne, vectorTwo): #GET THE INNER PRODUCT OF VECTORS

    if len(vectorOne) != len(vectorTwo): #CHECK IF THE VETORS ARE IN THE SAME SPACE

        print('MATCH ERROR: vectors in different Rn')

        return

    if checkSpace(vectorOne) and checkSpace(vectorTwo):

    rn = len(vectorOne) #GET THE LENGTH OF THE VECTOR
    innerProduct = 0 #INIT RESULT VARIABLE

    for i in range(0, rn): #DO THIS rn TIMES
        innerProduct += vectorOne[i] * vectorTwo[i]

    return innerProduct

def vectorNorm(vector): #GET THE NORM OF A VECTOR

    return (vectorInnerProduct(vector, vector))**(1/2) #WE KNOW THAT THE NORM IS THE SQRT OF THE INNER PRODUCT OF THE VECTOR WITH ITSELF

def vectorAngle(vectorOne, vectorTwo): #GET THE ANGLE BETWEEN TWO VECTORS

    if len(vectorOne) != len(vectorTwo):

        print('MATCH ERROR: vectors in different Rn')

        return

    innerProduct = vectorInnerProduct(vectorOne, vectorTwo) #SET THE INNER PRODUCT BETWEEN THE TWO VECTORS
    norms        = vectorNorm(vectorOne) * vectorNorm(vectorTwo) #SET THE PRODUCT BETWEEN THE NORM OF THE VECTORS


    if norms == 0: #JUST IN CASE WE ARE DEALING WITH A VECTOR ZERO

        print("ERROR: divided by zero")

        return

    return degrees(acos(innerProduct/norms)) #PASS THE RESULT FROM RAD TO DEGREES
