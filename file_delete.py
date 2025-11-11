import os

folder_name="E:/my_folder"

for file_name in os.listdir(folder_name):
    file_path=os.path.join(folder_name,file_name)
    if(os.path.exists(file_path)):
        os.remove(file_path)

print(f"Delete all file in {folder_name} folder")
