word_map = { "plus": "+", "minus": "-", "mltp": "*", "div": "/",  
            "mod": "%", "fdiv": "//", "iseq": "==", "noteq": "!=", 
            "gt": ">", "lt": "<", "gteq": ">=", "lteq": "<=",
            "par": "(", "epar": ")", "sqr": "[", "esqr": "]",
            "dct": "{", "edct": "}", "com": "," ,"then": ":",
            "hash": "#",}
 
transpiled_lines = []
with open("test.ipy", "r") as file:
    for line in file:
        transpiled_line=[]
        for word in line.split(" "):
            if word in word_map:
                transpiled_line.append(word_map[word])
            else:
                transpiled_line.append(word)
                
        transpiled_lines.append(" ".join(transpiled_line))

with open("test.py", "w") as file:
    for line in transpiled_lines:
        file.write(line)

      
