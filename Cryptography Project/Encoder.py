import numpy as np
import random
from matrixvariables import main_metrix  # This is the matrix which contain all the characters like "a","b"... etc.
from matrixvariables import indexing_metrix  # This is the matrix which contain the numbers 0,1,2,3,4,5,6,7,8 in a form of 3*3 matrix


# This function basically returns three parameters i.e. a rearranged version of the indexing metrix and the order of the rows and columns
def indexencoding1():
    i = [0, 1, 2]
    random.shuffle(i)
    res = indexing_metrix[:, i]
    j = [0, 1, 2]
    random.shuffle(j)
    res = res[j]
    return i, j, res


# encodestep1:-
# This function basically shuffle the matrix in a random way to get different outputs every single time.
# This function first rearrange the columns of the main matrix (res = metrix[:, i]) then rearrange the rows of the matrix(result = res[x]).
# Everytime the function is called it rearranges the main matrix in a new form.
# tis function returns three parameters i.e. the order of the shuffled column and row with the rearranged matrix as result
def encodestep1():
    i = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(i)
    res = main_metrix[:, i]
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(x)
    result = res[x]
    return i, x, result


# encodestep2:-
# This function takes two parameters one is the coordinates or in other word a list that contains the indexes of the elements you wnt to find and the second one is the matrix.
# It basically take the indexes from the list and search the elements at that indexes in the provided matrix.
# It returns a string which is made out off up the sticking the elements found at that index in to a string
def encodestep2(codinates, ciphermetrix):
    cipherlist = []
    for a in codinates:
        temp = str(ciphermetrix[a[0], a[1]])
        cipherlist.append(temp)
    cipherstring = "".join([str(x) for x in cipherlist])
    return cipherstring

# coordinates:-
# This function basically returns the coordinates of the element(arr) present in the given matrix(metrix1)
# cod is a list of the coordinates of the elements
def coordinates(arr, metrix1):
    cod = []
    for i in arr:
        temp = np.argwhere(metrix1 == i)
        tempa = temp.tolist()
        cod.append(*tempa)
    return cod


message = list(str(input("Enter the message: ")))  # this will take the message as input from the user
cl, ro, met = encodestep1()  # This function is called to get a random version of the main matrix and the order of the rows and column
co = coordinates(message, met)  # This function is called to get the initial coordinates of the individual character of the message
cl1, ro1, met1 = encodestep1()  # This encodestep1 is again called to get a new matrix
ciphertext = encodestep2(co, met1)  # This function is called to get the cipher text by getting the elements at same coordinates where the message elements were there
# This next part have used mainly to add a extra bit of encryption by changing the places of the indexes of column and rows which are present in the starting and ending of the cipher text
incls, inros, inmex = indexencoding1()  # This line calls the indexencoding1 function to return the shuffled form of the indexing matrix and the way the 3*3 matrix is arranged (column nad row)
# These next four lines basically do the same thing i.e. these lines will call the coordinates function which will return the coordinates of the stc(start cipher) and enc(end cipher)
cocls = coordinates(cl, inmex)  # The belong to start cipher
coros = coordinates(ro, inmex)  # The belong to start cipher
cocle = coordinates(cl1, inmex)  # The belong to end cipher
coroe = coordinates(ro1, inmex)  # The belong to end cipher
incle, inroe, inmexe = indexencoding1()  # This line calls the indexencoding1 function to return a new shuffled matrix so that the coordinates of the previous element we have will be applied and gather random numbers
# These next four lines basically takes the coordinates of the previous elements with the reshuffled matrix and returns the element that are present in the exact coordinates of the previous elements in the new matrix
encodcls = encodestep2(cocls, inmexe)  # This is the encoded form of cls
encodros = encodestep2(coros, inmexe)  # This is the encoded form of ros
encodcle = encodestep2(cocle, inmexe)  # This is the encoded form of cle
encodroe = encodestep2(coroe, inmexe)  # This is the encoded form of roe
# This next two lines will convert the four list into two separate strings that we will attach later
secretcodes = "".join([str(x) for x in incls]) + "".join([str(x) for x in inros])  # This line stitches the two lists i.e. incls and inros into one string
secretcodee = "".join([str(x) for x in incle]) + "".join([str(x) for x in inroe])  # This line stitches the two lists i.e. incle and inroe into one string
# This next two lines will convert the four list into two separate strings that we will attach later
stc = "".join([str(x) for x in encodcls]) + "".join([str(x) for x in encodros])    # This line stitches the two lists i.e. encodcls and encodros into one string
enc = "".join([str(x) for x in encodcle]) + "".join([str(x) for x in encodroe])    # This line stitches the two lists i.e. encodcle and encodroe into one string
# The next line prints the text, then first the stc(encodes start cipher) then the cipher text then anc(encoded end cipher)
print("Your encoded message is : ", stc + ciphertext + enc)
# This next line prints a secret key (The order in which after arranging the indexing_matrix you could recode the start cipher and the end cipher)
print("Your private key is : ", secretcodes + secretcodee)
