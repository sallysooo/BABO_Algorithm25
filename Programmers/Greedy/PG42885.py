'''
people : [70, 50, 80, 50]

limit : 100kg
구명보트를 최대한 적게 사용 = 최대한 많은 사람들을 한 보트에 싣는 문제

1. 사람 몸무게 배열을 오름차순 정렬
2. 가장 무거운 사람을 우선 태운다고 하면 그리디 방법으로 가장 무거운 사람은 가장 가벼운 사람과 짝을 지어서 무게가 낭비되는 걸 최소화하는 전략
'''

def solution(people, limit):
    boat = 0
    people.sort()       # 오름차순 : [50, 50, 70, 80]
    i = 0               # 가장 가벼운 사람의 인덱스
    j = len(people) - 1 # 가장 무거운 사람의 인덱스
    
    while i <= j:
        sum = people[i] + people[j]
        if limit >= sum:
            i += 1
        j -= 1
        boat += 1

    return boat