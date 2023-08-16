
def countSetBits(n):
    count =0
    while n:
        count += n & 1
        n >>= 1
    return count
 
def countOfOddPascal(n):
    c = countSetBits(n)
    return pow(2, c)

n= int(input())
print(countOfOddPascal(n))


