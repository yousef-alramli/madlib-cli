import re

def read_template(path):
    try:
        with open(path) as f:
            x=f.read()
    except FileNotFoundError:
        x = "sorry the file do not exist"
    
    return x


def parse_template(line):
    
    stripped = re.sub(r"{(\w+\s*)+}",'{}',line)
    parsed = tuple(re.findall(r"{(\w+\s*)+}",line))
    return stripped,parsed

def merge(stripped,newparse):
    merged = stripped.format(*newparse)
    return merged

def looping_inputs(parses):
    answers = []
    for i in parses:
        if i == 'Verb':
            answers.append(input(i + "(ing) "))
        else:
            answers.append(input(i + " ")) 
    
    return tuple(answers)


        

if __name__ == "__main__":
    stripped = parse_template(read_template("madlib_cli/assets/madlib_game.txt"))[0]
    parsed = parse_template(read_template("madlib_cli/assets/madlib_game.txt"))[1]
    inputs = looping_inputs(parsed)
    print(merge(stripped,inputs))
    
