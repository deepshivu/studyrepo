import os
def list_files(folder):
    try:
        files=os.listdir(folder)
        return files,None
    except FileNotFoundError:
        return None,"file not found"
def main():
    folder_names=input("enter folder names separated by spaces ").split()
    for folder in folder_names:
        files,error_message=list_files(folder)
        if files:
            for file in files:
                print(file)
        else:
            print(f"error with {folder}:{error_message}")
main()