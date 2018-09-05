import fileinput


if __name__ == '__main__':
    lines = []
    for line in fileinput.input():
        lines.append(line)
        
    res =lines[0]+lines[1]
    print(res)