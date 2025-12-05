def accessible(grid, y, x):
    total = 0
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            try:
                if i < 0 or j < 0:
                    raise
                if grid[i][j] == "@":
                    total += 1
            except:
                continue
    total -= 1
    return total < 4 

def main():
    with open("input.txt") as fin:
        answer = 0
        complete = False
        grid = [[i for i in line.strip()] for line in fin.readlines()]
        new_grid = grid[::1]
        while not complete:
            round_answer = 0
            for y in range(len(grid)):
                for x in range(len(grid[y])):
                    if grid[y][x] == "@":
                        if accessible(grid, y, x):
                            round_answer += 1
                            new_grid[y][x] = "X"
            if round_answer == 0:
                complete = True
                break
            grid = new_grid[::1]
            answer += round_answer
        print(answer)

main()