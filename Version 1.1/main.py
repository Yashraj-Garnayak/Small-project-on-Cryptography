# This is going to a OOPs version of my cryptography project
import numpy as np
import random
from matrix_variables import main_metrix  # This is the matrix which contain all the characters like "a","b"... etc.
from matrix_variables import \
    indexing_metrix  # This is the matrix which contain the numbers 0,1,2,3,4,5,6,7,8 in a form of 3*3 matrix


class Mainframe:
    def __init__(self):
        self.Encoder = self.Encoder()
        self.Decoder = self.Decoder()

    def encode(self):
        message = list(str(input("Enter the message: ")))  # this will take the message as input from the user
        cl, ro, met = self.Encoder.encodestep1()  # This staticmethod is called to get a random version of the main matrix and the order of the rows and column
        co = self.Encoder.coordinates(message,
                                      met)  # This staticmethod is called to get the initial coordinates of the individual character of the message
        cl1, ro1, met1 = self.Encoder.encodestep1()  # This encodestep1 is again called to get a new matrix
        ciphertext = self.Encoder.encodestep2(co,
                                              met1)  # This staticmethod is called to get the cipher text by getting the elements at same coordinates where the message elements were there
        # This next part have used mainly to add a extra bit of encryption by changing the places of the indexes of column and rows which are present in the starting and ending of the cipher text
        incls, inros, inmex = self.Encoder.indexencoding1()  # This line calls the indexencoding1 staticmethod to return the shuffled form of the indexing matrix and the way the 3*3 matrix is arranged (column nad row)
        # These next four lines basically do the same thing i.e. these lines will call the coordinates staticmethod which will return the coordinates of the stc(start cipher) and enc(end cipher)
        cocls = self.Encoder.coordinates(cl, inmex)  # The belong to start cipher
        coros = self.Encoder.coordinates(ro, inmex)  # The belong to start cipher
        cocle = self.Encoder.coordinates(cl1, inmex)  # The belong to end cipher
        coroe = self.Encoder.coordinates(ro1, inmex)  # The belong to end cipher
        incle, inroe, inmexe = self.Encoder.indexencoding1()  # This line calls the indexencoding1 staticmethod to return a new shuffled matrix so that the coordinates of the previous element we have will be applied and gather random numbers
        # These next four lines basically takes the coordinates of the previous elements with the reshuffled matrix and returns the element that are present in the exact coordinates of the previous elements in the new matrix
        encodcls = self.Encoder.encodestep2(cocls, inmexe)  # This is the encoded form of cls
        encodros = self.Encoder.encodestep2(coros, inmexe)  # This is the encoded form of ros
        encodcle = self.Encoder.encodestep2(cocle, inmexe)  # This is the encoded form of cle
        encodroe = self.Encoder.encodestep2(coroe, inmexe)  # This is the encoded form of roe
        # This next two lines will convert the four list into two separate strings that we will attach later
        secretcodes = "".join([str(x) for x in incls]) + "".join(
            [str(x) for x in inros])  # This line stitches the two lists i.e. incls and inros into one string
        secretcodee = "".join([str(x) for x in incle]) + "".join(
            [str(x) for x in inroe])  # This line stitches the two lists i.e. incle and inroe into one string
        # This next two lines will convert the four list into two separate strings that we will attach later
        stc = "".join([str(x) for x in encodcls]) + "".join(
            [str(x) for x in encodros])  # This line stitches the two lists i.e. encodcls and encodros into one string
        enc = "".join([str(x) for x in encodcle]) + "".join(
            [str(x) for x in encodroe])  # This line stitches the two lists i.e. encodcle and encodroe into one string
        # The next line prints the text, then first the stc(encodes start cipher) then the cipher text then anc(encoded end cipher)
        print("Your encoded message is : ", stc + ciphertext + enc)
        # This next line prints a secret key (The order in which after arranging the indexing_matrix you could recode the start cipher and the end cipher)
        print("Your private key is : ", secretcodes + secretcodee)

    def decode(self):
        ciphermessage = str(input("Enter the encoded text : "))
        secret_key = str(input("Please provide your secret key : "))
        stc, enc, ciphertext = self.Decoder.dissect(
            ciphermessage)  # This line calls the dissect method to divide the encoded message into three parts
        keyst, keyend = self.Decoder.keydissect(
            secret_key)  # This line calls the keydissect method to divide the secret key into two parts
        # From the next line the first the decryption of data is being started
        endkeymatrix = self.Decoder.secretmatrix(
            keyend)  # This line will call the method to get the initial rearranged form of the indexing_matrix
        # These next two lines are used to get the coordinates of the stc and enc in the endkeymatrix
        stcco = self.Decoder.coordinates_of_stc_enc(stc, endkeymatrix)  # This is to get the the coordinates of stc
        encco = self.Decoder.coordinates_of_stc_enc(enc, endkeymatrix)  # This is to get the the coordinates of stc
        startkeymetrix = self.Decoder.secretmatrix(
            keyst)  # This line is to get the new rearranged form of indexing_matrix according to the the new columns and rows
        # These next next two lines re used to get the original column and row combination
        stcdecoded = self.Decoder.element_finder(stcco, startkeymetrix)
        encdecoded = self.Decoder.element_finder(encco, startkeymetrix)
        enmetrix = self.Decoder.decode(
            encdecoded)  # Now with the help of the decoded enc we could get the rearranged main_matrix I.e. the step one to decode the message
        co = self.Decoder.coordinates(ciphertext,
                                      enmetrix)  # This line will call the coordinates method which will give he coordinates or in other word the indexes of he element present in the respective palaces of the provided matrix
        startmetrix = self.Decoder.decode(stcdecoded)  # Now the original main_matrix to get the decoded code
        simpletext = self.Decoder.element_finder(co,
                                                 startmetrix)  # This line will call the element_finder method to get the actual message
        print("The secret code is :", simpletext)

    class Encoder:

        # This staticmethod basically returns three parameters i.e. a rearranged version of the indexing metrix and the order of the rows and columns
        @staticmethod
        def indexencoding1():
            tempclm = [0, 1, 2]
            random.shuffle(tempclm)
            result = indexing_metrix[:, tempclm]
            temprow = [1, 0, 2]
            random.shuffle(temprow)
            result = result[temprow]

            return tempclm, temprow, result

        # encodestep1:-
        # This staticmethod basically shuffle the matrix in a random way to get different outputs every single time.
        # This staticmethod first rearrange the columns of the main matrix (res = metrix[:, i]) then rearrange the rows of the matrix(result = res[x]).
        # Everytime the staticmethod is called it rearranges the main matrix in a new form.
        # tis staticmethod returns three parameters i.e. the order of the shuffled column and row with the rearranged matrix as result

        @staticmethod
        def encodestep1():
            tempclm = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            random.shuffle(tempclm)
            res = main_metrix[:, tempclm]
            temprow = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            random.shuffle(temprow)
            result = res[temprow]
            return tempclm, temprow, result

        # encodestep2:-
        # This staticmethod takes two parameters one is the coordinates or in other word a list that contains the indexes of the elements you wnt to find and the second one is the matrix.
        # It basically take the indexes from the list and search the elements at that indexes in the provided matrix.
        # It returns a string which is made out off up the sticking the elements found at that index in to a string
        @staticmethod
        def encodestep2(codinates, ciphermetrix):
            cipherlist = []
            for a in codinates:
                temp = str(ciphermetrix[a[0], a[1]])
                cipherlist.append(temp)
            cipherstring = "".join([str(x) for x in cipherlist])
            return cipherstring

        # coordinates:-
        # This staticmethod basically returns the coordinates of the element(arr) present in the given matrix(metrix1)
        # cod is a list of the coordinates of the elements
        @staticmethod
        def coordinates(arr, mex):
            arr = list(arr)
            cod = []
            for i in arr:
                temp = np.argwhere(mex == i)
                tempa = temp.tolist()
                cod.append(*tempa)
            return cod

    class Decoder:
        # The dissect staticmethod is used to dissect the code or the cipher into parts i.e. stc, etc, and the cipher text
        @staticmethod
        def dissect(cimsg):
            x = int(len(cimsg)) - 18
            return cimsg[:18], cimsg[-18:], cimsg[18:x]

        @staticmethod
        # This keydissect staticmethod is takes the secret key and then dissect it into two parts which are  going to be the the row and column of the indexing_matrix
        def keydissect(fullkey):
            return fullkey[:6], fullkey[-6:]

        @staticmethod
        # secretmatrix:-
        # This staticmethod take a string then convert it into a list and then convert the individual str in the list to integer.
        # with the help of the integers the indexing_matrix is rearranged accordingly
        # This staticmethod returns an rearranged matrix according to the key.
        def secretmatrix(key):
            tempclm = list(key[:3])
            tempclm = [int(x) for x in tempclm]
            result = indexing_metrix[:, tempclm]
            temprow = list(key[-3:])
            temprow = [int(x) for x in temprow]
            result = result[temprow]
            return result

        @staticmethod
        # decode:-
        # This staticmethod takes a string i.e. the stc or enc to rearrange the main_matrix
        # this staticmethod first rearrange the columns then the rows
        def decode(clm_ro_order_string):
            tempclm = list(clm_ro_order_string[:9])
            tempclm = [int(x) for x in tempclm]
            result = main_metrix[:, tempclm]
            temprow = list(clm_ro_order_string[-9:])
            temprow = [int(x) for x in temprow]
            result = result[temprow]
            return result

        @staticmethod
        # element_finder:-
        # This staticmethod takes two parameter i.e. codinates(coordinates) and simpletextmatrix
        # The codinates is list that contains the indexes of the element, with the codinates you have to find which elements are present in the respective paces of he given matrix
        # This staticmethod returns a string of the elements present in the respective indexes that we have provided
        def element_finder(codinates, simpletextmetrix):
            cipherlist = []
            for a in codinates:
                temp = str(simpletextmetrix[a[0], a[1]])
                cipherlist.append(temp)
            cipherstring = "".join([str(x) for x in cipherlist])
            return cipherstring

        @staticmethod
        # # coordinates:-
        # # This staticmethod basically returns the coordinates of the element(arr) present in the given matrix(metrix1)
        # # cod is a list of the coordinates of the elements
        def coordinates(arr, mex):
            arr = list(arr)
            cod = []
            for i in arr:
                temp = np.argwhere(mex == i)
                tempa = temp.tolist()
                cod.append(*tempa)
            return cod

        @staticmethod
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


if __name__ == '__main__':
    _ = True


    def check(n):
        if n == 1:
            Mainframe.Encoder()
        else:
            Mainframe.Decoder()


    while _:
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  -------")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t| Welcome |".upper())
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t  -------")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t1.Encrypt message")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2.Decrypt message")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t0.Exit the program")
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tChoose the program:")
        inpt = int(input("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tChoose the program: "))
        if inpt == 1:
            start = Mainframe()
            start.encode()
        elif inpt == 2:
            start = Mainframe()
            start.decode()
        elif inpt == 0:
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tThank you for using our service....")
            exit()

        else:
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tInvalid input, Please enter again:")
            continue