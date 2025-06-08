# solution 1
def fib(n,k):
  if n==1 or n==2:
    return 1
  else:
    return fib(n-1,k)+k*fib(n-2,k)

print(fib(29,2))

# solution 2
dp = []
n,k=(5,3)
dp.append(1)
dp.append(1)
for i in range(2,n):
  dp.append(dp[len(dp)-1]+dp[len(dp)-2]*k)
print(dp[n-1])