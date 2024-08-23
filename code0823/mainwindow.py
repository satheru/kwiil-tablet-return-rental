import tkinter as tk
from tkinter import *
import time
import tkinter.messagebox as msgbox
import excelfind as exfind

class MainWindow(tk.Tk):
    def __init__(self, username, on_goto_login, on_goto_borrow, on_goto_return):
        super().__init__()
        self.username = username
        self.on_goto_login = on_goto_login
        self.on_goto_borrow = on_goto_borrow
        self.on_goto_return = on_goto_return
        
        # tkinter 윈도우 생성
        self.title("스마트 기기 대출 반납 프로그램")
        
        self.state('zoomed')
        
        icon = tk.PhotoImage(file="kwill.png")
        self.iconphoto(False, icon)

        # label2를 담을 회색 배경의 프레임 생성
        label2_frame = Frame(self, bg="gray")
        label2_frame.pack(side="top", pady=10, fill="x")

        # label2를 회색 프레임 안에 배치하고 글씨 색깔을 하얀색으로 설정
        label2 = tk.Label(label2_frame, text="스마트 기기 대출 반납 프로그램", font=("맑은 고딕", 50), bg="gray", fg="white", anchor="w")
        label2.pack(pady=10, fill="both")


        borrow_button = tk.Button(
            self, 
            text="대출", 
            command=self.gotoborrow, 
            font=("맑은 고딕", 70),  # 글꼴 크기 조정
            width=10,                # 버튼 크기 증가
            height=4,                # 버튼 크기 증가
            bg="#4542f5",            # 배경색 설정
            fg="white"               # 텍스트 색 설정
        )
        
        borrow_button.place(relx=0.2, rely=0.5, anchor='center')

        return_button = tk.Button(
            self, 
            text="반납", 
            command=self.gotoreturn, 
            font=("맑은 고딕", 70),  # 글꼴 크기 조정
            width=10,                # 버튼 크기 증가
            height=4,                # 버튼 크기 증가
            bg="#f53d33",            # 배경색 설정
            fg="white"               # 텍스트 색 설정
        )
        
        return_button.place(relx=0.5, rely=0.5, anchor='center')

        check_button = tk.Button(
            self, 
            text="나의 대여 목록", 
            command=self.check,  
            font=("맑은 고딕", 35),  # 글꼴 크기 조정
            width=15,                 # 버튼 크기 조정
            height=2,                 # 버튼 크기 조정
            fg="black"                # 텍스트 색 설정
        )
        
        check_button.place(relx=0.8, rely=0.35, anchor='center')  # 간격 조정

        back_button = tk.Button(
            self, 
            text="로그아웃", 
            command=self.backtologin,  
            font=("맑은 고딕", 35),  # 글꼴 크기 조정
            width=15,                # 버튼 크기 조정
            height=2,                # 버튼 크기 조정
            fg="black"               # 텍스트 색 설정
        )
        
        back_button.place(relx=0.8, rely=0.65, anchor='center')  # 간격 조정

        label123 = tk.Label(self, text="Woosung 1.0", font=("Forte", 15))
        label123.pack(side="bottom", pady=15)
        
        self.mainloop()

    def backtologin(self):
        self.destroy()  # 현재 창을 파괴합니다
        self.on_goto_login()  
    
    def gotoborrow(self):
        self.destroy()
        self.on_goto_borrow()

    def gotoreturn(self):
        self.destroy()
        self.on_goto_return()
        
    def check(self):
        a = exfind.laptopsfind(self.username)
        b = len(a) 
        if not a:  # a가 빈 리스트이거나 None일 때
            msgbox.showinfo("확인", f"{self.username}님은 빌린 태블릿이 없습니다.")
        else:
            a_str = ','.join(map(str, a))
            msgbox.showinfo("확인", f"{self.username}님은 {a_str}번을 빌렸습니다. [총 {b}개] ")
