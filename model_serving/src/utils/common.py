import yaml
import base64

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content
    
def decode_sound(sound_str, file_path):
    sound_data = base64.b64decode(sound_str)
    with open(file_path, 'wb') as f:
        f.write(sound_data)

def encode_sound(file_path: str) -> str:
    with open(file_path, "rb") as file:
        string = base64.b64encode(file.read()).decode("utf-8")
        return string
