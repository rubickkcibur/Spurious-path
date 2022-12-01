import os
from sys import api_version
rs = []
conf =[]
with open("pos.txt","r") as f:
    for line in f:
        line = line.strip().split()
        rs.append(line)
with open("pos_conf.txt","r") as f:
    for line in f:
        line = line.strip().split()
        conf.append(line)

better = []
worser = []
for i in range(len(rs)):
    if float(conf[i][2]) - float(rs[i][2]) > 0.4 and int(rs[i][1]) < int(conf[i][1]):
        print(i)
quit()
for i in range(len(rs)):
    if rs[i][1] < conf[i][1] and rs[i][2] < conf[i][2]:
        worser.append(i)
    if rs[i][1] > conf[i][1]:
        better.append(i)
print("worser:{}".format(worser))
print("better:{}".format(better))