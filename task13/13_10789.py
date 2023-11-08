from ipaddress import *

cnt = 0
for i in range(32):
    ip = ip_network(f"203.75.227.102/{i}", 0)
    s_ip = str(ip).split("/")[0]
    if s_ip == "203.75.224.0":
        cnt += 1

print(cnt)