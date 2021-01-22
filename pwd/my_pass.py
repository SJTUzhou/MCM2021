import sys
import threading
import datetime
import os
import subprocess
import getopt

i = 0

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
#        #self.result = self.func(*self.args)



def extractFile(password):  
    # 在这里改为cmd命令
    #fileExtr.extractall(pwd=password)
    #print('test')
    cmd = '.\\7z x 2021MCM_ProblemC_Files.rar -p'+str(password)
    #print(cmd)
    os.popen(cmd)
    #print('执行')
    return password

pwdLists = open("pwdLists1-4.txt")
startTime = datetime.datetime.now()
 
for line in pwdLists.readlines():
    Pwd = line.strip('\n')
    #t = MyThread(extractFile, (Pwd))
    t = extractFile(Pwd)
    #t.start()
    i = i + 1
    #print(line)

endTime = datetime.datetime.now()
timeSpan = endTime - startTime
print("search time:%ss" % (timeSpan.total_seconds()))