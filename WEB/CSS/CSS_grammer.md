# 1. 사용방법
1. HTML의 태그<style>
    - 사용 예 
    ```
    <head>
        <style>
            a #선택자(Selector): CSS 효과를 적용하는 대상을 직접적으로 언급하지 않는다는점에서 선택자라고 한다
            { #Declaration
                coler:balck; #Property:Value
                
            }
        </style>
    </head>
    ```
2. HTML의 속성<style>
    - 사용예
    ```
    <a href="~~~" style="color:red; text-decoration:underline">
    ```

# 2. Property
효과를 준다

# 3. 선택자
## 우선순위 : id선택자 > class 선택자 > tag 선택자
- id 선택자 : #(id이름)
- class 선택자 : #(class 이름)
- tag 선택자 : #(tag 이름)

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
