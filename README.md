# PttDownloader
# 预览
![首页](http://vmaig.qiniudn.com/screenshot/vmaig_01.jpg)
![头像](http://vmaig.qiniudn.com/screenshot/vmaig_02.jpg)
![评论](http://vmaig.qiniudn.com/screenshot/vmaig_03.jpg)
![新闻](http://vmaig.qiniudn.com/screenshot/vmaig_news.jpg)

# 安装运行
安装virtualenv :

    sudo pip install virtualenv

创建并激活虚拟环境 :

    virtualenv www
    cd www
    source bin/active

下载代码,切换目录 :
    
    git clone https://github.com/skyjan0428/PttDownloader.git
    cd vmaig_blog

然后 :

    pip install -r requirements.txt


```

初始化数据库 :

    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    
啟動server :
    
    python manage.py runserver
    

新增Superuser :
    
    python manage.py createsuperuser
    

	
啟動server後，请登录 http://your-domain/admin，帳密是剛剛新增的super user帳號密碼                   

# 接下来该干什么？
在浏览器中输入 http://127.0.0.1:8000/admin  
输入前面初始化数据库时的用户名密码。  
后台中，可以  
通过“Categories”新增要搜尋的看板
通过“Key Words”新增關鍵字搜尋
通过“Articles” 查看和操作下載好的文章


