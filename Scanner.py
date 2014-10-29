from sys import *

# ASSIGNING VALUES TO THE GLOBAL VARIABLES

lexeme = ['']*99
file = None
LETTER = 0
DIGIT = 1
MULT_OP = 23
INT_LIT = 10
IDENT = 11
UNKNOWN = 99
LEFT_PAREN = 25
RIGHT_PAREN = 26
nextToken = 1
nextChar = ""
EOF =-1
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
DIV_OP = 24


#DEFINING THE FUNCTION ADDCHAR()
def addChar():
    global lexLen,lexeme
    if lexLen <= 98:       
        lexeme[lexLen + 1] = nextChar
        lexeme[lexLen] = 0
    else:
        print "Error:lexeme is too long." 


#DEFINING THE LOOKUP FUNCTION
def lookup(ch):      
    global nextToken,charClass,nextChar
    if ch == '(':
        addChar()
        nextToken = LEFT_PAREN  #LOOKS FOR LEFT PARENTHASIS
    elif ch == ')':
        addChar()
        nextToken = RIGHT_PAREN #LOOKS FOR RIGHT PARENTHASIS
    elif ch == '+':
        addChar()
        nextToken = ADD_OP   #LOOKS FOR ADDITION OPERATOR
    elif ch == '-':
        addChar()
        nextToken = SUB_OP   #LOOKS FOR SUBSTRACTION OPERATOR
    elif ch == '=':
        addChar()
        nextToken = ASSIGN_OP   #LOOKS FOR EQUAL OPERATOR
    elif ch == '*':
        addChar()
        nextToken = MULT_OP   #LOOKS FOR MULTIPLICATION OPERATOR
    elif ch == '/':
        addChar()
        nextToken = DIV_OP  #LOOKS FOR DIVISION OPERATOR
    else:
        addChar()
        nextToken = EOF


#DEFINING THE GETCHAR FUNCTION
def getChar():
    global file,nextToken,charClass,nextChar
    try:
        rd = file.read(1)
        if rd != "-1":
            nextChar = rd
            if nextChar.isalpha():
                charClass = LETTER
            elif nextChar.isdigit():
                charClass = DIGIT
            else:
                charClass = UNKNOWN            
        else:
            charClass = EOF
            nextChar = '\0'        
    except Exception, e:
        print e


#DEFINING THE GETNONBLANK FUNCTION
def getNonBlank():
    global nextChar
    while nextChar.isspace():
        getChar()
    
#DEFINING THE LEX FUNCTION
def lex():
    global nextToken,charClass,lexLen,lexeme,nextChar
    lexLen = 0
    lexeme = ['']*99
    getNonBlank()
    if charClass == LETTER:
        addChar()
        getChar()        
        while charClass == LETTER:
            addChar()
            getChar()
        nextToken = IDENT
    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT
    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()
    elif charClass == EOF:
        nextToken = EOF
        lexeme[0] = 'E'
        lexeme[1] = 'O'
        lexeme[2] = 'F'
        lexeme[3] = '\0'
        
    if nextToken!=-1:    #THE NEXT TOKEN GETS PRINTED
    	print "Next token is: " + str(nextToken)
	print "Next lexeme is " + str(lexeme[1])
	print " "
    
    else:     # IF NEXT TOKEN IS -1 THE EOF WILL BE PRINTED
    	print "Next token is: " + str(nextToken)
	print "Next lexeme is EOF"

#DEFINING THE MAIN FUNCTION     
def main():    
    global file,nextToken,nextChar
    try:
        file = open("front.txt", "r")                  
    except Exception, e:
        print "ERROR: cannot open front.in"
    finally:
        getChar()
        temp = 0	#TEMPORARY VARIABLE FOR CHECKING EOF
    while nextToken != EOF:      
        lex() 
        temp+=1
    file.close()

main()