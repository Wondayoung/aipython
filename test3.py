def print_cat_art():
    cat_art = """
    /\_/\  
   ( o.o ) 
    > ^ <
    """
    print(cat_art)

# 고양이 아스키 아트 3번 반복 출력
for i in range(3):
    print(f"[{i + 1}번째 반복]")
    print_cat_art()
