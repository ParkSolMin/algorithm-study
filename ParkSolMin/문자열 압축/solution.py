min = 1001

def compress(s, length):
    global min
    temp = 0
    count = 1
    i = 0
    char = s[:length]

    if(min < length): return 1001

    for i in range(length, len(s), length):
        c = s[i:i+length]

        if char == c:
            count += 1
        else:
            temp += len(str(count)+char) if count > 1 else len(char)
            
            char = s[i:i+length]
            count = 1

    return temp+len(str(count)+char) if count > 1 else temp+len(char)

def solution(s):
    global min
    if len(s) == 1: min = 1
    
    for i in range(1, len(s)):
        length = compress(s, i)
        if min > length:
            min = length
    return min


print(solution('a'))
