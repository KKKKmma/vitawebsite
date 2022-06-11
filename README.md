# vitawebsite
Use python3 and Vue3 to build a website

建立一個不需要會員登入的預定網站，使用者選定商品後，會跳出該商品可預訂日期，若系統中顯示無庫存，表示商品已被預訂，無法進行下一步。若是該日期商品可預訂，會進行商品保留，是否要結帳，若要結帳，則使用API串接第三方金流進行付款。付款完成，回傳資料，系統自動發送Email通知已預定完成。

# Environment
Project開始之前請先安裝virtual environment，並且利用Terminal移動到my_django_environment下使用source bin/activate啟動虛擬環境，啟動虛擬環境後，請輸入下列指令，安裝project所需要的dependencies:

```text
pip install -r requirements.txt
```


## 功能
* 前端使用Vue 3.0進行呈現
* 使用Restful API進行前後端資料傳輸，並且增刪購物車內容
* 付款完成後，發送訂單確認的電子郵件給顧客（SMTP+Gmail）
* 後台管理可以直接查看訂單、上傳商品圖片、管理商品分類、管理會員資料
* 


###  流程圖：

[Flow_chat](https://github.com/KKKKmma/vitawebsite/blob/main/flow_chat.pdf)

### 資料庫設計：


### 使用技術與工具
* 前端
  * Vue 3.0
* 後端
  * Django(3.1.7) 
    * session
    * email(SMTP+Gmail)
    * django-shopping-cart
    * django rest framwork



* 資料庫
  * MySQL

* 部署
  * Docker
  * Heroku

----
客服系統：LineBot
