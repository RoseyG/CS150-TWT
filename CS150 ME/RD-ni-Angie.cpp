#include <iostream>
#include <cstdlib>
#include <fstream>

/*! \file
    \brief 
    Implements the recursive descent algorithm.
    
    Receives the file name of the input as an argument passed to the program from the command line
    


*/


/*!File where the input is stored*/
std::ifstream file;
/*!Token type of nextChar*/
int charClass;
/*!the lexeme to be displayed*/
char lexeme[100];
/*!Length of the lexeme*/
int lexLen;

/*!The next token from the input*/
int nextToken;
/*!The next lexeme from the input*/
char nextChar;
/*!Determines if there is a syntax error encountered*/
int SUC=1;
/*! Deteremines if the parenthesis are balanced*/
int PCOUNTER=1;
/*! Adds nextChar to the lexeme array*/
void addChar();
/*! Clasifies the lexeme(nextChar) generally before passing to the lexical analyzer */
void getChar();
/*! Clasifies the lexeme(nextChar) specifically and sets the value of the nextToken to the token of the lexeme(nextChar) */
int lookup(int);
/*!Gets the spaces from the input*/
void getWSpace();
/*!The lexical analyzer, turns input to tokens*/
int lex();
/*!Applies the rule E-> E+T|E-T|T
\n Calls the T() 
and will iteratively call lex() and T() while */
void E();
/*!Applies the rule T-> T*F|T/F|F*/
void T();
/*!Applies the rule F->(E)|id*/
void F();
/*!Applies the rule id->a|b|c*/
void ID();
/*!Applies the rule A->id=E*/
void A();
/*!Sets SUC to 0*/
void error();

/*!Token value of a letter */
#define LETTER 0
/*!Token value of a digit */
#define DIGIT 1
/*!Token value of a unknown lexeme */
#define UNKNOWN 99
/*!Token value of a equal sign (=) */
#define EQ  19
/*!Token value of an int literal (0-9) */
#define INT_LIT 10
/*!Token value of an id */
#define IDENT 11
/*!Token value of a addition operator (+) */
#define ADD_OP 21
/*!Token value of a substraction operator (-) */
#define SUB_OP 22
/*!Token value of a multiplication operator (*) */
#define MULT_OP 23
/*!Token value of a division operator (/) */
#define DIV_OP 24
/*!Token value of a left pranthesis '(' */
#define LEFT_PAREN 25
/*!Token value of a right parenthesis ')' */
#define RIGHT_PAREN 26

int main(int argc,char* argv[]){
    file.open(argv[1],std::ifstream::in);
    if (file.good()){
        getChar();
        lex();
        A();
    }
    else {
        SUC=-1;
    }
    
    if (SUC==1){
        std::cout<<"STRING ACCEPTED";
    }
    else if (SUC==-1){
        std::cout<<"ERROR: FILE NOT FOUND";
    }
    file.close();
    return  0;
       
}

void addChar() {
    if (lexLen <= 98) {
        lexeme[lexLen++] = nextChar;
        lexeme[lexLen] = 0;
    }
    else
    std::cout<<"Error - lexeme is too long \n";
    
}
void getChar() {
    if ((nextChar = file.get()) != EOF) {
        if (isalpha(nextChar)){
            charClass = LETTER;
        }
        else if (isdigit(nextChar)){
            charClass = DIGIT;
        }    
        else{ 
            charClass = UNKNOWN;
        }
    }
    else{
        charClass = EOF;
    }
}

void getWSpace(){
    while (isspace(nextChar)){
        getChar();
    }
}

int lookup(char ch) {
    switch (ch) {
        case '=':
            addChar();
            nextToken= EQ;
            break;
        case '(':
            addChar();
            nextToken = LEFT_PAREN;
            break;
        case ')':
            addChar();
            nextToken = RIGHT_PAREN;
            break;
        case '+':
            addChar();
            nextToken = ADD_OP;
            break;
        case '-':
            addChar();
            nextToken = SUB_OP;
            break;
        case '*':
            addChar();
            nextToken = MULT_OP;
            break;
        case '/':
            addChar();
            nextToken = DIV_OP;
            break;
        default:
            addChar();
            nextToken = EOF;
            break;
    }
    return nextToken;
}

