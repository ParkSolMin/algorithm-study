def check(answer):
    for x, y, option in answer:
        if option == 0: 
            if y == 0 or [x, y-1, 0] in answer or [x, y, 1] in answer or [x-1, y, 1] in answer:
                continue
            else:
                return False
        else: 
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True
        
def solution(n, build_frame):
    answer = []
        
    for order in build_frame:
        if order[-1] == 1: 
            answer.append([*order[:-1]])
            if not check(answer): answer.remove([*order[:-1]])
        else: 
            answer.remove([*order[:-1]])
            if not check(answer): answer.append([*order[:-1]])
    
    answer.sort()
    return answer

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))