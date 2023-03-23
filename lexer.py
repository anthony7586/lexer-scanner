#desired output:
    
    #keyword while
    #separator (
    #identifier t
    #operator <
    #identifier lower
    #separator )
    #identifier r
    #operator =
    #real 28.00
    #separator ;


###################################################################################################

    #Anthony Ruiz 
    #Anthony.ruiz@csu.fullerton.edu    
    #CPSC 323 Compilers & Languages 2023 Spring
    #Project 1

###################################################################################################

from comparisons import is_letter, is_seperator, is_keyword, is_operator


def lexer():
    print ("executing lexer function...")
   # print ("                           ")
   # print ("Token           Lexeme     ")
   # print ("___________________________")

# program to read file char by char 
#will put chars together to form a word and will do the same to put a number together 


    word = '' # this will hold the string 
    number = '' # this will be a number 
    #these are the states to be later used for a part of the much larger FSM 
    q0 = 0
    q1 = 1 
    q2 = 2 
   
    current_numeric_state = 3
    previous_ch = ''

    with open("input_scode.txt") as fileobj: #while() not end of file  
        for line in fileobj:                 #read in file line by line
             for ch in line:                 #char by char 



                 if is_letter(ch) == True: #checks to see if ch is a letter and not symbol or space
                    word += ch #append to word, remains in state 

                 if ch == ' ' or (is_seperator(ch) or is_operator(ch)) == True: #if there is a space word is complete
                               #what kind of word is it, identifier or Keyword

                    if is_keyword(word) == True:
                       # print("keyword = "+ word) #print keyword   TOKEN
                        f = open("output.txt", "a")
                        f.write("Keyword =        "+ word + "\n")
                        f.close() 
                        word = ''                 #clear the word                        

                    if (is_keyword(word) == False) and word != ' 'and word != '' and (is_operator(ch) == False) and (is_seperator(ch) == False):
                        #print("identifier =          "+ word)           #  TOKEN
                        f = open("output.txt", "a")
                        f.write("identifier =       "+ word + "\n")
                        f.close() 
                        word = ''                 #clear the word

                 
                 
                 if ch.isnumeric() or ch == '.':  
                     number += ch #add into string if it is numeric
                     
                     

                     if current_numeric_state == q1:# now we have ##.##
                         current_numeric_state = q2 

                     if current_numeric_state == q2:# this is output state 
                        # print("real =          " + number)#print the number             #  TOKEN
                         f = open("output.txt", "a")
                         f.write("real =            "+ number + "\n")
                         f.close() 
                         number = '' #clear the number variable 
                         current_numeric_state = 3 

                     if current_numeric_state == q0: #now we have ##.#X
                         current_numeric_state = q1

                     if ch == '.': 
                         current_numeric_state = q0 #initial state after '.'
                                            # number = ##.XX



                 if is_seperator(ch) == True : #check for ;                         #  TOKEN
                     #print("separator = " + ch) #prints the character (seperator)
                     f = open("output.txt", "a")
                     f.write("separator =       "+ ch + "\n")
                     f.close()  


                 if is_operator(ch) == True:                                        #  TOKEN
                     #print ("operator = "+ ch)    
                     f = open("output.txt", "a")
                     f.write("operator =        "+ ch + "\n")
                     f.close()                 
               
        

