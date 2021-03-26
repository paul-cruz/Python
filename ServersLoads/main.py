import sys


def solution(nums):
    s = sum(nums)//2
    n = len(nums)
    dp = [[0 for _ in range(s+1)] for x in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, s+1):
            if nums[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], nums[i-1]+dp[i-1][j-nums[i-1]])
            else:
                dp[i][j] = dp[i-1][j]
        print(dp)
    '''return second server loads - first server loads'''
    return (sum(nums)-dp[-1][-1])-dp[-1][-1] 

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()
