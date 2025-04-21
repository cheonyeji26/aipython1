import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(
        title="이미지 파일 선택",
        filetypes=(("이미지 파일", "*.png;*.jpg;*.jpeg;*.gif;*.bmp"), ("모든 파일", "*.*"))
    )
    if file_path:
        try:
            img = Image.open(file_path)
            # tkinter에서 사용할 수 있는 PhotoImage 객체로 변환
            photo = ImageTk.PhotoImage(img)
            # 이미지 라벨 업데이트
            image_label.config(image=photo)
            image_label.image = photo  # 이미지 객체를 유지하기 위해 참조 저장
        except FileNotFoundError:
            tk.messagebox.showerror("오류", "이미지 파일을 찾을 수 없습니다.")
        except Exception as e:
            tk.messagebox.showerror("오류", f"이미지 열기 오류: {e}")

# 메인 윈도우 생성
window = tk.Tk()
window.title("이미지 뷰어")

# 이미지 라벨 생성 (처음에는 빈 라벨)
image_label = tk.Label(window)
image_label.pack()

# "이미지 열기" 버튼 생성
open_button = tk.Button(window, text="이미지 열기", command=open_image)
open_button.pack(pady=10)

# GUI 프로그램 실행
window.mainloop()