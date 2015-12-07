#include <iostream>
#include <cstdlib>
#include <fstream>
#include <stack>
#include <istream>
#include <queue>
/*! \file
    \brief 
    Implements the LR parser.
    
    Receives the file name of the input as an argument passed to the program from the command line
    


*/



/*!File where the input is stored*/
std::ifstream file;
/*!Stack to be used by the SLR PARSER */
std::stack<int> stack;
/*!State of the input during the parsing*/
std::queue<char> input;
/*!Will return the number of items to be popped from the stack given the rule number*/
int rule(int);
/*!Rule to be used*/
char rule_var;
/*! Implements the parse table via nested switch, first switch for the states and the second switch (for every state) is for the token/variables*/
void action();
/*!The nextToken of from the input*/
char nextToken;
/*!The current state*/
int state;
/*!Applies the shifting step of the SLR Parsing: Push the nextToken to the Stack and the passed state to the stack.
\n Next state will be the top of the stack*/
void shift(int);
/*!Applies the reducing step of the SLR Parsing: Pops r* times from the Stack pushes the rule variable used 
\n*r -> value passed by the rule() and its state*/
void reduce(int);
/*!Determines if there is a syntax error encountered or not*/
int SUC=0;
/*!Prints stack*/
void print(std::stack<int> &); 
/*!Prints queue (input)*/
void print(std::queue<char> &,int);
/*!Gets the spaces from the input*/
void getWSpace();
/*!Determines if an input is push to the stack*/
int get;

/*!
Opens and reads the file. 
Calls the action()  iteratively until the parser encountered an error or if the parsing is a success.
*/
int main(int argc,char* argv[]){
    file.open(argv[1],std::ifstream::in);
    get=0;
    if (file.good()){
        while (nextToken!=EOF){
            nextToken=file.peek();
            getWSpace();
            nextToken=file.get();
            if (nextToken!=EOF){
                input.push(nextToken);
            }
             
        }
    }
    else {
        std::cout<<"FILE NOT FOUND";
        return 0;
    }
    
    input.push('$');
    file.clear();
    file.seekg(0,file.beg);
    stack.push(0);
    state=0;
    
    do{
        nextToken=file.peek();
        if (get){
            input.pop();
            --get;
        }
        getWSpace();
        std::cout<<"STACK: ";
        print(stack);
        std::cout<<"\nINPUT: ";
        print(input,input.size());
        std::cout<<"ACTION: ";
        action();
        std::cout<<"\n\n";
    }while (SUC==0);
    std::cout<<"SUCCESS?"<<SUC;
    file.close();
    return  0;
       
}

int rule(int n){
    switch (n){
        case 1:
            rule_var='A'; return 6;
        case 2:
            
        case 3:
            rule_var='E'; return 6;
        case 5:
        case 6:
            rule_var='T'; return 6;
        case 8:
            rule_var='F'; return 6;
        case 4:
            rule_var='E'; return 2;
        case 7:
             rule_var='T'; return 2;
        case 9:
            rule_var='F'; return 2;
        case 10:
        case 11:
        case 12:
            rule_var='I';
            return 2;
        
    }
}

void shift(int x){
        std::cout<<"s"<<x;
        stack.push(file.get());
        stack.push(x);
        state=stack.top();
        ++get;
}
void reduce (int r){
    std::cout<<"r"<<r;
    r=rule(r);
    
    
    for (int i=0; i<r;i++){
        stack.pop();
    }
    //std::cout<<"\n enter reduce";
    state=stack.top();
    std::cout<<"(";
    if (rule_var =='I'){
        std::cout<<"id";
    }
    else {
        std::cout<<rule_var;
    }    
    std::cout<<", "<<state<<")";
    nextToken=rule_var;
    stack.push(rule_var);
    action();                   
    //std::cout<<"\n exit reduce";                                                                                                                                                                                                                                                                   
}

