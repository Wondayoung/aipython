import tkinter as tk
from tkinter import ttk # ttk는 좀 더 현대적인 위젯을 제공합니다.
from PIL import Image, ImageTk # Pillow 라이브러리에서 이미지 처리를 위한 모듈을 가져옵니다.
import os # 파일 존재 여부 확인을 위해 os 모듈을 가져옵니다.

# --- 이미지 파일 경로 설정 ---
# 스크립트 파일과 같은 디렉토리에 이미지가 있다고 가정합니다.
# 만약 다른 경로에 있다면, 전체 경로를 입력해주세요.
IMAGE_FILES = {
    "산": "산.jpg", # 실제 파일명으로 변경하세요
    "구름": "구름.jpg",     # 실제 파일명으로 변경하세요
    "바다": "바다.jpg",         # 실제 파일명으로 변경하세요
}

# --- 이미지 표시 함수 ---
def display_image(image_path):
    """주어진 경로의 이미지를 로드하여 레이블에 표시합니다."""
    if not os.path.exists(image_path):
        print(f"오류: 이미지 파일을 찾을 수 없습니다: {image_path}")
        # 파일이 없을 경우 메시지를 표시합니다.
        display_message(f"이미지 파일을 찾을 수 없습니다:\n{image_path}")
        return

    try:
        # Pillow를 사용하여 이미지 열기
        pil_image = Image.open(image_path)

        # 이미지를 Tkinter에서 사용할 수 있는 형식(PhotoImage)으로 변환
        # 이미지 크기가 너무 클 경우, 여기서 적절히 조절할 수 있습니다.
        # 예: pil_image = pil_image.resize((400, 300))

        tk_image = ImageTk.PhotoImage(pil_image)

        # 이미지 레이블의 이미지 업데이트
        image_label.config(image=tk_image)
        # Tkinter는 PhotoImage 객체에 대한 참조가 유지되어야 이미지를 표시합니다.
        # image_label.image에 tk_image를 할당하여 참조를 유지합니다.
        image_label.image = tk_image # 중요! 이미지 표시를 위해 반드시 필요

        # 메시지 삭제
        display_message("")

    except Exception as e:
        print(f"이미지 로딩 또는 표시 중 오류 발생 ({image_path}): {e}")
        display_message(f"이미지 로딩 오류:\n{image_path}\n{e}")

# --- 메시지 표시 함수 ---
def display_message(text):
     """이미지 대신 텍스트 메시지를 레이블에 표시합니다."""
     image_label.config(image='') # 기존 이미지 제거
     image_label.config(text=text) # 텍스트 설정


# --- 버튼 클릭 이벤트 핸들러 ---
def show_mountain():
    display_image(IMAGE_FILES["mountain"])

def show_cloud():
    display_image(IMAGE_FILES["cloud"])

def show_sea():
    display_image(IMAGE_FILES["sea"])

# --- GUI 설정 ---
root = tk.Tk()
root.title("풍경 이미지 뷰어") # 창 제목 설정

# 버튼들을 담을 프레임 생성 (버튼 정렬을 위해)
button_frame = ttk.Frame(root)
button_frame.pack(pady=10) # 위쪽에 약간의 여백 추가

# 산 버튼 생성
btn_mountain = ttk.Button(button_frame, text="산", command=show_mountain)
btn_mountain.pack(side="left", padx=5) # 왼쪽에 배치, 좌우 여백 5

# 구름 버튼 생성
btn_cloud = ttk.Button(button_frame, text="구름", command=show_cloud)
btn_cloud.pack(side="left", padx=5) # 왼쪽에 배치, 좌우 여백 5

# 바다 버튼 생성
btn_sea = ttk.Button(button_frame, text="바다", command=show_sea)
btn_sea.pack(side="left", padx=5) # 왼쪽에 배치, 좌우 여백 5

# 이미지를 표시할 레이블 생성
# text와 image를 함께 사용할 수 있도록 compound='image' 설정 (여기서는 이미지만 표시할 것이므로 꼭 필요하지는 않지만, 메시지 표시와 함께 사용하려면 유용)
image_label = ttk.Label(root, text="위의 버튼을 눌러 이미지를 보세요.", compound="image")
image_label.pack(pady=10) # 아래쪽에 여백 추가

# --- 초기 화면 (선택 사항) ---
# 프로그램 시작 시 특정 이미지를 바로 표시하려면 아래 주석을 해제하세요.
# show_mountain() # 시작 시 산 이미지 표시

# --- GUI 실행 ---
root.mainloop()
