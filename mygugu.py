# 숫자 두개를 입력을 받아서
# +, -, *, / 를 출력하는 프로그램을 만들어 보자
def calculate_operations():
    try:
        # 두 개의 숫자를 입력받습니다.
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))

        # 사칙연산을 수행합니다.
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        
        # 나눗셈은 0으로 나누는 경우를 예외 처리합니다.
        try:
            division = num1 / num2
        except ZeroDivisionError:
            division = "정의되지 않음 (0으로 나눌 수 없음)"

        # 결과를 출력합니다.
        print(f"{num1} + {num2} = {addition}")
        print(f"{num1} - {num2} = {subtraction}")
        print(f"{num1} * {num2} = {multiplication}")
        print(f"{num1} / {num2} = {division}")

    except ValueError:
        # 숫자가 아닌 값을 입력했을 때의 예외 처리입니다.
        print("올바른 숫자를 입력하세요.")

# 프로그램 실행
calculate_operations()