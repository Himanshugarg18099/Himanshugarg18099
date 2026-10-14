import json

def validate_json_report(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        if not isinstance(data, list):
            print("Error: JSON must be a list (array).")
            return False

        return True
    except FileNotFoundError:
        print("Error: File not found.")
        return False
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return False
