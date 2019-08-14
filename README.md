# PttDownloader
# 預覽畫面
![首页](http://vmaig.qiniudn.com/screenshot/vmaig_01.jpg)
![头像](http://vmaig.qiniudn.com/screenshot/vmaig_02.jpg)
![评论](http://vmaig.qiniudn.com/screenshot/vmaig_03.jpg)
![新闻](http://vmaig.qiniudn.com/screenshot/vmaig_news.jpg)

# 安装運行程式
安装virtualenv :

    sudo pip install virtualenv

創建和啟動虛擬環境 :

    virtualenv www
    cd www
    source bin/active

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
通过“Categories”新增要搜尋的看板
通过“Key Words”新增關鍵字搜尋
通过“Articles” 查看和操作下載好的文章


