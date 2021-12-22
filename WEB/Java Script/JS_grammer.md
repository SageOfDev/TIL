- html 은 정적이나 JS 는 동적이다
  즉, `1+1`을 html은 문자 그대로 출력하나 JS는 계산한 결과인 2를 출력한다

# JS을 실행하는 법
1. <script></script> 태그를 이용하여 사용한다

2. event 속성을 사용한다.
    ```<body>
        <input type="button" value="hi" onclick="alert('hi')">
    </body>
    ```
    - event는 웹 페이지 상에서 일어나는 일들을 일컫는다. 대표적으로 다음과 같은 것들이 있다.
      - `onclick` : 무언가를 선택한 경우
      - `onchange` : 내용이 변한 경우
    - event가 발생했을 때 JS를 사용하도록 HTML은 규정하고 있다.

3. console를 사용한다.
    - 이 경우는 데이터를 처리해야하는 경우 활용하기 좋다. 즉석으로 명령문을 처리하여 결과를 보여주기 때문.
      - 예를 들어 `alert("text".length)`를 사용하면 웹피이지 상의 텍스 길이를 경고창으로 알려준다.
    - 검사창-'element'창에서 `esc`를 누르면 'console' 창이 분할되어 뜬다.

# program
- program은 '순서'라는 의미가 들어있는 단어이다.
- HTML은 웹페이지를 묘사하는 목적이기에 프로그램언어가 아니다
- JavaScript는 사용자와 소통하기 위함이기에 순서를 고려한다 -> 프로그램 언어이다.

# 리팩토링
직역하면 공장으로 다시보낸다. 즉 코드를 개선시켜서 효율성을 높이는 작업

# library vs framework
## library
- 만들고자 하는 프로그램에 필요한 부품이 되는 소프트웨어
- jQuery가 가장 많이 스이고 오래되고 안정적
## framework
- 만들고자 하는 것의 기본토대를 제공한다는 느낌인듯

# UI vs API
## User Interface
## Application Programming Interface
- 애플리케이션을 만들기 위해서 프로그램이을 할 때 사용하는 조작 장치
  - 예를 들어 `alert`가 API

# 검색어 추천
- document
  
  웹페이지에 있는 어떤 태그를 삭제하고 싶거나 어떤 태그에 자식 태그를 추가하고 싶을 때
  - DOM(Docyment Object MOdel)
    document 객체에서 찾을 수 없다면 DOM까지 수색범위를 넓혀보아라

- window
  
  웹 브라우저 자체를 제어할 때

- ajax
  
  웹 페이지를 리로드 하지 않고 정보를 변경하고 싶을 때

- cookie
  
  웹 페이지가 리로드 되어도 현 상태를 유지하고 싶을 때, 사용자를 위한 개인화된 서비스를 제공할 수 있음

- offline web application
  
  인터넷이 끊겨도 동작하는 웹 페이지

- webRTC
 
  화상 통신 웹

- speech
  
  음성 인식 및 음성 정보 전달하는 웹

- webGL
  
  3차원 게임 만들고 싶을 때

- webVR
  
  가상현실 웹

