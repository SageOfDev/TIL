'''
https://www.youtube.com/watch?v=yQ20jZwDjTE
9. User Agent  보다 말음

https://www.whatismybrowser.com/detect/what-is-my-user-agent
접속하는 브라우저마다 Uset Agent가 다름
'''
import requests
url = "https://www.zara.com/kr/ko/%ED%8F%AC%EC%BC%93-%EA%B0%80%EB%94%94%EA%B1%B4-p00077306.html?v1=139867711&v2=2011851"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("myZara.html", 'w', encoding="utf8") as f:
    f.write(res.text)