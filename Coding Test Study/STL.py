## 내장 함수 ##
## 1. itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리
## 순열과 조합 라이브러리를 제공함

## 2. heapq : 힙기능을 제공. 우선순위 큐 기능을 제공한다. 다익스트라알고리즘에 사용

## 3. bisect : 이진 탐색 기능을 제공

## 4. collections : deque, counter 등 자료구조를 포함

## 5. math : 수학적 기능을 제공 

# 1. itertools : 반복되는 데이터를 처리하는 기능을 포함. 코테에셔 permutations, combinateions 을 유용하게 쓸수 있음.
# permutations : 리스트와 같은 iterable 객체에서 r 개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산해줌.
# permutations 은 클래스 이므로 객체 초기화 이후에는 리스트 자료형으로변환하여 사용 가능.
# 중복 허용 하지 않음
#ex)

from itertools import permutations
data = ['A','B','C']
result = list(permutations(data,3)) 
print(result)

[('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]


# 2. combinations : 리스트와 같은 iterable 객체에서 r 개의 데이터를 뽑아
# 순서를 고려하지 않고
# 나열하는 모든 경우(조합)를 계산한다. 
# 중복 허용 하지 않음

from itertools import combinations
data = ['A','B','C']
result = list(combinations(data, 2))
print(result)
[('A', 'B'), ('A', 'C'), ('B', 'C')]


# 3. product 는 r 개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산한다.
# 원소를 중복하여 뽑는다.
# 객체를 초기화 할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다.

from itertools import product
data = ['A','B','C']
result = list(product(data, repeat = 2))
print(result)

[('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]