# json_manager.py
import json

def load_json(json_path, app):
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            app.mod_categories = json.load(file)
        app.update_list_widget()
    except Exception as e:
        raise Exception(f'JSONファイルの読み込みに失敗しました: {e}')
