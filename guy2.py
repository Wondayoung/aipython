import tkinter as tk
from PIL import ImageTk, Image

def show_mountain():
    """산 이미지를 표시하는 함수"""
    img = Image.open("mountain.jpg") # 산 이미지 파일 경로
    img.thumbnail((400, 400)) # 이미지 크기 조절 (원하는 크기로 변경)
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo # 가비지 컬렉션 방지를 위해 레퍼런스 유지

def show_sea():
    """바다 이미지를 표시하는 함수"""
    img = Image.open("sea.jpg") # 바다 이미지 파일 경로
    img.thumbnail((400, 400)) # 이미지 크기 조절
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo

def show_cloud():
    """구름 이미지를 표시하는 함수"""
    img = Image.open("cloud.jpg") # 구름 이미지 파일 경로
    img.thumbnail((400, 400)) # 이미지 크기 조절
    photo = ImageTk.PhotoImage(img)
    image_label.config(image=photo)
    image_label.image = photo

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("이미지 뷰어")

# 이미지를 표시할 라벨 생성
image_label = tk.Label(root)
image_label.pack(pady=10)

# 버튼 프레임 생성
button_frame = tk.Frame(root)
button_frame.pack()

# 산 버튼 생성
mountain_button = tk.Button(button_frame, text="산", command=show_mountain)
mountain_button.grid(row=0, column=0, padx=5)

# 바다 버튼 생성
sea_button = tk.Button(button_frame, text="바다", command=show_sea)
sea_button.grid(row=0, column=1, padx=5)

# 구름 버튼 생성
cloud_button = tk.Button(button_frame, text="구름", command=show_cloud)
cloud_button.grid(row=0, column=2, padx=5)

# Tkinter 이벤트 루프 시작
root.mainloop()