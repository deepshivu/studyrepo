import os
def ret_files(folder):
      try:
        files=os.listdir(folder)    
        return files, None
      except FileNotFoundError:
        return None,"folder non found"
      except PermissionError:
        return None,"Permission non found" 
            
def main():
    folder_name=input("please enter folder name separated by spaces ").split()
    for folder in folder_name:
        
            files,error_message=ret_files(folder)
            if files:
                for file in files:
                    print(file) 
            
            else:
                print(f"error in {folder} , error message is {error_message}")
                
main()    

