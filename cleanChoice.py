import os

# 定義目標資料夾的路徑
folder_path = r'填入資料夾路徑'

# 遍歷目標資料夾中的所有檔案，但不刪除子資料夾
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            os.remove(file_path)  # 刪除檔案
            print(f"已刪除: {file_path}")
        except Exception as e:
            print(f"無法刪除 {file_path}: {e}")
    # 只處理頂層資料夾中的檔案，跳過子資料夾
    break

print("目標資料夾中的所有檔案已刪除，但保留了子資料夾。")
