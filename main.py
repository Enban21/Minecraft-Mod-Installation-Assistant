import sys
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QVBoxLayout, QWidget, QListWidget, QMessageBox
from file_manager import get_all_files, load_folder, update_list_widget
from xlsx_manager import load_xlsx
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon


# メインウィンドウ生成
def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))
    window = ModInstallationAssistant()
    window.show()
    sys.exit(app.exec_())

class ModInstallationAssistant(QMainWindow):
    def __init__(self):
        super().__init__()

        self.mod_categories = {}
        self.file_list = []
        self.folder_path = ''
        self.json_path = ''

        self.initUI()
        self.observer = None

    def initUI(self):
        self.setWindowTitle('Minecraft Mod Installation Assistant')
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()

        self.list_widget = QListWidget()
        self.list_widget.itemClicked.connect(self.open_link)  # アイテムクリックでリンクを開く
        layout.addWidget(self.list_widget)
        
        self.folder_button = QPushButton('modsフォルダを選択してください')
        self.folder_button.clicked.connect(self.load_folder)
        layout.addWidget(self.folder_button)

        self.json_button = QPushButton('Excelファイルを選択してください')
        self.json_button.clicked.connect(self.load_xlsx)
        layout.addWidget(self.json_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_xlsx(self):
        excel_path, _ = QFileDialog.getOpenFileName(self, 'Excelファイルを選択してください', '', 'Excel Files (*.xlsx)')
        if excel_path:
            load_xlsx(excel_path, self)

    def load_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'modsフォルダを選択してください')
        if folder_path:
            self.folder_path = folder_path
            load_folder(folder_path, self)

    def update_list_widget(self):
        update_list_widget(self)

    def open_link(self, item):
        link = item.data(Qt.UserRole)
        if link:
            webbrowser.open(link)
        else:
            QMessageBox.warning(self, 'リンクがありません。', 'No link available for this MOD.')

    def refresh_files(self):
        if self.folder_path:
            self.file_list = get_all_files(self.folder_path)
            self.update_list_widget()

if __name__ == "__main__":
    main()