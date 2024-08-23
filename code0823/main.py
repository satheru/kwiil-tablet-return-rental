from mainwindow import MainWindow
from loginwindow import LoginWindow
from borrowwindow import BorrowWindow
from returnwindow import ReturnWindow
from adminwindow import AdminWindow

class App:
    def __init__(self) -> None:
        self.username = None
        
    def open_loginwindow(self) -> None:
        self.win = LoginWindow(self.on_login_success, self.on_login_fail, self.on_admin_login)
        
    def on_login_success(self, username) -> None:
        self.username = username
        self.open_mainwindow()
        
    def open_borrowwindow(self):
        self.win = BorrowWindow(self.username, self.open_mainwindow , self.open_loginwindow)

    def open_returnwindow(self):
        self.win = ReturnWindow(self.username, self.open_mainwindow , self.open_loginwindow)
        
    def open_mainwindow(self):    
        self.win = MainWindow(self.username,self.open_loginwindow,self.open_borrowwindow,self.open_returnwindow)
    
    def on_login_fail(self) -> None:
        pass
        
    def on_admin_login(self) -> None:
        self.open_adminwindow()
    
    def open_adminwindow(self):
        self.win = AdminWindow(self.open_loginwindow)
    
if __name__ == "__main__":
    app = App()
    app.open_loginwindow()
    
    