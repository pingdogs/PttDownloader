# PttDownloader
功能: PttDownloader會依照關鍵字去相應的看板去抓有關鍵字出現的文章並存到資料庫，預設是每小時抓一次，每次每個關鍵字去對應的看板上找最新的200則文章比對，若出現關鍵字則保留，若為上次重複文章則更新內文。

# 預覽畫面
![首页](https://github.com/skyjan0428/PttDownloader/blob/master/static/images/home.png)
![文章畫面](https://github.com/skyjan0428/PttDownloader/blob/master/static/images/article_content.png)

Demo網址: http://13.72.110.87/

# 安装運行程式
安装virtualenv :

    sudo pip install virtualenv

創建和啟動虛擬環境 :

    virtualenv www
    cd www
    source bin/activate

下載程式碼 :
    
    git clone https://github.com/skyjan0428/PttDownloader.git
    cd PttDownloader

安裝用到的python library :

    pip install -r requirements.txt


```

初始化資料庫 :

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    
啟動server :
    
    python manage.py runserver
    

新增Super User :
    
    python manage.py createsuperuser
    

	
啟動server後，请登录 http://your-domain/admin，帳密是剛剛新增的Super User帳號密碼                   

# 接下来該做什麼？
在瀏覽器輸入 http://127.0.0.1:8000/admin  
输入前面初始化資料庫时的帳號密碼。  
後台中，可以  
通過“Categories”新增要搜尋的看板
通過“Key Words”新增關鍵字搜尋
通過“Articles” 查看和操作下載好的文章

Settings.py 可以設定要多久下載一次文章




