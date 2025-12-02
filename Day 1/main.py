def rotates(rotation, deg):
    answer = 0
    for _ in range(abs(deg)):
        if deg < 0:
            rotation -= 1
        elif deg > 0:
            rotation += 1

        if rotation == -1:
            rotation = 99
        
        if rotation == 100:
            rotation = 0
        
        if rotation == 0:
            answer += 1
    
    return rotation, answer


def main():
    answer = 0
    rotation = 50

    with open("input.txt") as fin:
        line = fin.readline().strip()
        while line != "":
            before = rotation
            if line[0] == "L":
                rotation, a = rotates(before, -1*int(line[1:]))
            elif line[0] == "R":
                rotation, a = rotates(before, int(line[1:]))
            answer += a
            line = fin.readline().strip()
    print(answer)

main()