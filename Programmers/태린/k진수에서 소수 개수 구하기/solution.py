import math

def solution(n, k):
    answer = 0

    def convert(num, base):
        a,b = divmod(num, base)
        if a == 0:
            return b
        else:
            c = convert(a,base)
            return str(c)+str(b)
    
    def isPrime(num):
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True
    
    num_arr = str(convert(n,k)).split('0')
    for i in num_arr:
        if i != '1' and i != '':
            if isPrime(int(i)):
                answer += 1

    return answer

print(solution(110011,10))