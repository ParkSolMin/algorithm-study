import copy
keys = []

# slice와 zip을 이용해 회전
# e.g. [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # print(list(zip(*key[::-1])))  # *key[::-1] => [7, 8, 9] [4, 5, 6] [1, 2, 3]
                                    # zip => 튜플로 묶어주는 메소드 ~ [7, 4, 1]
    # print(list(zip(*key))[::-1])  # list(zip(*key)) => [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
                                    # zip => 튜플로 묶어주는 메소드 ~ [(3, 6, 9), (2, 5, 8), (1, 4, 7)]
def keySpin(key):
    global keys
    keys.append(list(map(list, zip(*key[::-1]))))

def keyHelp(key, lock):
    lenKey = len(key)
    lenLock = len(lock)   
    # 좌우
    for i in range(lenLock):
        lock[i] = [2]*(lenKey-1) + lock[i] + [2]*(lenKey-1)
    
    # 위 아래
    for _ in range(lenKey-1):
        lock.insert(0, [2]*((lenKey-1)*2 + lenLock))
    for _ in range(lenKey-1):
        lock.append([2]*((lenKey-1)*2 + lenLock))    

# 본격 잠금해제 시도
def unlock(startX, startY, _, key, lock):
    keySize = len(key)
    for i in range(keySize):
        for j in range(keySize):
            lock[startX + i][startY + j] += key[i][j]
    
    for x in _:
        for y in _:
            if lock[x][y] != 1: return False
    return True

def solution(key, lock):
    global keys
    keyHelp(key, lock)
    
    keys.append(key)
    for i in range(3):
        keySpin(keys[-1])

    lockArea = range(len(key)-1, len(lock)-(len(key)-1)) # 3 의 경우 index 2, 3, 4
    for k in keys:
        for x in range(len(lock) - len(key) + 1):
            for y in range(len(lock) - len(key) + 1):
                if unlock(x, y, lockArea, k, copy.deepcopy(lock)): return True
    
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]	
lock = [[1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 0, 1], [0, 1, 1, 1]]
print(solution(key, lock))