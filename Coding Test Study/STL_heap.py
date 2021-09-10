# heap 기능을 위해 heapq 라이브러리를 제공한다.
# 다익스트라 최단 경로 알고리즘을 포함.
# 우선순위 큐 기능을 구현하고자 할 때 사용.

# PriorityQueue 라이브러리 보단 heapq가 더 빠르게 동작하므로 heapq를 선호.

# 파이썬의 최소힙은 단순 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간복잡도 O(NlogN)에 오름차순 정렬이 완료된다.
# 보통 최소 힙 자료구조의 최상단 원소는 항상 "가장 작은 원소" 이기 때문.

# 힙에 원소를 삽입 할 때 : heapq.heappush()
# 힙에 원소를 꺼낼 때    : heapq.heappop()

import heapq
def heapsort(iterable) :
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable :
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼낼 때
    for i in range(len(h)) :
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8])
print(result)

[1, 2, 3, 4, 5, 6, 7, 8, 9]


# 파이썬의 힙은 최대힙을 구하는 라이브러리를 제공하지 않는다. 
# 따라서 heapq 라이브러리를 이용하여 원소의 부호를 임시로 변경하는 방식을 사용한다. 
# 1. 힙에 원소를 삽입하기 전에 잠시 부호를 반대로 바꿈
# 2. 힙에서 원소를 꺼낸 뒤 다시 원소의 부호를 바꿈.

import heapq 

def heapsort_2(iterable) :
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입 
    for value in iterable :
        heapq.heappush(h, -value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내기 
    for value in range(len(h)) :
        result.append(-heapq.heappop(h))
    return result 

result = heapsort_2([1,3,5,7,9,2,4,6,8])
print(result)

[9, 8, 7, 6, 5, 4, 3, 2, 1]