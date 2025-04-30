Going to turn this into a transpiled language specifically to code on an iphone keyboard without any special characters. 

for now its going to be extremely simple by doing a replace on the below mappings. the mappings will require to be wrappe with spaces. eg ' plus ' will turn into ' + '. if the spaces arent there it wont map. 

Operators: 
    plus +, 
    minus -, 
    mltp *, 
    div /, 
    mod %, 
    N/A **, 
    fdic //, 
    iseq ==, 
    noteq !=, 
    gt >, 
    lt <, 
    gteq >=, 
    lteq <=, 
    N/A &, 
    N/A |, 
    N/A ^, 
    N/A ~, 
    N/A <<, 
    N/A >>

Delimiters: 
    par epar ( ),
    sqr esqr [ ],
    dct edct { },
    com , ,
    then :,
    N/A ;,

Assignment:
    eq =,
    qt ",
    N/A /,
    N/A \,

Decorators: 
    N/A @,
    N/A _

Comments: 
    hash #