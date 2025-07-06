def mortal_fib(n, m):
    dp =[0]*(n+1)
    dp[0]=1
    dp[1]=1
    for i in range(2, n+1):
        if i-m<0:
            dp[i] = dp[i-1]+dp[i-2]
        elif i==m or i==m+1:
            dp[i] = dp[i-1] + dp[i-2] - 1
        else:
            dp[i] = dp[i-1]+dp[i-2]-dp[i-m-1]
    return dp[n-1]
print(mortal_fib(95,20))