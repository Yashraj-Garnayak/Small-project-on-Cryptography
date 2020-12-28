import numpy as np
# These are the two matrix which will be used by he two files Encoder.py and Decoder.py

# This first matrix contain all the characters a user could enter
main_metrix = np.array([["a", "b", "c", "d", "e", "f", "g", "h", "i"],
                        ["j", "k", "l", "m", "n", "o", "p", "q", "r"],
                        ["s", "t", "u", "v", "w", "x", "y", "z", " "],
                        ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        ["0", "A", "B", "C", "D", "E", "F", "G", "H"],
                        ["I", "J", "K", "L", "M", "N", "O", "P", "Q"],
                        ["R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
                        ["!", "@", "#", "$", "%", "&", "(", ")", "_"],
                        [".", "?", "+", "-", "<", ">", "/", ",", ";"]])

# This indexing_matrix mainly used for the encoding and decoding of the stc and enc
indexing_metrix = np.array([[0, 1, 2],
                            [3, 4, 5],
                            [6, 7, 8]])
