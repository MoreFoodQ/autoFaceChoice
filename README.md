# **自動圖片篩選與分類工具**

## **專案概述**
本工具旨在自動化圖片的隨機篩選、格式轉換與臉部辨識分類，適合處理大量圖片資料池。透過多階段的處理流程，能快速完成圖片的篩選與分類，並支援資料夾清理功能。

---

## **功能特色**
1. **隨機篩選圖片**：從資料池中隨機選取指定數量的圖片。
2. **圖片格式轉換**：自動將圖片統一轉換為 JPG 格式。
3. **臉部辨識分類**：
   - 單人臉（one_face）
   - 多人臉（multiple_faces）
   - 無人臉（no_face）
4. **清理功能**：
   - 清空篩選資料夾。
   - 刪除資料夾內非圖片檔案。

---

## **資料夾結構**
```plaintext
project/
│
├── sourceFolder/          # 圖片資料池，放置大量圖片
├── choiceFolder/          # 隨機篩選出的圖片及分類結果
│   ├── one_face/          # 單人臉圖片
│   ├── multiple_faces/    # 多人臉圖片
│   ├── no_face/           # 無人臉圖片
├── scripts/               # 程式碼檔案
│   ├── flow.py            # 主流程控制程式
│   ├── cleanChoice.py     # 清空篩選資料夾
│   ├── randomChoice.py    # 隨機篩選與格式轉換
│   ├── faceTracker.py     # 臉部辨識與分類
│   ├── cleanUp.py         # 清除資料夾內非圖片檔案
│   ├── requirements.txt   # 相依套件清單
├── README.md              # 本文件
```

---

## **安裝步驟**
1. **克隆專案**
   ```bash
   git clone https://github.com/MoreFoodQ/autoFaceChoice
   cd project/
   ```

2. **安裝相依套件**
   使用 `requirements.txt` 安裝所需的 Python 套件：
   ```bash
   pip install -r scripts/requirements.txt
   ```

   - **套件清單**：
     - `face_recognition`：臉部辨識功能。
     - `Pillow`：圖片格式轉換。

3. **準備資料夾**
   - 在 `sourceFolder` 中放置大量圖片作為資料池。
   - 確保 `choiceFolder` 存在，程式會自動建立所需的分類子資料夾。

---

## **使用方式**
### **1. 主流程執行**
執行 `flow.py`，自動完成以下步驟：
1. 清空篩選資料夾。
2. 隨機篩選圖片並轉換格式。
3. 將圖片分類為單人臉、多臉與無臉。

```bash
python scripts/flow.py
```

### **2. 清空篩選資料夾**
如需重新篩選圖片，手動執行清空程式：
```bash
python scripts/cleanChoice.py
```

### **3. 刪除非圖片檔案**
清理資料池中的非圖片檔案，確保資料夾內只保留有效圖片：
```bash
python scripts/cleanUp.py
```

---

## **執行流程詳解**
1. **初始化資料夾**：
   - 清除 `choiceFolder` 資料夾內的舊檔案。
2. **隨機篩選與格式轉換**：
   - 從 `sourceFolder` 中隨機選取圖片，轉換為 JPG 格式後存入 `choiceFolder`。
3. **臉部辨識與分類**：
   - 將篩選出的圖片分類為 `one_face`、`multiple_faces` 和 `no_face`。
4. **檢視結果**：
   - 完成後，檢查 `choiceFolder` 資料夾內的分類結果。

---

## **注意事項**
1. **臉部辨識需求**：
   - `face_recognition` 需要安裝 `dlib`，若安裝失敗，請確認開發環境支援。
2. **圖片格式要求**：
   - 原始圖片應為常見格式（如 JPG、PNG、JPEG）。
3. **處理效能**：
   - 大量圖片可能耗時，建議使用高效能設備運行。


