def print_ascii_art(choice):
    if choice == 1:
        # 첫 번째 아스키 아트
        art1 = """
        ^_^
        ( o.o )
         > ^ <
        """
        print(art1)
    
    elif choice == 2:
        # 두 번째 아스키 아트
        art2 = """
        (\(^o^)/)
        """
        print(art2)
    
    elif choice == 3:
        # 세 번째 아스키 아트
        art3 = """
        (◕‿◕)
        """
        print(art3)
    
    else:
        print("잘못된 선택입니다. 1, 2, 3 중에서 선택하세요.")

# 사용자에게 선택 받기
print("1, 2, 3을 입력하여 아스키 아트를 선택하세요.")
print("1: 아스키 아트 1")
print("2: 아스키 아트 2")
print("3: 아스키 아트 3")

try:
    choice = int(input("선택: "))
    print_ascii_art(choice)
except ValueError:
    print("잘못된 입력입니다. 숫자를 입력하세요.")

