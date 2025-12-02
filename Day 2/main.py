from itertools import batched
def invalidate(id):
    n = 2
    batch_size = len(id)//n
    while batch_size > 0:
        if len(set(batched(id, batch_size))) == 1:
            return True
        n+=1
        batch_size = len(id)//n
    return False

def main():
    answer = 0
    with open("input.txt") as fin:
        ranges = fin.readline().strip().split(",")
        for r in ranges:
            rmin, rmax = r.split("-")
            for i in range(int(rmin), int(rmax)+1):
                if invalidate(str(i)):
                    answer += i

    print(answer)

main()