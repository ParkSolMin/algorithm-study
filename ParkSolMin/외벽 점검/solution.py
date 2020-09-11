import itertools

def check(weak, friends):
    start = weak[0]
    count = 0
    for i in range(1, len(weak)):
        if friends[count] >= abs(start-weak[i]):
            continue
        else:
            count += 1
            start = weak[i]
            if count >= len(friends): return False
            
    return True

def solution(n, weak, dist):
    answer = 0
    dist.sort()
    dist.reverse()
    
    for count in range(1, len(dist)+1):
        if count == 1:
            friends = [[dist[0]]]
        else: 
            friends = list(map(list, itertools.permutations(dist[:count], count)))
        for i in range(len(weak)):
            for _ in friends:
                if check(weak[i:] + list(map(lambda i: i+n, weak[:i])), _):
                    return len(_)
    
    return -1

n = 12
weak = [0, 1, 3, 4, 9, 10]
dist = [1]
print(solution(n, weak, dist))