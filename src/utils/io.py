import json

def read_json(file_path: str) -> dict:
    """Read a json file and return the dic t
    """
    with open(file_path) as f:
        return json.load(f)
    

def read_file(file_path: str) -> dict:
    """Read afile and return  the content 
    """
    with open(file_path) as f:
        return json.load(f)

        