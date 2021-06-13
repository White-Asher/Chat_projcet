import socket   # 소켓을 사용하기 위해 socket을 import함
import threading    # 송신, 수신 쓰레드 분리하기 위해 threading을 import함

HOST = '192.168.35.242' # 연결할 서버 주소 입력
PORT = 9998 # 소켓 통신할 포트 입력

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 클라이언스 소켓 생성 (첫번째 인자: 패밀리(주소체계:IPv4), 두번째인자: 소켓타입(스트림소켓))
cs.connect((HOST, PORT)) # 생성된 클라이언트 소켓함수에 (호스트와, 포트값 정보 입력)
print("서버에 연결되었습니다.")

def send_function(client_socket): # 메세지 전송
    while True: # 무한 반복문
        send_message = input() # 클라이언트 사용자 메세지 입력
        client_socket.send(send_message.encode()) # 클라이언트 소켓으로 메세지 전달

def receive_function(client_socket): # 메세지 수신
    while True: # 무한 반복문
        recv_message = client_socket.recv(2048) # 다른 클라이언트가 전송한 메세지를 받음 (서버에서 전송)
        print(recv_message.decode()) # 메세지 전송한 클라이언트 번호, 메세지 출력

send_message_thread = threading.Thread(target=send_function, args=(cs, )) # 메세지 전송 전용 쓰레드 생성
send_message_thread.start() # 메세지 송신 쓰레드 시작

receive_message_thread = threading.Thread(target=receive_function, args=(cs, )) # 메세지 수신 전용 쓰레드 생성
receive_message_thread.start() # 메세지 수신 쓰레드 시작