void action(){
     
    switch (state){
        case 0:
            switch (nextToken){
                case 'a':
                    shift(3);
                    break;
                case 'b':
                    shift(4);
                    break;
                case 'c':
                    shift(5);
                    break;
                case 'A':
                    stack.push(1);
                    state=1;
                    break;
                case 'I':
                    stack.push(2);
                    state=2;
                    
                    break;
                default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED ID\n";
                    SUC=-1;
                }
			  break;
        case 1:
            if (nextToken==EOF){
                SUC=1;
                std::cout<<"acc";
            }
            else{ 
                std::cout<<"\nSYNTAX ERROR: EXPECTED EOF \n";
                SUC=-1;
			}
            break;
        case 2:
            if (nextToken=='='){
                shift(6);
            }
            else{
                std::cout<<"\nSYNTAX ERROR: EXPECTED \'= \' \n"; 
                SUC=-1;
			}
            break;
        case 3:
			switch(nextToken){
				case '=':
				case '+':
				case '-':
				case '*':
				case '/':
				case ')':
				case EOF:
					reduce(10);
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED OPERATOR TOKEN OR \')\' \n";
					SUC=-1;
			}
			break;
		case 4:
			switch(nextToken){
				case '=':
				case '+':
				case '-':
				case '*':
				case '/':
				case ')':
				case EOF:
					reduce(11);
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED OPERATOR TOKEN OR \')\' OR EOF\n";
					SUC=-1;
			}
			break;
		case 5:
			switch(nextToken){
				case '=':
				case '+':
				case '-':
				case '*':
				case '/':
				case ')':
				case EOF:
					reduce(12);
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED OPERATOR TOKEN OR \')\' OR EOF \n";
					SUC=-1;
			}
			break;
		case 6:
			switch(nextToken){
				case '(':
					shift(10);
					break;
                case 'a':
                    shift(3);
                    break;
                case 'b':
                    shift(4);
                    break;
                case 'c':
                    shift(5);
                    break;
				case 'E':
					stack.push(7);
					state=7;
					
					break;
				case 'T':
					stack.push(8);
					state=8;
					
					break;
				case 'F':
					stack.push(9);
					state=9;
					
					break;
				case 'I':
					stack.push(11);
					state=11;
					
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED ID TOKEN OR \'(\' \n";
					SUC=-1;
			}
			break;
		case 7:
			switch(nextToken){
				case '+':
					shift(12);
					break;
				case '-':
					shift(13);
					break;
				case EOF:
					reduce(1);
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED \' + \'  OR \' - \' \n";
					SUC=-1;
			}
			break;
		case 8:
			switch(nextToken){
				case '+':
				case '-':
				case ')':
				case EOF:
					reduce(4);
					break;
				case '*':
					shift(14);
					break;
				case '/':
					shift(15);
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED OPERATOR TOKEN OR \' ) \' OR EOF\n";
					SUC=-1;
			}
			break;
		case 9:
			switch(nextToken){
				case '+':
				case '-':
				case ')':
				case EOF:
				case '*':
				case '/':
					reduce(7);
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED OPERATOR TOKEN OR \' ) \' OR EOF\n";
					SUC=-1;
			}
			break;
		case 10:
			switch(nextToken){
				case '(':
					shift(10);
					break;
                case 'a':
                    shift(3);
                    break;
                case 'b':
                    shift(4);
                    break;
                case 'c':
                    shift(5);
                    break;
				case 'E':
					stack.push(16);
					state=16;
					
					break;
				case 'T':
					stack.push(8);
					state=8;
					
					break;
				case 'F':
					stack.push(9);
					state=9;
					
					break;
				case 'I':
					stack.push(11);
					state=11;
					
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED ID TOKEN OR \' ( \' \n";
					SUC=-1;
			}
			break;
		case 11:
			switch(nextToken){
				case '+':
				case '-':
				case ')':
				case EOF:
				case '*':
				case '/':
					reduce(9);
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED OPERATOR TOKEN OR \' ) \' OR EOF\n";
					SUC=-1;
			}
			break;
		case 12:
			switch(nextToken){
				case '(':
					shift(10);
					break;
                case 'a':
                    shift(3);
                    break;
                case 'b':
                    shift(4);
                    break;
                case 'c':
                    shift(5);
                    break;
				case 'T':
					stack.push(17);
					state=17;
					
					break;
				case 'F':
					stack.push(9);
					state=9;
					break;
				case 'I':
					stack.push(11);
					state=11;
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED ID TOKEN OR \'( \' \n";
					SUC=-1;
			}
			break;			
		case 13:
			switch(nextToken){
				case '(':
					shift(10);
					break;
                case 'a':
                    shift(3);
                    break;
                case 'b':
                    shift(4);
                    break;
                case 'c':
                    shift(5);
                    break;
				case 'T':
					stack.push(18);
					state=18;
					break;
				case 'F':
					stack.push(9);
					state=9;
					break;
				case 'I':
					stack.push(11);
					state=11;
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED ID TOKEN OR \'( \' \n";
					SUC=-1;
			}
			break;
		case 14:
			switch(nextToken){
				case '(':
					shift(10);
					break;
                case 'a':
                    shift(3);
                    break;
                case 'b':
                    shift(4);
                    break;
                case 'c':
                    shift(5);
                    break;
				case 'F':
					stack.push(19);
					state=19;
					break;
				case 'I':
					stack.push(11);
					state=11;
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED ID TOKEN OR \'( \' \n";
					SUC=-1;
			}
			break;
		case 15:
			switch(nextToken){
				case '(':
					shift(10);
					break;
                case 'a':
                    shift(3);
                    break;
                case 'b':
                    shift(4);
                    break;
                case 'c':
                    shift(5);
                    break;
				case 'F':
					stack.push(20);
					state=20;
					break;
				case 'I':
					stack.push(11);
					state=11;
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED ID TOKEN OR \'( \' \n";
					SUC=-1;
			}
			break;
		case 16:
			switch(nextToken){
				case '+':
					shift(12);
					break;
				case '-':
					shift(13);
					break;
				case ')':
					shift(21);
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED \'+ \' , \'- \' OR \' ) \' \n";
					SUC=-1;
			}
			break;
		case 17:
			switch(nextToken){
				case '+':
				case '-':
				case ')':
				case EOF:
					reduce(2);
					break;
				case '*':
					shift(14);
					break;
				case '/':
					shift(15);
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED OPERATOR TOKEN OR \') \' OR EOF\n";
					SUC=-1;
			}
			break;
		case 18:
			switch(nextToken){
				case '+':
				case '-':
				case ')':
				case EOF:
					reduce(3);
					break;
				case '*':
					shift(14);
					break;
				case '/':
					shift(15);
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED OPERATOR TOKEN OR \') \' OR EOF\n";
					SUC=-1;
			}
			break;
		case 19:
			switch(nextToken){
				case '+':
				case '-':
				case ')':
				case EOF:
				case '*':
				case '/':
					reduce(5);
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED OPERATOR TOKEN OR \') \' OR EOF\n";
					SUC=-1;
			}
			break;
		case 20:
				switch(nextToken){
				case '+':
				case '-':
				case ')':
				case EOF:
				case '*':
				case '/':
					reduce(6);
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED OPERATOR TOKEN OR \') \' OR EOF\n";
					SUC=-1;
			}
			break;
		case 21:
			switch(nextToken){
				case '+':
				case '-':
				case ')':
				case EOF:
				case '*':
				case '/':
					reduce(8);
					break;
				default:
                    std::cout<<"\nSYNTAX ERROR: EXPECTED OPERATOR TOKEN OR \' ) \' OR EOF\n";
					SUC=-1;
			}
			break;
	}                                
}

void print(std::stack<int> &s)
{
    if(s.empty())
    {
        std::cout << std::endl;
        return;
    }
    int x= s.top();
    s.pop();
    print(s);
    s.push(x);
    if (x<=21){
        std::cout << x<<" ";
    }
    
    else{
        if (char (x) =='I'){
            std::cout<<"id"<<" ";
        }
        else {
            std::cout<<char(x)<<" ";
        }
    }
        
    
}
void print(std::queue<char> &q,int n){
    if(!n)
    {
        std::cout << std::endl;
        return;
    }
    char x= q.front();
    q.pop();
    std::cout << x<<" ";
    q.push(x);
    print(q,--n);
}
void getWSpace(){
    while (isspace(nextToken)){
        file.ignore();
        nextToken=file.peek();
    }
}
