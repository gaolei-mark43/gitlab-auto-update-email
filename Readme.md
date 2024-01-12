# 项目名称

自动更新新用户的邮箱

## 项目简介

1.使用get_user.py 通过gitlab接口查询并筛选出所有新用户列表写入文件
2.使用auto_update_email.py调用浏览器页面操作自动修改邮箱
3.使用auto_run.py实现定时十分钟执行上述脚本代码

## 安装

1.火狐浏览器更新最新版本
2.安装火狐浏览器驱动
3.安装packages目录中的py依赖包

## 使用方法

site-packages.zip需要解压到Lib\site-packages目录中，过程确实的包请解压packages.zip（任意目录），进入packages目录，pip install 对应包名称的.whl文件即可
上述依赖安装完毕后，pycharm打开项目，执行auto_run.py即可