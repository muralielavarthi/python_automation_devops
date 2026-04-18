import os

def files_in_folder(item):
    try:  
        files=os.listdir(item)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"

def main():
    folders_path= input("Enter a list of folder paths separated by spaces: ")
    folders_path_list=folders_path.split(" ")
    for item in folders_path_list:
        files, error_message=files_in_folder(item)
        if files:
            print("files in folder:",item)
            for item in files:
                print(item)
        else:
            print(f"Error in {item}:{error_message}")

if __name__ == "__main__": # invoking main
    main()
        

