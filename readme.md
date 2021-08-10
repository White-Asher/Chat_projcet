## 1\. 프로젝트 개요

**소켓통신, 다중 스레드를 이용한 단일 서버, 멀티 클라이언트 실시간 채팅 프로그램 구현**

1.  Server는 Client의 메시지를 받아 각 클라이언트들에게 전달한다.
2.  다수의 Client가 동시에 통신하여 실시간 채팅을 할 수 있다.
3.  Client는 메시지를 여러 번 보낼 수 있다.
4.  Client의 시간, 주소, 메세지를 DB에 저장한다.
5.  저장된 DB를 Bitnami(APM)를 통해 외부 IP의 웹페이지에서 조회할 수 있다.

## 2\. 구성언어, 환경

-   Python (Server, Client)
-   SQL (Raspberry pi MariaDB)
-   html, CSS, JS, ajax (WEB)
-   Apache2(WEB server)

## 3\. 구조

![image](https://user-images.githubusercontent.com/55140122/128791916-ff580eb1-ad12-4c8f-a07a-6ab68cd9f72c.png)

![image](https://user-images.githubusercontent.com/55140122/128791954-d8aae75f-2dcd-4f5b-8521-a582d66c744d.png)
## 4\. 실행 결과

#### 서버

![image](https://user-images.githubusercontent.com/55140122/128791972-5166286e-8045-40cf-b138-6413f3ce187b.png)

#### DB

![image](https://user-images.githubusercontent.com/55140122/128791996-bf809844-22ca-4d00-83cc-144d6753a4f3.png)

#### Client1

![image](https://user-images.githubusercontent.com/55140122/128792021-6f06da2c-de8d-4d89-9adf-a6522b48a75d.png)
![image](https://user-images.githubusercontent.com/55140122/128792082-20a43e13-d474-43f9-9d18-cc5c7abf19ed.png)

#### Client2

![image](https://user-images.githubusercontent.com/55140122/128792127-0e81119d-dc87-45a5-8656-fdbd5f96ae83.png)

#### Client3

![image](https://user-images.githubusercontent.com/55140122/128792133-7aee6479-9a84-460a-91cf-f3887f06a29b.png)


#### WEB

![image](https://user-images.githubusercontent.com/55140122/128792149-7fa8d0d0-57ef-4921-9b94-95b5f7fca4dc.png)