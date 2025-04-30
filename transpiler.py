import argparse

def transpile(file):
    word_map = { "plus": "+", "minus": "-", "mltp": "*", "div": "/",  
            "mod": "%", "fdiv": "//", "iseq": "==", "noteq": "!=", 
            "gt": ">", "lt": "<", "gteq": ">=", "lteq": "<=",
            "par": "(", "epar": ")", "sqr": "[", "esqr": "]",
            "dct": "{", "edct": "}", "com": "," ,"then": ":",
            "hash": "#", "eq": "="}
    new_name = file.replace("ipy", "py")
    transpiled_lines = []

    
    with open(file, "r") as file:
        for line in file:
            transpiled_line=[]
            for word in line.split(" "):
                if word in word_map:
                    transpiled_line.append(word_map[word])
                else:
                    transpiled_line.append(word)
                
            transpiled_lines.append(" ".join(transpiled_line))

    with open(new_name, "w") as file:
        for line in transpiled_lines:
            file.write(line)

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="Transpiler for the Ithon language. Ithon is meant as a no special character language for use within mobile environments or where ever the keyboard is limited.")

    # Add arguments
    parser.add_argument("--file", help="Ithon file ending in .ipy to convert to python", 
                        required=True, type=str)

    # Parse arguments
    args = parser.parse_args()

    # Access arguments
    file=args.file
    print(file)

    transpile(file)
