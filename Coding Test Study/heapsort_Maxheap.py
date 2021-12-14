#Maxheap은 파이썬에서 제공되지 최대힙 구현시 원소의 부호를 임시로 변경했다 사용한다.
# 힙에 원소를 삽입하기 전 잠시부호를 바꿨다가 꺼낼시 부호 다시 바꾸는 방법 이용

import heapq

def heapsort(iterable):
    h = []
    result = []

    # 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)