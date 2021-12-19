# 1. 사용방법
1. HTML의 태그 `<style>`
    - 사용 예 
    ```
    <head>
        <style>
            a #선택자(Selector): CSS 효과를 적용하는 대상을 직접적으로 언급한다는점에서 선택자라고 한다
            { #Declaration
                coler:balck; #Property:Value
                
            }
        </style>
    </head>
    ```
2. HTML의 속성`<style>`
    - 사용예
    ```
    <a href="~~~" style="color:red; text-decoration:underline">
    ```

# 2. Property
효과를 준다

# 3. 선택자
## 우선순위 : id선택자 > class 선택자 > tag 선택자
- id 선택자 : #(id이름)
- class 선택자 : .(class 이름)
- tag 선택자 : (tag 이름)

왜 그럴까? 
- HTML에선 id 값은 단 한 개의 태그에서만 등장해야한다.
- 구체적인 것이 더욱 우선순위 높도록 만들었음

# 3. box model
google image 검색에서 "css box model"
```
h1{
                border:5px red solid;
                padding:20px;
                margin:20px;
                display:block;
                width:100px;
                }
```

# 4. grid

## caniuse.com
CSS HTML JavaScript 의 기술을 인터넷 브라우저들이 지원하는지 통계를 보여줌. 중요한 사이트.

# 5. 반응형 웹(responsive web), MediaQuery
다양한 기기(화면)에서 반응하도록 만들어야 함.
"화면에 크기에 따라서 웹 페이지의 각요소들이 반응해서 동작하게 하는 것"

# 6. Caching(캐싱)
캐싱이란 저장하다는 뜻.
한 번 style.css를 받았다면 웹브라우저는 계속해서 클라이언트 컴퓨터에 저장해두어서 필요할때마다 부른다.
- 클라이언트들은 속도를 높인다.
- 사업자들은 네트워크 트래픽을 줄여서 돈을 절약할 수 있다.
따라서 중복되는 CSS 꺼내서 별도의 파일로 저장하여 `<link>` 을 하는 것이 좋다.
