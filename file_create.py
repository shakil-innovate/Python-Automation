import os

folder_name="E:/my_folder"

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

x=10001
for i in range(1,x):
    file_path=os.path.join(folder_name,f"file_{i}.txt")
    with open (file_path,"w") as f:
        f.write(f"THIS is file number {i}")

print(f"{x-1} file create successfully")
