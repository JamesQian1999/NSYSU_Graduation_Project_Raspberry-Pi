import os

i = os.popen("ifconfig | egrep -o 'inet [0-9]+\.[0-9]+\.[0-9]+\.[0-9]+ ' | sed 's/inet 127.0.0.1//g' | tr '\n' ' '| sed 's/inet //g'")
i = i.read()
i = "rtsp://"+i[:-4]+":8555/unicast"
print("\n\033[32mSent:\033[m\t\t",i)

# from bluetooth import *
# import subprocess

# server_sock=BluetoothSocket( RFCOMM )
# server_sock.bind(("",PORT_ANY))
# server_sock.listen(1)

# port = server_sock.getsockname()[1]

# uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

# advertise_service( server_sock, "SampleServer",
#                    service_id = uuid,
#                    service_classes = [ uuid, SERIAL_PORT_CLASS ],
#                    profiles = [ SERIAL_PORT_PROFILE ])

# print("Waiting for connection on RFCOMM channel %d" % port)

# client_sock, client_info = server_sock.accept()

# print("Accepted connection from ", client_info)

# #this part will try to get something form the client
# # you are missing this part - please see it's an endlees loop!!
# try:
#     data = client_sock.recv(1024)
#     client_sock.send("ACK")
#     while True:
#         data = client_sock.recv(1024)
#         if len(data) == 0: break
#         print("received [%s]" % data)

# # raise an exception if there was any error
# except IOError:
#     pass

# print("disconnected")

# client_sock.close()
# server_sock.close()