'''
부분 배낭 문제
1. 짐 별로 무게당 가치를 구한다.
2. 무게당 가치가 높은 짐부터 넣을 수 있는 만큼 배낭에 넣는다.
2-1. 배낭 용량 > 짐무게 인 경우 짐을 쪼개서 넣는다.
3. 과정 2를 배낭이 허용하는 용량이 0이 될때까지 수행한다.
'''

def calculate_value(items):
    for item in items:
        item.append(item[1] / item[0])
    return items

def sort_value(items):
    items.sort(key=lambda x : x[2], reverse=True)
    return items


def solution(items, weight_limit):  # [[10, 19], [7, 10], [6, 10]]
    items = calculate_value(items)  # [[10, 19, 1.9], [7, 10, 1.4], [6, 10, 1.6]]
    items = sort_value(items)       # [[10, 19, 1.9], [6, 10, 1.6], [7, 10, 1.4]]

    total_value = 0
    
    for item in items:
        weight = item[0]
        value = item[1]
        if weight_limit >= weight:
            total_value += value
            weight_limit -= weight
        else:
            fraction = weight_limit / weight
            total_value += value * fraction
            break
    return total_value