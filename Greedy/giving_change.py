def solution(amount):
    denom = [1, 10, 50, 100]
    denom.sort(reverse=True) # 1. 화폐 단위를 큰 순서대로 정렬 : [100, 50, 10, 1]
    
    change = [] # 2. 거스름돈을 담을 리스트
    
    for coin in denom:
        while amount >= coin:   # 3. 해당 화폐 단위로 거스름돈을 계속 나눠줌
            change.append(coin) # 4. 거스름돈 리스트 업데이트
            amount -= coin      # 5. 정산이 완료된 거스름돈 빼기
    
    return change # 6. 거스름돈 리스트 반환