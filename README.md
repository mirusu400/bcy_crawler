# bcy_crawler
**[한글 README](README-KO.md)**
## 项目简介
一.文件简介
-----
1. `threading_control.py`
        多线程数目控制,用于控制下载线程数目
2. `bcy_single_climber.py`
        半次元单界面爬虫,能够爬取但界面的所有图片
3. `bcy_user_climber.py`
        半次元用户爬虫,能够爬取某用户的所有作品

二.使用方法
-----
1. Python版本

>>       Python 3.x

2. 系统版本

>>       Windowns, Mac OS, Linux

3. 依赖库

>>       BeautifulSoup, requests

```bash
> pip3 install requests
> pip3 install beautifulsoup4
```
4. 使用方法
```
usage: bcy_crawler_main.py [-h] [-n directory] [-d] Link

Download images from bcy.net.

positional arguments:
  Link          Link of user or Link of post

optional arguments:
  -h, --help    show this help message and exit
  -n directory  Set path to save
  -d, --date    Use it if you need download with date.
```

> `Python bcy_single_climber.py bcy_post_link`
> `Python bcy_user_climber.py bcy_user_link`

三.已知问题
-----
        `暂不明确`

Enjoy
-----
