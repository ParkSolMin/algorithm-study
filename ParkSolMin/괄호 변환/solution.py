def valid(w):
    stack = []
    for i in w:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                return False
            stack.pop()
    return True


def detach(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1

        if count == 0:
            return s[:i+1], s[i+1:]


def solution(p):
    if not p:
        return ''

    u, v = detach(p)
    if valid(u):
        return u+solution(v)
    else:
        temp = '('
        temp += solution(v)
        temp += ')'

        for char in u[1:-1]:
            temp += '(' if char == ')' else ')'

        return temp


print(solution('(()())()'))
