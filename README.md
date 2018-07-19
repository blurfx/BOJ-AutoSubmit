# BOJ-AutoSubmit
자동으로 백준 온라인 저지에 소스 코드를 제출해주는 봇

## 의존성
- Python 3.x
- Selenium
- ChromeDriver

## 사용법
0. `pip install -r requirements.txt`
1. [ChromeDriver](http://chromedriver.chromium.org/downloads)를 다운받아 압축을 해제 한 뒤 소스 코드의 루트 폴더에 chromedriver.exe를 위치시켜줍니다.
2. app.py에서 자동으로 제출할 데이터를 생성하는 로직을 작성한 뒤 실행시킵니다.
3. PROFIT!

기본적으로 *[10948번 Daily 로또](https://www.acmicpc.net/problem/10948)* 문제를 자동으로 제출하는 코드가 작성되어 있습니다.