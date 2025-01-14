import os
import shutil
import face_recognition

# 定義來源資料夾和目標資料夾的路徑
source_folder = r'填入圖片來源資料夾路徑'
one_face_folder = os.path.join(source_folder, 'one_face')
multiple_faces_folder = os.path.join(source_folder, 'multiple_faces')
no_face_folder = os.path.join(source_folder, 'no_face')

# 確保目標資料夾存在，如果不存在則創建
for folder in [one_face_folder, multiple_faces_folder, no_face_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 設置檔案的讀寫權限
def ensure_writable(file_path):
    try:
        # 設置為可讀寫
        os.chmod(file_path, 0o666)
    except Exception as e:
        print(f"無法更改檔案權限: {file_path}, 錯誤: {e}")

# 遍歷來源資料夾中的所有圖片檔案，並忽略目標資料夾
for root, dirs, files in os.walk(source_folder, topdown=True):
    dirs[:] = [d for d in dirs if d not in ['one_face', 'multiple_faces', 'no_face']]

    for file in files:
        if file.lower().endswith(('.jpg', '.png', '.jpeg')):
            file_path = os.path.join(root, file)

            # 先確保檔案可讀寫
            ensure_writable(file_path)

            # 加載圖片並進行人臉檢測
            image = face_recognition.load_image_file(file_path)
            face_locations = face_recognition.face_locations(image)

            # 根據檢測到的人臉數量進行分類
            if len(face_locations) == 1:
                shutil.move(file_path, os.path.join(one_face_folder, file))
                print(f"檢測到 1 人臉: {file}，已移到 {one_face_folder}")
            elif len(face_locations) > 1:
                shutil.move(file_path, os.path.join(multiple_faces_folder, file))
                print(f"檢測到多於 1 人臉: {file}，已移到 {multiple_faces_folder}")
            else:
                shutil.move(file_path, os.path.join(no_face_folder, file))
                print(f"未檢測到人臉: {file}，已移到 {no_face_folder}")
