# 함수 만들기
def hello():
    print("hello world!")  # 느낌표는 문자열 안에 위치

# 함수 호출(실행)
hello()

def hello_name(name):
    print(f"안녕 {name}야~")  # name 앞에 공백 추가하면 보기 좋아요

# 함수 호출(실행)
name = input("이름을 입력: ")
hello_name(name)

# 연산을 하는 함수
def cal(n1, n2, op):  # 1, 2, + (이렇게 입력)
    r = 0  # 결과값
    if op == "+":
        r = n1 + n2
    elif op == "-":  # 들여쓰기 수정
        r = n1 - n2
    else:
        print("잘못입력")
    return r  # 결과값을 전달

# 더하기 연산
r = cal(2, 1, "+")
print(f"두 수를 더한 값: {r}")

# 빼기 연산
r = cal(2, 1, "-")
print(f"두 수를 뺀 값: {r}")
