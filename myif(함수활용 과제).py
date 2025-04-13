def print_ascii_art(choice):
    if choice == 1:
        art = """
            ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
         ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
       ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
           ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
        ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
           ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
         ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
          ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
          ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
              ~ ~ ~ ~ ~ ~ ~ ~ ~
              🌊🌞 ~~~ 🌴🌊
        """
    elif choice == 2:
        art = """
             /\      /\   
            /  \    /  \   
           /    \  /    \  
          /______\/______\ 
        /\      /\      /\   
       /  \    /  \    /  \   
      /    \  /    \  /    \  
     /______\/______\/______\ 
     ~~~~~~~~~~🏞️~~~~~~~~~~
        ~~~~~~~~~~🌲~~~~~~~~~
        """
    elif choice == 3:
        art = """
         \     /     
          .-'-. 
       -- (   ) --
          -.-'    
         /     \\
        ~~~~~~~~~~
          ☁️☁️☁️
        """
    else:
        art = "잘못된 선택입니다. 1, 2, 3 중에서 선택하세요."

    print(art)


def run_program(print_count=1):
    while True:
        print("\n1, 2, 3을 입력하여 아스키 아트를 선택하세요.")
        print("1: 아스키 아트 1")
        print("2: 아스키 아트 2")
        print("3: 아스키 아트 3")
        print("0: 프로그램 종료")

        try:
            choice = int(input("선택: "))

            if choice == 0:
                print("프로그램을 종료합니다.")
                break

            if choice in [1, 2, 3]:
                for _ in range(print_count):
                    print_ascii_art(choice)
            else:
                print("1, 2, 3 중에서 선택하세요.")

        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")


# 실행 시작
print("프로그램 모드를 선택하세요:")
print("1: 그림 1번 출력 모드")
print("2: 그림 5번 출력 모드")

while True:
    try:
        mode = int(input("모드 선택 (1 또는 2): "))
        if mode == 1:
            run_program(print_count=1)
            break
        elif mode == 2:
            run_program(print_count=5)
            break
        else:
            print("1 또는 2 중에서 선택하세요.")
    except ValueError:
        print("숫자로 입력해주세요.")
