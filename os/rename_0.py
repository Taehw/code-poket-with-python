#폴더명 변경 기본
#os 모듈 사용

import os

old_folder_name = "./base"
new_folder_name = "./change"

os.rename(old_folder_name, new_folder_name)
# os.rename : 파일이나 폴더의 이름을 변경
# 폴더가 존재하지 않으면 FileNotFoundError 발생
