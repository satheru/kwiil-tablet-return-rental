import tkinter as tk
from tkinter import *
import tkinter.messagebox as msgbox
import excelfind as exfind
import excelwrite as exwrite

class BorrowWindow(tk.Tk):
    def __init__(self, username, on_goto_main , on_goto_login ):
        super().__init__()
        self.username = username
        self.on_goto_main = on_goto_main
        self.on_goto_login = on_goto_login
        
        self.borrowpot = set()  # 중요!!!! 여기에 담아서 한번에 넘김.
        
        
        # tkinter 윈도우 생성
        self.title("스마트 기기 대출 반납 프로그램 : 대출")
        self.state('zoomed')
        self.resizable(False, False)
        
        icon = tk.PhotoImage(file="kwill.png")
        self.iconphoto(False, icon)

        # label2를 담을 회색 배경의 프레임 생성
        label2_frame = Frame(self, bg="gray")
        label2_frame.pack(side="top", pady=10, fill="x")

        # label2를 회색 프레임 안에 배치하고 글씨 색깔을 하얀색으로 설정
        label2 = tk.Label(label2_frame, text="스마트 기기 대출 반납 프로그램 : 대출", font=("맑은 고딕", 50), bg="gray", fg="white", anchor="w")
        label2.pack(pady=10, fill="both")

        
        label3_frame = Frame(self)
        label3_frame.pack(side="left", padx=20, pady=20)  # 왼쪽에 배치하고 여백을 줍니다.

        label3 = tk.Label(label3_frame, text="\n      :사용 방법:       \n\n바코드를 찍습니다\n\n필요한 갯수만큼 찍으신 후\n대여을 누릅니다\n(한번에 모두 처리됩니다.)\n\n잘못 찍으셨다면\n잘못 찍은 태블릿을 누르고\n취소를 누릅니다.\n",
                        font=("맑은 고딕", 35), relief="solid", bd=2, padx=10, pady=10)  # solid 스타일의 테두리와 패딩 추가
        label3.pack(side="left")
        
        # 바코드 입력 프레임 생성
        entry_frame = Frame(self)
        entry_frame.pack(pady=20)

        # 바코드 입력창
        self.entry_var = tk.StringVar()
        self.entry_var.trace_add("write", self.check_length)  # 입력 길이를 추적
        self.entry = tk.Entry(entry_frame, textvariable=self.entry_var, font=("맑음 고딕", 40), width=22)
        self.entry.pack(side="right", padx=10, pady=20)
        self.entry.focus_set()
        
        # 리스트박스와 취소, 대여 버튼을 담을 프레임 생성
        listbox_frame = Frame(self)
        listbox_frame.pack(pady=20)

        # 리스트박스
        self.listbox = Listbox(listbox_frame, height=11, width=15, font=("맑은 고딕", 35))
        self.listbox.pack(side="left", expand=False)

        # 스크롤바 설정
        scrollbar = Scrollbar(listbox_frame, orient="vertical", width=30)  # 너비를 30으로 설정
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side="left", fill="y")
        
        
        # 버튼들을 담을 프레임 생성 (취소 버튼과 대여 버튼을 세로로 배치)
        button_frame = Frame(listbox_frame)
        button_frame.pack(side="left", padx=10, fill="y")

        # 취소 버튼 (리스트박스 오른쪽에 배치)
        self.cancel_button = tk.Button(button_frame, text="취소", font=("맑은 고딕", 30), command=self.remove, height=2, width=10)
        self.cancel_button.pack(pady=25)

        # 대여 버튼 (취소 버튼 아래에 배치)
        self.processing_button = tk.Button(button_frame, text="대여", font=("맑은 고딕", 30), command=self.processing, height=2, width=10)
        self.processing_button.pack(pady=25)

        self.back = tk.Button(button_frame, text="뒤로가기", font=("맑음 고딕", 30), command=self.backtomain, height=2, width=10)
        self.back.pack(side="bottom")
        
    
        

        label123 = tk.Label(self, text="Woosung 1.0",
                          font=("Forte", 15))
        label123.pack(side="bottom", pady=10)
        
        self.mainloop()

    def add(self):
        barcode_a = self.entry.get()
        barcode = barcode_a.replace("ㅆ", "T")
        
        number = exfind.barcodefind(self.username, barcode, "b")
        
        if number == False:  # 누군가 대여중일 때
            msgbox.showinfo("오류", "누군가 해당 태블릿을 이미 대여중입니다")
            self.entry.delete(0, END)  # 입력창의 텍스트를 지움
        
        else:
            if isinstance(number, int):  # 정상 상황일 때
                if not number in self.borrowpot:  # 처음 선택할때
                    self.entry.delete(0, END)  # 입력창의 텍스트를 지움
                    
                    # listbox에서 현재 모든 항목을 가져옴
                    current_items = list(self.listbox.get(0, END))
                    new_item = f"{number}번 태블릿"
                    current_items.append(new_item)
                    
                    # 항목들을 정렬
                    current_items.sort()
                    
                    # 새로 추가된 항목의 인덱스를 찾음
                    new_index = current_items.index(new_item)
                    
                    # listbox 초기화
                    self.listbox.delete(0, END)
                    
                    # 정렬된 항목들을 다시 listbox에 추가
                    for item in current_items:
                        self.listbox.insert(END, item)
                    
                    # 새로 추가된 항목을 선택
                    self.listbox.select_set(new_index)
                    self.listbox.activate(new_index)
                    self.listbox.see(new_index)
                    
                    self.borrowpot.add(number)
                    
                else:  # 이미 선택되어 있을때
                    msgbox.showinfo("오류", f"{number}번 태블릿은 이미 선택되어있는 태블릿입니다")
                    self.entry.delete(0, END)
                    
            else:  # 없는 바코드일 때
                msgbox.showinfo("오류", "바코드에 맞는 태블릿을 찾을 수 없습니다")
                self.entry.delete(0, END)  # 입력창의 텍스트를 지움




    def check_length(self, *args):
        if len(self.entry_var.get()) == 5:
            self.add()

    def remove(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_item = self.listbox.get(selected_index)
            self.listbox.delete(selected_index)
            # "번 태블릿"이라는 텍스트를 파싱하여 숫자만 추출
            number = int(selected_item.split('번')[0])
            self.borrowpot.discard(number)
            
    def processing(self):
        
        for value in sorted(self.borrowpot):
            exwrite.bwrite(value,self.username)
            
        #초기화
        a = self.borrowpot 
        self.borrowpot = set()
        self.listbox.delete(0, END)
        msgbox.showinfo("완료", f"{a}번 태블릿을 대여했습니다")
        
        self.destroy()
        self.on_goto_login()
        
        
        
    def backtomain(self):
        self.destroy()
        self.on_goto_main()