import socket         # 소켓을 사용하기 위해 socket을 import함
import threading      # 송신, 수신 쓰레드 분리하기 위해 threading을 import함
import pymysql        # 파이썬에 mysql을 사용하기 위해 사용
import datetime       # 현재 시간을 출력하기 위해 사용

# 현재시간 출력함수
def Current_Time():
    now = datetime.datetime.now()                             # datetime 오브젝트의 now() 메서드를 사용해 현재 시간을 가져옴
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')           # datetime 오브젝트의 strftime() 메서드를 사용해 연,월,일 시,분,초 형식으로 변환함
    return nowDatetime                                        # 변환된 시간 결과값을 return 함

# DB에 데이터 입력을 실행하는 함수 
def SQL_Input_Function(SQL_Input_Address, SQL_Input_Message): # 인자값 받음 (주소, 메세지)
    conn = pymysql.connect(host='', user='', password='', db='chatproject', port=, charset='utf8')
                                                              # 기존에 생성한 DB에 접속하기 위한 구문
    cur = conn.cursor()                                       # 접속한 DB에 상호작용하기 위한 구문
    cur.execute("INSERT INTO chat_table (time_log, user_addr, message) VALUES (%s, %s, %s)",(Current_Time(), SQL_Input_Address, SQL_Input_Message ))
                                                              # excute 메서드를 이용해 INSERT쿼리를 실행 
                                                              # chat_table이름의 table 에 현재시간, 주소, 메세지 입력
    conn.commit()                                             # DB에 반영하기 위해 commit 선언
    cur.close()                                               # DB 연결 종료
    conn.close()                                              # DB 연결 종료

# connecting_client 함수는 서버에서 accept가 되면 생성되는 socket 인스턴스를 통해 client로 부터 데이터를 받으면 재송신하는 메소드이다.
def connecting_client(client_socket, client_addr):                     # cs, addr = ss.accept() 에서 클라이언트 소켓, 주소 인자 전달 받음
    print(Current_Time(),':',client_addr[0],"가 연결되었습니다.")       # 서버 터미널에 해당 클라이언트 연결 기록 출력
    SQL_Input_Function(client_addr[0],"Client-Connect")                # 클라이언트 연결기록 DB에 입력

    # try except 문을 이용한 예외처리
    try:
        # 접속 상태에서 클라이언트로 부터 받을 데이터를 무한정 대기한다.
        # 만약 접속이 끊기게 된다면 except가 발생해서 접속이 끊기게 되며 소켓이 닫힌다.
        while True:
            send_message = client_socket.recv(2048)                # 2048 byte까지 크기의 보낼 메세지를 클라이언트 소켓을 통해 받음
            if send_message:                                       # 보낼 메세지가 있다면 조건문 실행
                for x in All_clients:                              # 접속된 모든 클라이언트들을 지정함
                    if x != client_socket:                         # 서버로 메세지를 전송한 해당 클라이언트에게 다시 메세지를 보내지 않음
                        add_address_message = Current_Time() +' ('+ client_addr[0] +'): '+ send_message.decode()
                                                                   # 다른 클라이언트에게 [시간 (메세지 보낸 클라이언트): 메세지] 형태로 전송하기 위해 구문 작성
                        try:
                            x.send(add_address_message.encode())   # 다른 클라이언트에게 시간, 클라이언트, 메세지 로 보내기 위해 decode한 것을 다시 encode하여 전송
                            Current_Time()                         # 현재 시간 함수 실행
                            SQL_Input_Function(client_addr[0],send_message.decode())
                                                                   # DB에 메세지를 전송한 클라이언트 주소와 메세지를 저장하기 위한 구문
                        except:
                            pass 

    #except 구문 발생시 print문 출력
    except: 
        print(Current_Time(),':',client_addr[0],"가 접속 해제 되었습니다.")  # 클라이언트 접속 해제시 서버 터미널에 시간, 클라이언트 접속해제 구문 출력
        SQL_Input_Function(client_addr[0],"Client-Disconnect")             # DB에 접속 해제된 클라이언트 주소, Client_Disconnect구문 입력

    # 오류 발생여부 상관 없이 무조건 실행되는 코드
    finally: 
        client_socket.close() # 클라이언트 소켓 닫음.

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # 소켓 생성 (첫번째 인자: 패밀리(주소체계:IPv4), 두번째인자: 소켓타입(스트림소켓))
ss.bind(('', 9998))                                       # 수신 받을 모든 IP 와 9998 포트로 받겠다는 의미
ss.listen()                                               # 클라이언트 수신 받음 (클라이언트 접속수 무제한으로 설정)
All_clients = []                                          # 클라이언트 목록 리스트
server_local_host = ""                      # 서버 주소

# 서버 코드 실행시 동작되는 함수
try:
    print(Current_Time() ,"서버가 실행되었습니다")          # 서버 터미널에 현재시간, 서버실행 문구 출력
    SQL_Input_Function(server_local_host, "Server-Start") # 처음 서버 실행시 DB에 Server-start문구 입력
                                                    
    # 서버는 다중 클라이언트를 받기 때문에 while True문으로 무한 루프를 사용한다.
    # client가 서버로 접속 하면 accept가 발생.
    # client 소켓과 주소를 튜플 자료형으로 받는다.
    while True:
        cs, addr = ss.accept()            # 쓰레드를 이용해 client 접속 대기를 만든 후, accept로 넘어가서 다른 client를 대기한다.
        All_clients.append(cs)            # accept시 클라이언트 소켓에 마지막으로 접속된 클라이언트를 추가함
        len(All_clients)                  # 동일 주소 클라이언트 접속 시 중복 주소값 입력을 제거
        chat_thread = threading.Thread(target=connecting_client, args=(cs, addr))
                                          # 스레드를 사용하기 위한 threading 모듈의 Thread()함수 이용
                                          # connecting_client 함수를 Thread함수의 target 아규먼트로 지정한다.
                                          # 클라이언트 소켓(cs), 클라이언트 주소 를 인자로 전달 (튜플형으로)
        chat_thread.start()               # 스레드 실행

# 코드 실행시 에러 발생하면 print문 출력 후 코드 종료
except:  
    print("에러발생!") 

# 오류 발생여부 상관 없이 무조건 실행되는 코드
finally:
    ss.close()   # 서버 소켓을 닫음
