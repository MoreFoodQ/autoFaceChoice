import os
import random
import shutil
from PIL import Image

# 定義來源資料夾和目標資料夾的路徑，使用原始字符串避免轉義字元錯誤
source_folder = r'填入資料夾路徑'
output_folder = r'填入資料夾路徑r'

# 設定預設隨機選取圖片的數量
image_count = 50  # 你可以改變這個值來選取不同數量的圖片

# 確保目標資料夾存在，如果不存在則創建
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 使用 os.walk 遞迴讀取所有子資料夾中的圖片檔案
image_files = []
for root, dirs, files in os.walk(source_folder):
    for file in files:
        # 將文件名轉換為小寫以進行副檔名匹配
        if file.lower().endswith(('.jpg', '.png', '.jpeg')):
            image_files.append(os.path.join(root, file))

# 確保資料夾內至少有指定數量的圖片可供選擇
if len(image_files) < image_count:
    raise ValueError(f"圖片數量不足，只有 {len(image_files)} 張圖片，無法選取 {image_count} 張。")

# 隨機選取指定數量的圖片
selected_images = random.sample(image_files, image_count)

# 將選定的圖片轉換成 .jpg 格式並複製到目標資料夾
for idx, image_path in enumerate(selected_images, start=1):
    # 打開圖片並轉換為RGB模式（若是PNG圖，可能含有透明通道）
    with Image.open(image_path) as img:
        img = img.convert('RGB')  # 確保轉換為JPG格式
        # 將文件保存為 .jpg 格式
        new_filename = f"{idx}.jpg"
        img.save(os.path.join(output_folder, new_filename), 'JPEG')

print(f"已選擇 {len(selected_images)} 張圖片，並將它們轉換為 .jpg 格式後保存到 {output_folder} 中。")
