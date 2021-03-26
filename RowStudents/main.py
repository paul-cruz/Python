import sys


def solution(A):
    flag = False
    helper = []
    rows = 0
    for i in A:
        if helper:
            for j in helper:
                if j > i:
                    flag = True
            if not flag:
                helper.append(i)
                rows += 1
            flag = False
        else:
            helper.append(i)
            rows = 1
    return rows


def main():
    """Read from stdin, solve the problem, write answer to stdout."""
    input = sys.stdin.readline().split()
    A = [int(x) for x in input[0].split(",")]
    sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
    main()
