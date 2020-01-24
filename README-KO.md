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
> pip install requests
> pip install beautifulsoup4
```
4. 사용 방법
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
`-n directory` 옵션을 사용하면 특정한 폴더에 저장 가능합니다. 기본 옵션은 `\bcydownload` 입니다.
`-d`, `--date` 옵션을 사용하면 폴더 저장 시 날짜를 같이 저장합니다.

> `Python bcy_single_climber.py bcy_post_link`
> `Python bcy_user_climber.py bcy_user_link`

위 두 단일 스크립트는 특정 유저/포스트를 저장하는 스크립트로 무조건 `\bcydownload` 에 저장됩니다. 

三.알려진 문제
-----

`나도 몰라`

-----
Enjoy

