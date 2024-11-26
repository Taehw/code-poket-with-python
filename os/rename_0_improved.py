#기존코드에 예외처리 기능을 추가
#os.path.exists 사용


import os

old_folder_name = "./base"
new_folder_name = "./change"

if os.path.exists(old_folder_name):
    if not os.path.exists(new_folder_name):
        os.rename(old_folder_name, new_folder_name)
        print(f"폴더명이 '{old_folder_name}'에서 '{new_folder_name}으로 변경")
    else:
        print(f"{new_folder_name} already exist")
else:
    print(f"'{old_folder_name}' doesn't exist")
