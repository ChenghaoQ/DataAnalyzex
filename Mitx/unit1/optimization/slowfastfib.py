
def slowfib(n):
        if n == 0 or n == 1:
                return 1
        else:
                return slowfib(n-1) + slowfib(n-2)



def fastfib(n,memo = {}):
        if n == 0 or n == 1:
                return 1
        try:
                return memo[n]
        except KeyError:
                result = fastfib(n-1,memo) + fastfib(n-2,memo)
                memo[n]= result
                return result


for i in range(12111):

        print('fib['+ str(i) +']=',fastfib(i))
