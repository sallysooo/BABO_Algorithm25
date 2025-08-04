from collection import defaultdict
# defaultdict 클래스는 키가 없을 때 기본 값을 defaultdict 형태([])로 기본값을 저장함 

def solution(graph, start):
	# 1. 그래프를 인접 리스트로 변환
    adj_list = defaultdict(list) # []로 초기화
    for u, v in graph:
    	adj_list[u].append(v)
    
    # 2. DFS 탐색 함수
    def dfs(node, visited, result):
    	visited.add(node)                       # 3. 현재 노드를 방문한 노드들의 집합에 추가
        result.append(node)                     # 4. 현재 노드를 결과 리스트에 추가
        for neighbor in adj_list.get(node, []): # 5. 현재 노드와 인접한 노드 순회
        	if neighbor not in visited:         # 6. 아직 방문하지 않은 노드라면 
            	dfs(neighbor, visited, result)
    
    # DFS를 순회한 결과를 반환 
    visited = set()
    result = []
    dfs(start, visited, result) # 7. 시작 노드에서 DFS 시작
    return result               # 8. DFS 탐색 결과 반환
