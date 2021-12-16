# 해싱을 데이터를 아주 빠르게 삽입 하거나 가져올 때 사용하는 기법이다.
# 전체 자료를 검색해야 하기 때문에 최대값, 최소값을 찾을 때는 효율이 떨어진다.
# 파이썬의 딕셔너리는 해시 테이블로 구현되어 있다. 

# 원리
# key 값을 넣고 hash function 에서 buckets에 저장된 값을 리턴받는다.
# 해시값을 주소로 바꿔 쓰는 것을 direct-address table 이라 한다

# 파이썬에서는...
# hash() 함수를 사용함. 단 프로그램 재시작 시 해시값이 달라짐. 해시값이 달라짐에 문제가 생기면 딕셔너리 사용하는게 편함...

print(hash('LIM')

# 암호학 적 해시 함수
import hashlib
h = hashlib.sha256()
h.update(b'LIM')
result = h.hexdigest()
print(result)

# 암호화에 응용하여 사용하기 좋은것 같음.
# 해시값에서 역으로 원본찾기가 어려움 "단방향성"