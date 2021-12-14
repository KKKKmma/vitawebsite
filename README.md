# vitawebsite
Use python3 and Vue3 to build a website

建立一個不需要會員登入的預定網站，使用者選定商品後，會跳出該商品可預訂日期，若系統中顯示無庫存，表示商品已被預訂，無法進行下一步。若是該日期商品可預訂，會進行商品保留，是否要結帳，若要結帳，則使用API串接第三方金流進行付款。付款完成，回傳資料，系統自動發送Email通知已預定完成。

# Environment
Project開始之前請先安裝virtual environment，並且利用Terminal移動到my_django_environment下使用source bin/activate啟動虛擬環境，啟動虛擬環境後，請輸入下列指令，安裝project所需要的dependencies:

```text
pip install -r requirements.txt
```


## 前後端接口
使用django restframework進行前後端資料傳輸


###  流程圖：


### 資料庫設計：


