# 숫자 두 개를 입력을 받아서
# +, -, *, / 를 출력하는 프로그램을 만들어 보자

# 덧셈 프로그램
print("===== 덧셈 프로그램 =====")
try:
    # 사용자로부터 두 수 입력받기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    # 덧셈 수행
    result = num1 + num2
    # 결과 출력
    print(f"{num1} + {num2} = {result}")
except ValueError:
    print("올바른 숫자를 입력해주세요.")

# 뺄셈 프로그램
print("===== 뺄셈 프로그램 =====")
try:
    # 사용자로부터 두 수 입력받기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    # 뺄셈 수행
    result = num1 - num2
    # 결과 출력
    print(f"{num1} - {num2} = {result}")
except ValueError:
    print("올바른 숫자를 입력해주세요.")

# 곱셈 프로그램
print("===== 곱셈 프로그램 =====")
try:
    # 사용자로부터 두 수 입력받기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    # 곱셈 수행
    result = num1 * num2
    # 결과 출력
    print(f"{num1} × {num2} = {result}")
except ValueError:
    print("올바른 숫자를 입력해주세요.")

# 나눗셈 프로그램
print("===== 나눗셈 프로그램 =====")
try:
    # 사용자로부터 두 수 입력받기
    num1 = float(input("첫 번째 숫자를 입력하세요: "))
    num2 = float(input("두 번째 숫자를 입력하세요: "))
    # 0으로 나누는 경우 확인
    if num2 == 0:
        print("0으로 나눌 수 없습니다.")
    else:
        # 나눗셈 수행
        result = num1 / num2
        # 결과 출력
        print(f"{num1} ÷ {num2} = {result}")
except ValueError:
    print("올바른 숫자를 입력해주세요.")
