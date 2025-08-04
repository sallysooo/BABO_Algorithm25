from collections import defaultdict, deque

def solution(graph, start):
	# 그래프를 인접 리스트로 변환
    adj_list = defaultdict(list)
    for u, v in graph:
    	adj_list[u].append(v)
    
    # BFS 탐색 함수
    def bfs(start):
    	visited = set()     # 1. 방문한 노드를 저장할 set
    
    	# 2. 탐색 시 맨 처음 방문할 노드를 push하고 방문 처리
        queue = deque([start])
        visited.add(start)
        result.append(start)
        
        # 3. 큐가 비어 있지 않은 동안 반복 
        while queue:
        	node = queue.popleft()                 # 4. 큐에 있는 원소 중 가장 먼저 푸시된 원소 pop
            for neighbor in adj_list.get(node, []) # 5. 인접한 이웃 노드들에 대해서
            	if neighbor not in visited:        # 6. 방문되지 않은 인접한 노드인 경우,
                	# 7. 인접한 노드를 방문 처리
                	queue.append(neighbor)
                    visited.append(neighbor)
                    result.append(neighbor)
    
    result = []
    bfs(start)    # 8. 시작 노드부터 BFS 탐색 수행
    return result
