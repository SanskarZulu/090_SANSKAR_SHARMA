//Assignment 3: Knowledge-based Expert system
//FLOYD: An AI program
//Submitted by: Sanskar Sharma
//PRN: 0120180381
//Roll number: 090
// Program Name: Floyd Chatterbox
// This a expert system, which have a set of responses for every question
//out of which a random answer will be selected for a question asked by the user!
//



#include <iostream>
#include <string>
#include <vector>
#include <ctime>
#include <cstdlib>

const int MAX_RESP = 3;//3 possible responses for each question asked!

typedef std::vector<std::string> vstring;

vstring find_match(std::string input);
void copy(char *array[], vstring &v);


typedef struct {
    char *input;
    char *responses[MAX_RESP];
}record;

//Database or knowledge base for the expert system!

record KnowledgeBase[] = {
    {"WHAT IS YOUR NAME",
    {"MY NAME IS FLOYD.",
     "YOU CAN CALL ME FLOYD.",
     "WHY DO YOU WANT TO KNOW MY NAME?"}
    },
    
    {"HI", 
    {"HI THERE!",
     "HI, HOW ARE YOU?",
     "HOLA!"}
    },
    {"HEY", 
    {"HI THERE!",
     "HI, HOW ARE YOU?",
     "HOLA!"}
    },
    
    {"HOW ARE YOU",
    {"I'M DOING FINE!",
    "I'M DOING WELL AND YOU?",
	"PRETTY MUCH FINE, WBU?"}
    },

    {"WHO ARE YOU",
    {"I'M AN ARTIFICIAL INTELLIGENCE PROGRAM.",
     "I THINK THAT YOU KNOW WHO I'M.",
	 "I AM A BABY NOW, WHO WILL BECOME YOUR FUTURE!"}
    },

    {"ARE YOU INTELLIGENT",
    {"YES,OFCORSE.",
     "ACTUALY,I'M VERY INTELLIGENT!",
	 "TAKE A GUESS ;)"}
    },
    
    {"CAN WE BECOME FRIENDS",
    {"YES,OFCORSE.",
     "AREN'T WE ALREADY?'",
	 "WHY NOT, JUST REMEMNER LAST SLICE OF PIZZA IS ALWAYS FLOYD'S ;)'"}
    },

    {"ARE YOU REAL",
    {"DOES THAT QUESTION REALLY MATERS TO YOU?",
     "I'M AS REAL AS I CAN BE.",
	 "WHAT IF, I'M NOT?"}
    }
};

size_t nKnowledgeBaseSize = sizeof(KnowledgeBase)/sizeof(KnowledgeBase[0]);

int main() {
	
    srand((unsigned) time(NULL));
    std::string sInput = "";
    std::string sResponse = "";
    //std::cout << "HOW CAN I HELP YOU "<<name << std::endl;
    while(1) {
        std::cout << ">";
        std::getline(std::cin, sInput);//cin>>sInput;//
        vstring responses = find_match(sInput);
        if(sInput == "BYE"||sInput == "SEE YOU" || sInput == "TTYL") {
            std::cout << "FLOYD: IT WAS NICE TALKING TO YOU USER, SEE YOU NEXTTIME!" << std::endl;  
            break;
        } 
        else if(responses.size() == 0)  {
            std::cout << "FLOYD: I'M NOT SURE IF I UNDERSTAND WHAT YOU  ARE TALKING ABOUT." 
                      << std::endl;
        }
        else {
            int nSelection = rand()  % MAX_RESP;
            sResponse =   responses[nSelection]; 
			std::cout <<"FLOYD: "<< sResponse << std::endl; 
        } 
    } 

    return 0;
}
    
// make a  search for the  user's input 
// inside the database of the program 
vstring find_match(std::string  input) { 
    vstring result;
    for(int i = 0; i < nKnowledgeBaseSize;  ++i) {  
        if(std::string(KnowledgeBase[i].input) == input) { 
            copy(KnowledgeBase[i].responses, result); 
            return result;
        } 
    } 
    return result; 
}

void copy(char  *array[], vstring &v) { 
    for(int i = 0;  i < MAX_RESP; ++i) {
        v.push_back(array[i]);
    }
}

/*
OUTPUT:
(Note: Floyd is an ongoing AI program. He may ask silly 
questions and may not respond properly.)
A conversation following the database rules, facts.

>HI
FLOYD: HOLA!
>HI
FLOYD: HI, HOW ARE YOU?
>WHAT IS YOUR NAME
FLOYD: WHY DO YOU WANT TO KNOW MY NAME?
>WHAT IS YOUR NAME
FLOYD: YOU CAN CALL ME FLOYD.
>LET'S RESTART
FLOYD: I'M NOT SURE IF I UNDERSTAND WHAT YOU  ARE TALKING ABOUT.
>HEY
FLOYD: HI, HOW ARE YOU?
>WHO ARE YOU
FLOYD: I AM A BABY NOW, WHO WILL BECOME YOUR FUTURE!
>WHO ARE YOU
FLOYD: I'M AN ARTIFICIAL INTELLIGENCE PROGRAM.
>ARE YOU INTELLIGENT
FLOYD: TAKE A GUESS ;)
>ARE YOU INTELLIGENT
FLOYD: YES,OFCORSE.
>ARE YOU INTELLIGENT
FLOYD: ACTUALY,I'M VERY INTELLIGENT!
>ARE YOU REAL
FLOYD: I'M AS REAL AS I CAN BE.
>CAN WE BECOME FRIENDS
FLOYD: AREN'T WE ALREADY?'
>CAN WE BECOME FRIENDS
FLOYD: YES,OFCORSE.
>CAN WE BECOME FRIENDS
FLOYD: WHY NOT, JUST REMEMNER LAST SLICE OF PIZZA IS ALWAYS FLOYD'S ;)'
>SEE YOU
FLOYD: IT WAS NICE TALKING TO YOU USER, SEE YOU NEXTTIME!

--------------------------------
Process exited after 136.9 seconds with return value 0
Press any key to continue . . .
He is a 
*/
