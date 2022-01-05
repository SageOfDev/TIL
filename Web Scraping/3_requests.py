import requests
res = requests.get("https://google.com")
#res = requests.get("https://naver.com")
# res = requests.get("https://www.zara.com/kr/ko/%ED%8F%AC%EC%BC%93-%EA%B0%80%EB%94%94%EA%B1%B4-p00077306.html?v1=139867711&v2=2011851")
res.raise_for_status()
# print("응답코드 :", res.status_code)

#if res.status_code == requests.codes.ok:
#    print('정상입니다.')
#else:
#    print("문제가 생겼습니다. [에러코드 ", res.status_code,"]")

print(len(res.text))
print(res.text)

with open("mygooogle.html", 'w', encoding="utf8") as f:
    f.write(res.text)