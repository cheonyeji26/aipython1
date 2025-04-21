from PIL import Image

# 1. 이미지 열기
try:
    img = Image.open("your_image.jpg")  # 처리할 이미지 파일 경로를 넣어주세요.
    print(f"이미지 크기: {img.size}")
    print(f"이미지 형식: {img.format}")
    print(f"색상 모드: {img.mode}")

    # 2. 흑백으로 변환
    img_gray = img.convert("L")  # "L" 모드는 흑백(grayscale)을 의미합니다.
    print(f"변환 후 색상 모드: {img_gray.mode}")

    # 3. 흑백 이미지 저장
    img_gray.save("your_image_gray.png")  # 저장할 파일 경로와 이름을 지정합니다.
    print("흑백 이미지 저장 완료!")

except FileNotFoundError:
    print("오류: 해당 이미지 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"오류 발생: {e}")