import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import excelfind as exfind
import excelwrite as exwrite

class AdminWindow(tk.Tk):
    def __init__(self, on_goto_login):
        super().__init__()
        self.on_goto_login = on_goto_login
        
        self.title("관리자 화면")
        self.state('zoomed')
        self.resizable(False, False)
        
        icon = tk.PhotoImage(file="kwill.png")
        self.iconphoto(False, icon)

        label2 = tk.Label(self, text="관리자용 비밀번호 입력", font=("맑은 고딕", 35))
        label2.pack(side="top", pady=10)
        
        self.entry = tk.Entry(self, font=("맑음 고딕", 20), show="*")
        self.entry.pack(side="top", padx=5)
        self.entry.focus_set()
        
        label3 = tk.Label(self, text="노트북 번호 입력(1개만)", font=("맑은 고딕", 35))
        label3.pack(side="top", pady=10)
        
        self.entry2 = tk.Entry(self, font=("맑음 고딕", 20))
        self.entry2.pack(side="top", padx=5)
        
        label4 = tk.Label(self, text="대출시 대출할 사람 입력 / 반납시 반납  입력", font=("맑은 고딕", 35))
        label4.pack(side="top", pady=10)
        
        self.entry3 = tk.Entry(self, font=("맑음 고딕", 20))
        self.entry3.pack(side="top", padx=5)
        
        # 확인 버튼 (입력창 오른쪽에 배치)
        self.insert_button = tk.Button(self, text="확인", font=("맑음 고딕", 20), command=self.edit)
        self.insert_button.pack(side="top", padx=5)
        
        label4 = tk.Label(self, text="명부등은 엑셀파일에서 직접 수정하시기 바랍니다\n경고: 이 프로그램과 엑셀을 동시에 실행시키면 작동하지 않습니다!", font=("맑은 고딕", 25))
        label4.pack(side="top", pady=10)
        
        self.insert_button = tk.Button(self, text="버전확인", font=("맑음 고딕", 20), command=self.version)
        self.insert_button.pack(side="top", pady=20)
        
        label123 = tk.Label(self, text="Woosung 1.0",
                          font=("Forte", 15))
        label123.pack(side="bottom", pady=15)
        
        self.insert_button = tk.Button(self, text="나가기(로그인창으로)", font=("맑음 고딕", 30), command=self.backtologin)
        self.insert_button.pack(side="bottom", pady=20)
        
        self.mainloop()
        
        
       
    def edit(self):
        password = self.entry.get()
        barcode_a = self.entry2.get()
        barcode = barcode_a.replace("ㅅ뮤", "tab")
        name = self.entry3.get()
        
        number = exfind.adminbarcode(barcode)
        
        if password == "guis128876!":
            if not number == False:
                
                if name == "반납":
                    name = "none"
                
                exwrite.adminwrite(number,name)
                msgbox.showinfo("완료", f"{number}번 노트북을 {name}  명의로 수정했습니다\n(명의가 none일 경우 반납입니다)")
                
            else:
                msgbox.showinfo("오류", "바코드가 알맞지 않습니다")
        else:
            msgbox.showinfo("오류", "비밀번호가 틀립니다")
            self.entry.delete(0, END)
            
            
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        
    def backtologin(self):
        self.destroy()
        self.on_goto_login()
        
    def version(self):
        msgbox.showinfo("Check source code version by date", " 2024-08-28 ver.  // WS\n*listbox에 값이 추가 될때마다 정렬.")