import numpy as np
from matrixvariables import main_metrix  # This is the matrix which contain all the characters like "a","b"... etc.
from matrixvariables import indexing_metrix   # This is the matrix which contain the numbers 0,1,2,3,4,5,6,7,8 in a form of 3*3 matrix

# The dissect function is used to dissect the code or the cipher into parts i.e. stc, etc, and the cipher text
def dissect(cimsg):
    x = int(len(cimsg)) - 18
    return cimsg[:18], cimsg[-18:], cimsg[18:x]

# This keydissect function is takes the secret key and then dissect it into two parts which are  going to be the the row and column of the indexing_matrix
def keydissect(fullkey):
    return fullkey[:6], fullkey[-6:]

# secretmatrix:-
# This function take a string then convert it into a list and then convert the individual str in the list to integer.
# with the help of the integers the indexing_matrix is rearranged accordingly
# This function returns an rearranged matrix according to the key.
def secretmatrix(key):
    tempclm = list(key[:3])
    tempclm = [int(x) for x in tempclm]
    result = indexing_metrix[:, tempclm]
    temprow = list(key[-3:])
    temprow = [int(x) for x in temprow]
    result = result[temprow]
    return result

# decode:-
# This function takes a string i.e. the stc or enc to rearrange the main_matrix
# this function first rearrange the columns then the rows
def decode(clm_ro_order_string):
    tempclm = list(clm_ro_order_string[:9])
    tempclm = [int(x) for x in tempclm]
    result = main_metrix[:, tempclm]
    temprow = list(clm_ro_order_string[-9:])
    temprow = [int(x) for x in temprow]
    result = result[temprow]
    return result

# element_finder:-
# This function takes two parameter i.e. codinates(coordinates) and simpletextmatrix
# The codinates is list that contains the indexes of the element, with the codinates you have to find which elements are present in the respective paces of he given matrix
# This function returns a string of the elements present in the respective indexes that we have provided
def element_finder(codinates, simpletextmetrix):
    cipherlist = []
    for a in codinates:
        temp = str(simpletextmetrix[a[0], a[1]])
        cipherlist.append(temp)
    cipherstring = "".join([str(x) for x in cipherlist])
    return cipherstring

# # coordinates:-
# # This function basically returns the coordinates of the element(arr) present in the given matrix(metrix1)
# # cod is a list of the coordinates of the elements
def coordinates(arr, mex):
    arr = list(arr)
    cod = []
    for i in arr:
        temp = np.argwhere(mex == i)
        tempa = temp.tolist()
        cod.append(*tempa)
    return cod

# coordinates_of_stc_enc:-
# This basically does the same thing as coordinates does but before searching it just convert the elements to integer
# It returns a list which contain the indexes of the elements of the given string arr
def coordinates_of_stc_enc(arr, mex):
    arr = list(arr)
    arr = [int(x) for x in arr]
    cod = []
    for i in arr:
        temp = np.argwhere(mex == i)
        tempa = temp.tolist()
        cod.append(*tempa)
    return cod


ciphermessage = str(input("Enter the encoded text : "))
secretKey = str(input("Please provide your secret key : "))
stc, enc, ciphertext = dissect(ciphermessage)   # This line calls the dissect function to divide the encoded message into three parts
keyst, keyend = keydissect(secretKey)   # This line calls the keydissect function to divide the secret key into two parts
# From the next line the first the decryption of data is being started
endkeymatrix = secretmatrix(keyend)    # This line will call the function to get the initial rearranged form of the indexing_matrix
# These next two lines are used to get the coordinates of the stc and enc in the endkeymatrix
stcco = coordinates_of_stc_enc(stc, endkeymatrix)   # This is to get the the coordinates of stc
encco = coordinates_of_stc_enc(enc, endkeymatrix)   # This is to get the the coordinates of stc
startkeymetrix = secretmatrix(keyst)    # This line is to get the new rearranged form of indexing_matrix according to the the new columns and rows
# These next next two lines re used to get the original column and row combination
stcdecoded = element_finder(stcco, startkeymetrix)
encdecoded = element_finder(encco, startkeymetrix)
enmetrix = decode(encdecoded)   # Now with the help of the decoded enc we could get the rearranged main_matrix I.e. the step one to decode the message
co = coordinates(ciphertext, enmetrix)  # This line will call the coordinates function which will give he coordinates or in other word the indexes of he element present in the respective palaces of the provided matrix
startmetrix = decode(stcdecoded)    # Now the original main_matrix to get the decoded code
simpletext = element_finder(co, startmetrix)   # This line will call the element_finder function to get the actual message
print("The secret code is :", simpletext)   # This line will print the actual message or we can say the decoded message