int lex() {
    lexLen = 0;
    getWSpace();
    switch (charClass) {
        case LETTER:
            addChar();
            getChar();
            while (charClass == LETTER || charClass == DIGIT) {
                addChar();
                getChar();
            }
            nextToken = IDENT;
        break;
        case DIGIT:
            addChar();
            getChar();
            while (charClass == DIGIT) {
                addChar();
                getChar();
            }
            nextToken = INT_LIT;
            break;
        case UNKNOWN:
            lookup(nextChar);
            getChar();
            break;
        case EOF:
            nextToken = EOF;
            lexeme[0] = 'E';
            lexeme[1] = 'O';
            lexeme[2] = 'F';
            lexeme[3] = 0;
            break;
    } 
    std::cout<<"Next token is: "<<nextToken<<"\tNext Lexeme is: "<<lexeme<<"\n";
    return nextToken;
}

void A(){

    std::cout<<"Enter <A>\n";
    ID();
    if (nextToken==EQ && SUC){
        lex();
        E();
    }
    else {
        std::cout<<"SYNTAX ERROR: EXPECTED '=' ";
        error();
    }
    if (!SUC){
        return;
    }
    std::cout<<"EXIT <A>\n";
}
void E(){

    std::cout<<"Enter <E>\n";
    T();
    if (!SUC){
        return;
    }
    while ((nextToken==ADD_OP || nextToken==SUB_OP)&& SUC){
        lex();
        T();
    }
    if (!SUC){
        return;
    }
    std::cout<<"EXIT <E>\n";
}
void T(){

    std::cout<<"Enter <T>\n";
    F();

    while ((nextToken==MULT_OP || nextToken==DIV_OP)&& SUC){
        lex();
        F();
    }
    
    if (!SUC){
        return;
    }
    std::cout<<"EXIT <T>\n";
}
void F(){
    
    std::cout<<"Enter <F>\n";
    if (nextToken==IDENT){
        ID();
        if (nextToken==LEFT_PAREN){
            std::cout<<"SYNTAX ERROR: EXPECTED OPERATOR TOKEN \n";
            error();
            return;
        }

    }
    else{
        if( nextToken==LEFT_PAREN){
            ++PCOUNTER;
            lex();
            E();
            if( nextToken==RIGHT_PAREN){
                lex();
                
                if (nextToken==IDENT || nextToken==LEFT_PAREN) {
                    std::cout<<"SYNTAX ERROR: EXPECTED OPERATOR TOKEN \n";
                    error();
                    return;
                }
            }
            else {
                std::cout<<"SYNTAX ERROR: EXPECTED \' ) \' \n";
                error();
                return;
            }
        }
		else {
		  std::cout<<"SYNTAX ERROR: EXPECTED \' (  \' \n";
		  error();
		  return;
		}
    }
    if (nextToken==RIGHT_PAREN) {
          if(--PCOUNTER<=0){
		      std::cout<<"SYNTAX ERROR: EXPECTED \' (  \' \n";
		      error();
		      return;
        }           
		              
    }
    /*
	else {
	   std::cout<<"SYNTAX ERROR: EXPECTED \' (  \'";
		error();
		return;
		}
    */
    if (!SUC){
        return;
    }
    std::cout<<"EXIT <F>\n";
}
void ID() {
    std::cout<<"Enter <id>\n";
    
    if ((lexeme[0]=='a'||lexeme[0]=='b'||lexeme[0]=='c') && lexLen==1){
        std::cout<<"EXIT <id>\n";
        lex();
    }
    else{
        std::cout<<"SYNTAX ERROR: EXPECTED ID TOKEN\n";
        //std::cout<<"---ERROR AT ID----\n";
        error();
        return;
    }
    
    
}

void error(){
   SUC=0;
}
