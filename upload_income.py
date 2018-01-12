def upload():
    import smtplib

    gmail_user = "lufu.family@gmail.com"
    gmail_pwd = "242familyacc"
    FROM = "lufu.family@gmail.com"
    TO = "sunny.lu.sl@gmail.com"
    SUBJECT = "test"
    TEXT = "test"

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print('上傳成功!')
    except:
        print("上傳失敗...請聯絡Sunny")
        print("郵件: sunny.lu.sl@gmail.com")


import sys
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QLabel, QPushButton, QMessageBox, QMainWindow, QComboBox)
from PyQt5.QtCore import pyqtSlot
import datetime

now = datetime.datetime.now()
month = now.month
year = now.year
class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = '收租記錄幫手'
        self.left = 10
        self.top = 50
        self.width = 650
        self.height = 750
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(650, 750)
        self.statusBar().showMessage("Ready!")


        month_select = QComboBox(self)
        month_select.addItem("Month")
        month_select.addItem("01 月")
        month_select.addItem("02 月")
        month_select.addItem("03 月")
        month_select.addItem("04 月")
        month_select.addItem("05 月")
        month_select.addItem("06 月")
        month_select.addItem("07 月")
        month_select.addItem("08 月")
        month_select.addItem("09 月")
        month_select.addItem("10 月")
        month_select.addItem('11 月')
        month_select.addItem('12 月')
        month_select.resize(100,100)
        month_select.move(20,600)

        year_select = QComboBox(self)
        year_select.addItem("Year")
        year_select.addItem(str(year))
        year_select.addItem(str(year - 1))
        year_select.addItem(str(year - 2))
        year_select.addItem(str(year - 3))
        year_select.addItem(str(year - 4))
        year_select.resize(100, 100)
        year_select.move(120, 600)

        month_select.setCurrentIndex(int(month - 1 if month - 1 > 0 else month + 11))
        year_select.setCurrentText(str(year if month_select.currentIndex() != 12 else year - 1))

        #House Labels
        Mich_242 = QLabel("242 Michener Dr", self)
        Rae_873 = QLabel("873 Rae St", self)
        Rae_1064 = QLabel("1064 Rae St", self)
        Athol_943 = QLabel("943 Athol St", self)
        Broad_1929 = QLabel("1929 Broad St", self)
        Assiniboine_1102 = QLabel("1102 Assiniboine", self)
        Desmond_816 = QLabel("816 Desmond", self)
        ON_condo = QLabel("ON Condo", self)
        Gren_Farm = QLabel("Grenfell Farm", self)

        Mich_242.move(20, 60)
        Rae_873.move(20, 120)
        Rae_1064.move(20, 180)
        Athol_943.move(20, 240)
        Broad_1929.move(20, 300)
        Assiniboine_1102.move(20, 360)
        Desmond_816.move(20, 420)
        ON_condo.move(20, 480)
        Gren_Farm.move(20, 540)

        income = QLabel("收進/Income", self)
        expense = QLabel("支出/Expense", self)
        income.move(220, 20)
        expense.move(470, 20)

        #Houses Income Box
        self.aMichener_242 = QLineEdit(self)
        self.aRae_873 = QLineEdit(self)
        self.aRae_1064 = QLineEdit(self)
        self.aAthol_943 = QLineEdit(self)
        self.aBroad_1929 = QLineEdit(self)
        self.aAssiniboine_1102 = QLineEdit(self)
        self.aDesmond_816 = QLineEdit(self)
        self.aON_condo = QLineEdit(self)
        self.aGren_Farm = QLineEdit(self)

        self.aMichener_242.move(150, 60)
        self.aRae_873.move(150, 120)
        self.aRae_1064.move(150, 180)
        self.aAthol_943.move(150, 240)
        self.aBroad_1929.move(150, 300)
        self.aAssiniboine_1102.move(150, 360)
        self.aDesmond_816.move(150, 420)
        self.aON_condo.move(150, 480)
        self.aGren_Farm.move(150, 540)

        self.aMichener_242.resize(200, 40)
        self.aRae_873.resize(200, 40)
        self.aRae_1064.resize(200, 40)
        self.aAthol_943.resize(200, 40)
        self.aBroad_1929.resize(200, 40)
        self.aAssiniboine_1102.resize(200, 40)
        self.aDesmond_816.resize(200, 40)
        self.aON_condo.resize(200, 40)
        self.aGren_Farm.resize(200, 40)

        #House expense
        self.Michener_242 = QLineEdit(self)
        self.Rae_873 = QLineEdit(self)
        self.Rae_1064 = QLineEdit(self)
        self.Athol_943 = QLineEdit(self)
        self.Broad_1929 = QLineEdit(self)
        self.Assiniboine_1102 = QLineEdit(self)
        self.Desmond_816 = QLineEdit(self)
        self.ON_condo = QLineEdit(self)
        self.Gren_Farm = QLineEdit(self)

        self.Michener_242.move(400, 60)
        self.Rae_873.move(400, 120)
        self.Rae_1064.move(400, 180)
        self.Athol_943.move(400, 240)
        self.Broad_1929.move(400, 300)
        self.Assiniboine_1102.move(400, 360)
        self.Desmond_816.move(400, 420)
        self.ON_condo.move(400, 480)
        self.Gren_Farm.move(400, 540)

        self.Michener_242.resize(200, 40)
        self.Rae_873.resize(200, 40)
        self.Rae_1064.resize(200, 40)
        self.Athol_943.resize(200, 40)
        self.Broad_1929.resize(200, 40)
        self.Assiniboine_1102.resize(200, 40)
        self.Desmond_816.resize(200, 40)
        self.ON_condo.resize(200, 40)
        self.Gren_Farm.resize(200, 40)
        #Create a button in the window
        button = QPushButton('上傳表格\nUpload', self)
        button.setToolTip("Upload")
        button.resize(300, 100)
        button.move(320, 600)
        button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        print("uploading...")
        text = self.textbox.text()
        # Branch of question
        reply = QMessageBox.question(self, "Confirmation", "Upload now?", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            
            #upload()
            self.aMichener_242.setText("")
            self.aRae_873.setText("")
            self.aRae_1064.setText("")
            self.aAthol_943.setText("")
            self.aBroad_1929.setText("")
            self.aAssiniboine_1102.setText("")
            self.aDesmond_816.setText("")
            self.aON_condo.setText("")
            self.aGren_Farm.setText("")
            self.Michener_242.setText("")
            self.Rae_873.setText("")
            self.Rae_1064.setText("")
            self.Athol_943.setText("")
            self.Broad_1929.setText("")
            self.Assiniboine_1102.setText("")
            self.Desmond_816.setText("")
            self.ON_condo.setText("")
            self.Gren_Farm.setText("")
            self.statusBar().showMessage("上傳成功! Complete!")
        else:
            self.textbox.setText(text)
            self.statusBar().showMessage("Ready!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
