from rich import print
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
from rich.panel import Panel
from rich.progress import track
import time

# 콘솔 객체 생성
console = Console()

# 1. 기본 컬러 텍스트 출력
print("[bold magenta]안녕하세요, Rich입니다![/bold magenta] :sparkles:")

# 2. 테이블 출력
table = Table(title="사용자 정보")

# 열 추가 (이름, 나이, 언어)
table.add_column("이름", style="cyan", no_wrap=True)
table.add_column("나이", justify="right", style="green")
table.add_column("사용 언어", style="yellow")

# 행 추가
table.add_row("앨리스", "25", "Python")
table.add_row("밥", "30", "JavaScript")

# 테이블 출력
console.print(table)

# 3. 코드 하이라이트 출력
code = '''def 인사():
    print("안녕하세요, Rich!")'''

# 코드에 하이라이팅 적용 (언어: python, 테마: monokai)
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)

# 4. 패널 출력
panel = Panel("이 내용은 [bold green]패널[/bold green] 안에 있습니다.", title="패널 제목", subtitle="하단 설명")
console.print(panel)

# 5. 진행 바 출력
for step in track(range(10), description="처리 중..."):
    time.sleep(0.1)  # 예시로 잠깐 대기

from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

def print_ascii_art(choice):
    if choice == "1":
        art = """
[cyan]
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
[/cyan]
"""
    elif choice == "2":
        art = """
[green]
         /\\      /\\   
        /  \\    /  \\   
       /    \\  /    \\  
      /______\\/______\\ 
    /\\      /\\      /\\   
   /  \\    /  \\    /  \\   
  /    \\  /    \\  /    \\  
 /______\\/______\\/______\\ 
 ~~~~~~~~~~🏞️~~~~~~~~~~
     ~~~~~~~~~~🌲~~~~~~~~~
[/green]
"""
    elif choice == "3":
        art = """
[blue]
     \\     /     
      .-'-. 
   -- (   ) --
      `-.-'    
     /     \\
    ~~~~~~~~~~
      ☁️ ☁️ ☁️
[/blue]
"""
    else:
        print("[red]잘못된 선택입니다. 1, 2, 3 중에서 선택하세요.[/red]")
        return
    
    print(Panel.fit(art, title="🖼️ 아스키 아트", subtitle="Rich로 출력됨", border_style="bold magenta"))

# 프로그램 실행
while True:
    print("[bold yellow]\n1, 2, 3을 입력하여 아스키 아트를 선택하세요.[/bold yellow]")
    print("1: 해변 풍경 🏖️")
    print("2: 산과 호수 🏞️")
    print("3: 하늘과 구름 ☁️")
    print("0: 프로그램 종료 ❌")

    choice = Prompt.ask("선택", default="1")

    if choice == "0":
        print("[bold red]프로그램을 종료합니다.[/bold red]")
        break

    # 아스키 아트 출력 반복 여부
    while True:
        print_ascii_art(choice)
        again = Prompt.ask("계속 출력하시겠습니까? (y/n)", default="n").lower()
        if again != 'y':
            break
