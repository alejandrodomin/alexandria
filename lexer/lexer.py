import re

def parse(line):
    """
    There needs to be an order in how these things are processed only a subset can start a line from there it should be
    a simple regex call to get things moving right?
    But that seems too complicated just get the tokens and assemble them in the order that they exist in
    """
    tokens=[]
    func_regex=r"(int|char)\s+([a-zA-Z]+)[(](.*)[)]\s+[{]((\n.*)*)[}]"

    found=re.search(func_regex, line)
    for i in range(1,5):
        print(found.group(i) + "\n")

test_str="""int sum(int a, int b) {
    c = a + b;
    return c;
}"""

parse(test_str)

