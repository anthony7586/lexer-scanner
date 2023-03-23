

##this is the main for the lexer scanner 

# function named lexer(), which will be responsible for returning a token when required. 
# unction should return a record that contains two fields: one for the token and the other for the actual value
  #of the token, also known as the lexeme

#expected output:

#_TOKENS___________LEXEMES ___
    #keyword        while
    #separator      (
    #identifier     t
    #operator       <
    #identifier     lower
    #separator      )
    #identifier     r
    #operator       =
    #real           28.00
    #separator      ;

from lexer import lexer
import numpy as np 
import matplotlib.pyplot as plt





#opens output file and rewrites it so that we have a fresh one for every run 
f = open("output.txt", "w")
f.write("Token__________Lexeme\n")
f.write("_____________________\n")
f.close()

lexer() #the FSM will be within the lexer function
        #lexer funtion returns the tokens and lexemes 

#open and read the file after writing to it
f = open("output.txt", "r")
print(f.read())





