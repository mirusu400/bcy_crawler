# bcy_crawler
## 프로젝트 소개
一.파일 안내
-----
1. `threading_control.py`
        이미지 다운로드 스레드 관리 
2. `bcy_single_climber.py`
        bcy.net/item/detail/{ID} 형식의 단일 URL 이미지 다운로드
3. `bcy_user_climber.py`
        bcy.net/u/{UID} 형식의 사용자 URL에 대한 모든 이미지 다운로드
4. `bcy_crawler_main.py`
        bcy_crawler 에 대한 메인 실행 스크립트

二.사용 방법
-----
1. Python 버전

>>       Python 3.x

2. OS 버전

>>       Windowns, Mac OS, Linux

3. 필요 패키지

>>       BeautifulSoup, requests

```bash
> pip3 install requests
> pip3 install beautifulsoup4
```
4. 사용 방법
> `Python3 bcy_crawler_main.py bcy_user_or_post_link [-d directory]`

-d directory 옵션을 사용하지 않으면 저절로 `\bcydownload` 에 저장됩니다.

> `Python3 bcy_single_climber.py bcy_post_link`

> `Python3 bcy_user_climber.py bcy_user_link`

위 두 단일 스크립트는 무조건 `\bcydownload` 에 저장됩니다. 

三.알려진 문제
-----
나도 몰라

Enjoy
-----







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
> `Python3 bcy_single_climber.py`

三.已知问题
-----
        `暂不明确`

Enjoy
-----
