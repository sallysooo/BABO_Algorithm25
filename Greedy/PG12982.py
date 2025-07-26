# 프로그래머스 12982 : 예산

def solution(d, budget):
    d.sort() # 1. 오름차순 정렬 : [1, 2, 3, 4, 5]
    result = 0 # 물품 지원 가능한 부서의 개수

    for cost in d:
        if budget >= cost: # 지원 가능한 경우
            result += 1
            budget -= cost
        else:
            break # 지원 금액 쪼개기는 불가능

    return result if budget >= 0 else result - 1