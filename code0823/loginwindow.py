import excelfind as exfind
import tkinter.messagebox as msgbox
import tkinter as tk
from tkinter import *

class LoginWindow(tk.Tk):
    def __init__(self, on_login_success, on_login_fail , on_admin_login):
        super().__init__()
        self.on_login_success = on_login_success
        self.on_login_fail = on_login_fail
        self.on_admin_login = on_admin_login

        # tkinter 윈도우 생성
        self.title("로그인 화면")
        
        self.state('zoomed')
        self.resizable(False, False)

        icon = tk.PhotoImage(file="kwill.png")
        self.iconphoto(False, icon)

        # label2를 담을 회색 배경의 프레임 생성
        label2_frame = Frame(self, bg="gray")
        label2_frame.pack(side="top", pady=10, fill="x")

        # label2를 회색 프레임 안에 배치하고 글씨 색깔을 하얀색으로 설정
        label2 = tk.Label(label2_frame, text="스마트 기기 대출 반납 프로그램", font=("맑은 고딕", 50), bg="gray", fg="white", anchor="w")
        label2.pack(pady=10, fill="both")

        # 중앙에 위치시킬 프레임 생성
        center_frame = Frame(self)
        center_frame.pack(expand=True)

        # 아이디 입력란 생성
        label = tk.Label(center_frame, text="이름을 입력하고 확인 버튼을 눌러주세요.",font=("맑은 고딕", 30))
        label.pack(pady=30)

        self.entry = tk.Entry(center_frame,font=("맑은 고딕", 40))
        self.entry.pack(pady=30)
        self.entry.focus_set()

        # 로그인 버튼 생성
        login_button = tk.Button(center_frame, text="확인",font=("맑은 고딕", 40), command=self.on_login)
        login_button.pack(pady=30)

        # 주의 라벨을 밑쪽에 배치
        version_label = tk.Label(self, text="Woosung 1.0",
                          font=("Forte", 15))
        version_label.pack(side="bottom", pady=15)
        
        
        warning_label = tk.Label(self, text="      주의   :   이 프로그램을 사용할 땐 꼭 엑셀을 꺼주시기 바랍니다.",
                          font=("맑은 고딕", 25))
        warning_label.pack(side="bottom", pady=(0, 5))
        
        # "Woosung 1.0" 라벨을 밑쪽에 배치
        

        self.mainloop()

    def on_login(self):
        username = self.entry.get()
        if exfind.namefind(username) == True:
            self.destroy()
            self.on_login_success(username)
            
        elif username == "admin" or username == "관리자":
            msgbox.showinfo("경고", "관리자 모드로 접속합니다.")
            self.destroy()
            self.on_admin_login()
            
        else:
            msgbox.showinfo("오류", "이름이 목록에 없거나 잘못 입력되었습니다.")
            self.entry.delete(0, END)
