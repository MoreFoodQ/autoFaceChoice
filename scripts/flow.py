import subprocess

# 定義你要執行的三個 .py 程式路徑
script1 = r'?:\?\cleanChoice.py' #將?替換為對應的資料夾路徑
script2 = r'?:\?\randomChoice.py'
script3 = r'?:\?\faceTracker.py'

# 順序執行每個腳本
try:
    # 執行第一個腳本
    print("正在初始化資料夾(清除檔案)...")
    subprocess.run(["python", script1], check=True)
    
    # 執行第二個腳本
    print("正在隨機挑選圖片")
    subprocess.run(["python", script2], check=True)

    # 執行第三個腳本
    print("正在辨識圖片人物是否存在並分類資料夾")
    subprocess.run(["python", script3], check=True)

    print("執行完成，請檢閱資料夾進行最後的人工確認")

except subprocess.CalledProcessError as e:
    print(f"腳本執行失敗: {e}")
