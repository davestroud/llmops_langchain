import re

def parse_logs(file_path):
    with open(file_path, 'r') as f:
        logs = f.readlines()

    errors = [line for line in logs if "ERROR" in line]
    return errors

if __name__ == "__main__":
    errors = parse_logs("app_logs.log")
    print("Found Errors:")
    for error in errors:
        print(error)
