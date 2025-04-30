with open("filename", "r") as file:
    for line in file:
        
        transpiled_line=[]
        for word in line.split(" "):
            if word in word_map:
                transpiled_line.append(word_map[word])
            else:
                transpiled_line.append(word)
                
        print(" ".join(transpiled_line))
        