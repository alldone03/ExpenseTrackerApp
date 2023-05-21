import os
import socket

ipawal = "192.168."
print("1. IP")
print("2. Hostname")
inputResult = input("Answer: ")
if inputResult == "1":
    while(1):
        ip = input("IP:"+ipawal)
        ret = os.system("ping -c 1 "+ipawal+ip)
        if ret != 0:
            print("IP address not responding")
            continue
        else:
            print("IP address Alive")
            print("Device Name is "+socket.gethostbyaddr(ipawal+ip)[0]+"\n")
            break

elif inputResult == "2":
    print("insert Hostname")
    hasilinput = input("Answer: ")
    print("finding")
    iplayer3 =0
    iplayer4 =0
    while(1):
        if socket.gethostbyaddr(str(ipawal)+str(iplayer3)+"."+str(iplayer4))[0] == hasilinput:
            ip = str(iplayer3)+"."+str(iplayer4)
            print("**Device Ditemukan**")
            break
        iplayer4 = iplayer4+1
        if iplayer4 >255:
            iplayer4 = 0
            iplayer3 =iplayer3+1
            print('.',end='')
            if iplayer3>255:
                print("**Device Tidak Ditemukan**")
                break
        
print("1. Pair\n2. Connect")
hasilinput = input("choose: ")
if (hasilinput == "1"):
    while(1):
        port = input("Port:")
        print(ipawal +ip+":"+port)
        print("Enter Pairing Code :")
        result  = os.popen("adb pair "+ipawal+ip+":"+port).read()
        if "Successfully" in result:
            print("**Pair Success**")
            while(1):
                port = input("Port:")
                print(ipawal +ip+":"+port)
                result = os.popen("adb connect "+ipawal+ip+":"+port).read()
                if "connected" in result:
                    print("**Connect Success**")
                    break
                else:
                    print("please input port correctly!!!")
            break
        elif "Failed" in result:
            print("Please Enter port Corretly!!")
            continue
elif (hasilinput == "2"):
    while(1):
        port = input("Port:")
        print(ipawal+ip+":"+port)
        result = os.popen("adb connect "+ipawal+ip+":"+port).read()
        if "connected" in result:
            break
        else:
            print("please input port correctly!!!")

