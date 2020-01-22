# 收聽台北愛樂網路廣播


## 檔案說明

- `FM997_onAir.xspf` : 台北愛樂廣播電台

- `FM997_Jazz.xspf` : Jazz 頻道電台

- `FM997_OBG.xspf` : OBG 頻道電台

- `update_token.py` : 更新上述檔案的 token 及 expires 資訊

## 使用方法

1. 從 CLI
    $ cvlc FM997_onAir.xspf
   或
    $ vlc FM997_onAir.xspf
   或從圖形界面中雙擊 xspf 檔案圖示。

2. 若出現錯誤訊息無法收聽，則執行 `update_token.py` 更新 `.xspf` 檔案內容後，再嘗試前一步驟。
