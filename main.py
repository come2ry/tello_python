import socket
import time

class Command():
    start = 'command'.encode('utf-8')
    takeoff = 'takeoff'.encode('utf-8')
    land = 'land'.encode('utf-8')

tello_ip = '192.168.10.1'
tello_port = 8889

#udpソケット作成
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = (tello_ip , tello_port)

#コマンドモードを使うため'command'というテキストを投げる
socket.sendto(Command.start, tello_address)
#5秒まつ
time.sleep(5)

#離陸のため'takeoff'というテキストを投げる
socket.sendto(Command.takeoff, tello_address)
#5秒まつ
time.sleep(5)

#着陸のため'land'というテキストを投げる
socket.sendto(Command.land, tello_address)