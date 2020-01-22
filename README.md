# 收聽台北愛樂網路廣播


## 檔案說明

- `FM997_onAir.xspf` : 台北愛樂廣播電台

- `FM997_Jazz.xspf` : Jazz 頻道電台

- `FM997_OBG.xspf` : OBG 頻道電台

- `update_token.py` : 更新上述檔案的 token 及 expires 資訊

## 使用方法

1. 從 CLI 執行以下命令
```$ cvlc FM997_onAir.xspf```
 or 
```$ vlc FM997_onAir.xspf```
 or 
dobule click `.xspf` icon from file manager in the GUI.

2. 若出現錯誤訊息無法收聽，則執行 `update_token.py` 更新 `.xspf` 檔案內容後，再嘗試前一步驟。
