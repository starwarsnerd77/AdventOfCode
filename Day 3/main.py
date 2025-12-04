def get_max_joltage(line, n, joltage):
    if n == 0:
        return joltage
    digit = "0"
    subline = ""
    for i in range(len(line)-(n-1)):
        if int(line[i]) > int(digit):
            digit = line[i]
            subline = line[i+1:]
    return get_max_joltage(subline, n-1, joltage+digit)
            

def main():
    with open("input.txt") as fin:
        answer = 0
        line = fin.readline().strip()
        while line != "":
            joltage = get_max_joltage(line, 12, "")
            
            answer += int(joltage)

            line = fin.readline().strip()
        print(answer)

main()