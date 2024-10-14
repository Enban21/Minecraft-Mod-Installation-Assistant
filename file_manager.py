# file_manager.py
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class ModFileSystemEventHandler(FileSystemEventHandler):
    def __init__(self, app):
        self.app = app

    def on_any_event(self, event):
        self.app.refresh_files()

def start_observer(folder_path, app):
    event_handler = ModFileSystemEventHandler(app)
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()
    return observer

def get_all_files(folder_path):
    all_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.relpath(os.path.join(root, file), folder_path)
            all_files.append(full_path)
    return all_files

def load_folder(folder_path, app):
    file_list = get_all_files(folder_path)
    app.file_list = file_list
    app.update_list_widget()  # 呼び出し先を修正
    
    # Start observing the folder for changes
    if app.observer:
        app.observer.stop()
        app.observer.join()

    app.observer = start_observer(folder_path, app)

def update_list_widget(app):
    app.list_widget.clear()
    for category, mods in app.mod_categories.items():
        app.list_widget.addItem(f"{category}")
        for mod in mods:
            folder = mod.get('folder', '')
            file_name = mod['file']
            link = mod.get('link', '')
            description = mod.get('description', '')
            full_path = os.path.join(folder, file_name) if folder else file_name
            is_present = full_path in app.file_list
            status = "✔" if is_present else "✘"
            
            # ファイル名と補足説明を通常のテキストとして表示
            item_text = f"{status} - {file_name} - {description}"
            item = QListWidgetItem(item_text)
            
            # 文字色の設定
            if is_present:
                item.setForeground(QColor('green'))
            else:
                item.setForeground(QColor('red'))
            
            item.setData(Qt.UserRole, link)  # リンクをアイテムデータに保存
            app.list_widget.addItem(item)