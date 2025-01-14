import os

# 定義來源資料夾的路徑，使用原始字符串避免轉義字元錯誤
source_folder = r'填入需清理的資料夾'

# 定義允許保留的圖片副檔名
image_extensions = ('.jpg', '.png', '.jpeg')

# 遞迴遍歷資料夾並刪除非圖片檔案
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # 檢查檔案是否是圖片檔案
        if not file.lower().endswith(image_extensions):
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)  # 刪除非圖片檔案
                print(f"已刪除: {file_path}")
            except Exception as e:
                print(f"無法刪除 {file_path}: {e}")

print("資料夾整理完成，只保留圖片檔案。")
