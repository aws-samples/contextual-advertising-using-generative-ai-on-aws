import json

def save_json_to_file(name, json_data):
    with open(name, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False)
    return json_data