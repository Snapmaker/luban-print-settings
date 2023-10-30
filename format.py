import json
import os


ROOT_DIR = os.path.join(os.getcwd(), 'resources', 'laser')


for dirpath, dirnames, filenames in os.walk(ROOT_DIR):
    for filename in filenames:
        if filename.endswith('.json'):
            file_path = os.path.join(dirpath, filename)

            print('file path:', file_path)

            with open(file_path, 'r') as f:
                data = json.load(f)

            formatted_json = json.dumps(data, indent=4)
            
            with open(file_path, 'w') as f:
                f.write(formatted_json)
