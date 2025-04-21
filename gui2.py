import tkinter as tk
from PIL import Image, ImageTk

def show_cat():
    try:
        img = Image.open("d/cat.jpg")  # 고양이 이미지 파일명
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
    except FileNotFoundError:
        show_error("고양이 이미지를 찾을 수 없습니다.")
    except Exception as e:
        show_error(f"고양이 이미지 열기 오류: {e}")

def show_penguin():
    try:
        img = Image.open("d/penguin.jpg")  # 펭귄 이미지 파일명
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
    except FileNotFoundError:
        show_error("펭귄 이미지를 찾을 수 없습니다.")
    except Exception as e:
        show_error(f"펭귄 이미지 열기 오류: {e}")

def show_raccoon():
    try:
        img = Image.open("d/raccoon.jpeg")  # 너구리 이미지 파일명
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
    except FileNotFoundError:
        show_error("너구리 이미지를 찾을 수 없습니다.")
    except Exception as e:
        show_error(f"너구리 이미지 열기 오류: {e}")

def show_error(message):
    tk.messagebox.showerror("오류", message)

# 메인 윈도우 생성
window = tk.Tk()
window.title("동물 이미지 뷰어")

# 이미지 라벨 생성
image_label = tk.Label(window)
image_label.pack(pady=10)

# 버튼 생성
cat_button = tk.Button(window, text="고양이", command=show_cat)
cat_button.pack(pady=5)

penguin_button = tk.Button(window, text="펭귄", command=show_penguin)
penguin_button.pack(pady=5)

raccoon_button = tk.Button(window, text="너구리", command=show_raccoon)
raccoon_button.pack(pady=5)

# GUI 프로그램 실행
window.mainloop()