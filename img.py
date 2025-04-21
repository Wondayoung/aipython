from PIL import Image

try:
    # 이미지 열기
    img = Image.open('input.jpg')

    # 이미지 정보 출력
    print(f"이미지 크기: {img.size}")
    print(f"이미지 모드: {img.mode}")

    # 흑백으로 변환
    gray_img = img.convert('L')

    # 흑백 이미지 저장
    gray_img.save('output_grayscale.jpg')

    print("이미지를 흑백으로 변환하여 저장했습니다.")

except FileNotFoundError:
    print("오류: 'input.jpg' 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"오류 발생: {e}")