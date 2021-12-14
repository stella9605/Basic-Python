#python의 heap은 heapq 라이브러리를 제공한다.
#heapq는 다익스트라 최단 경로 알고리즘을 포함해 우선순위 큐 기능을 구현하고자 할 때 사용한다.
#최소힙(Min Heap) 은 원소에 힙을 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다.
#heapq.heappush(), heapq.heappop() 메서드를 사용한다.

import heapq

def heapsort(iterable):
    h = []
    result = []
        
    for value in iterable:
        heapq.heappush(h, value)

    for i in range(len(h)) :
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)