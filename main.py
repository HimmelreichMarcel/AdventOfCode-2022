from pathlib import Path
import json

DAYS = 24

def create_folder(path):
    try:
        Path(path).mkdir(parents=True, exist_ok=True)
    except Exception as error:
        print("Unable to export dictionary as json")
        print(error)

def main():
    for day in range(DAYS):
        create_folder(f"Day_{day + 1}")  
        
main()