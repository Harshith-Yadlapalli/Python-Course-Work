# # # SwAp CaSe 
# # Sample Input : HackerRank.com presents "Pythonist 2".
# Sample Output: hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# # String Validation
# Sample Input: qA2
# Sample Output
# True
# True
# True
# True
# True

if __name__ == '__main__':
    s = input()
    a = b = c = d = e = False
    for ch in s:
        if ch.isalnum():
            a = True
        if ch.isalpha():
            b = True
        if ch.isdigit():
            c = True
        if ch.islower():
            d = True
        if ch.isupper():
            e = True
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

 #Loops
# Sample Input: 5
# Sample Output:
# 0
# 1
# 4
# 9
# 16

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i*i)

# Sample Input : 1990
# Sample Output :False
def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 400==0 :
        return True
    elif year%100==0:
        return False
    elif year%4==0:
        return True
    else:
        return False
    return leap

year = int(input())
print(is_leap(year))

