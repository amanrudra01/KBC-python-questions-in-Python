questions=[['Who developed Python Programming Language?',
            'a) Wick van Rossum','b) Rasmus Lerdorf','c) Guido van Rossum','d) Niene Stom','c',
            'Explanation: Python language is designed by a Dutch programmer Guido van Rossum in the Netherlands.'
            ],

            ['Which type of Programming does Python support?',
            'a) object-oriented programming',
            'b) structured programming',
            'c) functional programming',
            'd) all of the mentioned',
            'd',
            'Explanation: Python is an interpreted programming language, which supports object-oriented, structured, and functional programming.'
            ],

            ['Is Python case sensitive when dealing with identifiers?',
            'a) no',
            'b) yes',
            'c) machine dependent',
            'd) none of the mentioned',
            'b',
            'Explanation: Case is always significant while dealing with identifiers in python.'
            ],
            
            ['Which of the following is the correct extension of the Python file?',
            'a) .python',
            'b) .pl',
            'c) .py',
            'd) .p',
            'c',
            'Explanation: ‘.py’ is the correct extension of the Python file. Python programs can be written in any text editor. To save these programs we need to save in files with file extension ‘.py’.'
            ],

            ['Is Python code compiled or interpreted?',
            'a) Python code is both compiled and interpreted',
            'b) Python code is neither compiled nor interpreted',
            'c) Python code is only compiled',
            'd) Python code is only interpreted',
            'a',
            'Explanation: Many languages have been implemented using both compilers and interpreters, including C, Pascal, and Python.'
            ],

            ['All keywords in Python are in ______.',
            'a) Capitalized',
            'b) lower case',
            'c) UPPER CASE',
            'd) None of the mentioned',
            'd',
            'Explanation: True, False and None are capitalized while the others are in lower case.',
            ],

            [['What will be the value of the following Python expression?',  '4 + 3 % 5'],
            'a) 7',
            'b) 2',
            'c) 4',
            'd) 1',
            'a',
            'Explanation: The order of precedence is: %, +. Hence the expression above, on simplification results in 4 + 3 = 7. Hence the result is 7.'
            ],

            ['Which of the following is used to define a block of code in Python language?',
            'a) Indentation',
            'b) Key',
            'c) Brackets',
            'd) All of the mentioned',
            'a',
            'Explanation: In Python, to define a block of code we use indentation. Indentation refers to whitespaces at the beginning of the line.'
            ],

            ['Which keyword is used for function in Python language?',
            'a) Function',
            'b) def',
            'c) Fun',
            'd) Define',
            'b',
            'Explanation: The def keyword is used to create, (or define) a function in python.'
            ],

            ['Which of the following character is used to give single-line comments in Python?',
            'a) //',
            'b) #',
            'c) !',
            'd) /*',
            'b',
            'Explanation: To write single-line comments in Python use the Hash character (#) at the beginning of the line. It is also called number sign or pound sign. To write multi-line comments, close the text between triple quotes. Example: “”” comment text “””.'
            ],

            [['What will be the output of the following Python code?',
                'i = 1',
                'while True:',
                '    if i%3 == 0:',
                '        break',
                '    print(i)',
                '    i + = 1'],
            'a) 1 2 3',
            'b) error',
            'c) 1 2',
            'd) none of the mentioned',
            'b',
            'Explanation: SyntaxError, there shouldn’t be a space between + and = in +=.'
            ],

            ['Which of the following functions can help us to find the version of python that we are currently working on?',
            'a) sys.version(1)',
            'b) sys.version(0)',
            'c) sys.version()',
            'd) sys.version',
            'd',
            'Explanation: The function sys.version can help us to find the version of python that we are currently working on. It also contains information on the build number and compiler used. For example, 3.5.2, 2.7.3 etc. this function also returns the current date, time, bits etc along with the version.'
            ],

            ['Python supports the creation of anonymous functions at runtime, using a construct called ______',
            'a) pi',
            'b) anonymous',
            'c) lambda',
            'd) none of the mentioned',
            'c',
            'Explanation: Python supports the creation of anonymous functions (i.e. functions that are not bound to a name) at runtime, using a construct called lambda. Lambda functions are restricted to a single expression. They can be used wherever normal functions can be used.'
            ],

            ['What is the order of precedence in python?',
            'a) Exponential, Parentheses, Multiplication, Division, Addition, Subtraction',
            'b) Exponential, Parentheses, Division, Multiplication, Addition, Subtraction',
            'c) Parentheses, Exponential, Multiplication, Division, Subtraction, Addition',
            'd) Parentheses, Exponential, Multiplication, Division, Addition, Subtraction',
            'd',
            'Explanation: For order of precedence, just remember this PEMDAS (similar to BODMAS).'
            ],

            ['What will be the output of the following Python code snippet if x=1?:   x<<2',
            'a) 4',
            'b) 2',
            'c) 1',
            'd) 8',
            'a',
            'Explanation: The binary form of 1 is 0001. The expression x<<2 implies we are performing bitwise left shift on x. This shift yields the value: 0100, which is the binary form of the number 4.'
            ],

            ['What does pip stand for python?',
            'a) Pip Installs Python',
            'b) Pip Installs Packages',
            'c) Preferred Installer Program',
            'd) All of the mentioned',
            'c',
            'Explanation: pip is a package manager for python. Which is also called Preferred Installer Program.'
            ],

            ['Which of the following is true for variable names in Python?',
            'a) underscore and ampersand are the only two special characters allowed',
            'b) unlimited length',
            'c) all private members must have leading and trailing underscores',
            'd) none of the mentioned',
            'b',
            'Explanation: Variable names can be of any length.'
            ]
        ]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,75000000]
money=0
for i in range(0,len(questions)):
    print(f"Question for Rs.{levels[i]}\n{i+1}. {questions[i][0]}\n")
    print(f"{questions[i][1]}       {questions[i][2]}\n")
    print(f"{questions[i][3]}       {questions[i][4]}")
    ans=input("\nEnter your answer:")
    if(ans==questions[i][-2]):
        print(f"Jioo! Correct Answer,\n{questions[i][6]}\nYou have won Rs.{levels[i]}\n\n\n")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    elif(ans!='a' and ans!='b' and ans!='c' and ans!='d'):
        print("Invalid Answer you Moron, This option is not even exist")
        break
    else:
        print("Wrong Answer Fool!")
        break
print(f"Now overall money you won: Rs.{money}")
if(money!=0):
    print("BUT intersting part is that you never get this money :)")
