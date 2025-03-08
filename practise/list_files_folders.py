import os

def list_files_folder(folder):
     try:
          files=os.listdir(folder)
          return files, None
     except FileNotFoundError:
          return None,"file not found"
          
    
def main():
    folder_names=input("enter folder names separated by spaces ").split()
    #try:
    for folder in folder_names:
            files,error_message=list_files_folder(folder)
            #files=os.listdir(folder)
            if files:
               for file in files:
                  print(file)
            else:
                 print(error_message)
    #except FileNotFoundError:
        #print("folder does not exist")
if __name__ == "__main__":
     main()
