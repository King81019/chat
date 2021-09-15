def read_file(input_filename):
    lines = []
    with open(input_filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

"""
#我原本的寫法
def typeset(lines):
    chat =[]
    for line in lines:
        if 'Allen' in line:
            name = 'Allen'
        elif 'Tom' in line:
            name = 'Tom'
        elif name == 'Allen':
            dialog = line
            chat.append([name, dialog])
        elif name == 'Tom':
            dialog = line
            chat.append([name, dialog])
    print(chat)
    return chat

def write_file(output_filename, chat):
    with open(output_filename, 'w', encoding = 'utf-8-sig') as f:
        for line in chat:
            f.write(line[0] + ':' + line[1] + '\n')
"""

#使用continue的寫法
def typeset(lines):
    chat =[]
    name = None
    for line in lines: 
        if line == 'Allen':
            name = 'Allen'
            continue
        elif line == 'Tom':
            name = 'Tom'
            continue    
        if name:
            chat.append(name + ': ' + line) 
        else:
            chat.append('unknown' + ': ' + line) 
    return chat

def write_file(output_filename, lines):
    with open(output_filename, 'w', encoding = 'utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')
     
def main():
    lines = read_file('input.txt')
    lines = typeset(lines)
    write_file('output.txt', lines)

main()


