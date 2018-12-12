# import threading, time
#  
# class myThread(threading.Thread):
#     def __init__(self,name,counter):
#         threading.Thread.__init__(self)
#         self.name = name 
#         self.counter = counter
#          
#     def run(self):
#         print_time(self.name, self.counter)
#  
#  
# def print_time(threadName, counter):
#     while counter:
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         time.sleep(2)
# #         print(threadName)
#         counter -=1 
#              
# thread1 = myThread("Somil",3)
# thread2 = myThread("Amit",2)
#  
#  
# thread1.start()
# thread2.start() 
#  
# threads = []
# threads.append(thread1)
# threads.append(thread2)
#  
# for thread in threads:
#     thread.join()
# print ("Exiting Main thread")




# val = input("Enter here")
# print (val, type(val))
# print (val + "somil")



# print(5/2)
# print(5//2)
# print(5./2)
# print(5.//2)

# print (10%7)



import threading, time
 
# class myThread(threading.Thread):
#     def __init__(self,name,counter):
#         threading.Thread.__init__(self)
#         self.name = name 
#         self.counter = counter
#          
#     def run(self):
#         threadLock.acquire()
#         print_time(self.name, self.counter)
#         threadLock.release()
#  
# def print_time(threadName, counter):
#     while counter:
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         time.sleep(2)
# #         print(threadName)
#         counter -=1 
#  
# threadLock = threading.Lock()
#             
# thread1 = myThread("Somil",3)
# thread2 = myThread("Amit",2)
#  
#  
# thread1.start()
# thread2.start() 
#  
# threads = []
# threads.append(thread1)
# threads.append(thread2)
#  
# for thread in threads:
#     thread.join()
# print ("Exiting Main thread")


# import webbrowser 
# webbrowser.open("https://www.google.com")




# import socket 
# s = socket.socket() 
# host = socket.gethostname()
# print (host)
# 
# ip = socket.gethostbyname(host)
# print(ip)


# import re 
# # ip = "10.78.184.168" 
# with open('IP.txt') as f1:
#     data = f1.read()
# #     print(data, type(data))
# 
# # patt = "^\d{1,3}[1-5]\.\d{1,3}[1-5]\.\d{1,3}[1-5]\.\d{1,3}[1-5]$"
# # patt = "([0-9]|[1-9][0-9]|1[0-9]|2[0-5]\.$)" * 4 
# 
# #patt = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?(\.|$))'
# patt = r'\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?(\.|$)){4}\b'
# # print(patt)
# m = re.finditer(patt,data)
# print (m)
# # if m:
# #     print(m.group(0))
# # parts = ip.split('.')
# # if len(parts)==4 and 
# #     
# 
# 
# #1-255 
# 
# # 255-200  ----2[0-5]{3}
# # 199-100-----1[0-9]{3}
# # 99-10---[1-9][0-9]{2}
# # 9-0----- [0-9]{1}
# 
# # 255-200  ----2[0-5]{3}
# # 199-100-----1[0-9]{3}
# # 99-10---[1-9][0-9]{2}
# # 9-0----- [0-9]{1}
# # 
# # 
# # 192.255.10.1


# import re 
# patt = "\w+\@\w+"
# data = "somi@gmail.com"
# print(re.match(patt,data))



# for i in range(10):
#     print(i)

# s = range(10)
# print (s)
# print(list(s))


# key_value ={} 
# key_value[2] = 56       
# key_value[1] = 2 
# key_value[5] = 12 
# key_value[4] = 24
# key_value[6] = 18      
# key_value[3] = 323
# 
# for i in sorted (key_value.keys()) :  
#      print(i, end = " ") 



# val =  (lambda x,y:x*y)(5,6)
# print (val)


# s = []
# print (all(s))


# roll_no = [ 4, 1, 3, 2 ,3] 
# marks = [ 40, 50, 60, 70 ]
# print (list(zip(roll_no,marks)))




# val = input("Enter the number here")
# temp = []
# for i in range(val):
#     print (i) 
# #     if val % i == 0:
# #         temp.append(i)
# # print(temp)


# import hashlib 
# str = "GeeksforGeeks"
# print(str.encode)
# print (hashlib.algorithms_guaranteed)
# print (hashlib.sha256(str.encode()))



# print (chr(400))



# s = [2,3,5,1,4]
# temp = []
# while s:
#     min = s[0]
#     for i in s:
#         if i < min:
#             min = i 
#     temp.append(min)
#     s.remove(min)
# print(temp)


# n = int(input("Enter the number here"))
# temp = []
# for i in range(2,n):
#     if n%i == 0:
#         temp.append(i)
# print(temp)

# from itertools import combinations
# s = [1,2,3,4,5,6]
# temp = [] 



# import re 
# # patt = "\w+\@\w+"
# patt = "\w+[._]?\w+\@\w+(.)(com|adu|edu|in)$"
# # email = "a_mit.kumar@cisco.comm"
# email = "a_mit.kumar@cisco.in"
# m=  (re.match(patt,email))
# if m:
#     print (m.group(0))



# import re 
# date = "00/"
# # patt = r"(3[01]|[012][0-9])" 
# patt = r"(3[01]|[012][0-9])(/)" 
# 
# m = (re.search(patt,date))
# print (m.group(0))
# print (m.group(1))
# print (m.group(2))


# import re 
# patt = "(20[0-9][0-9]){4}"
# data = "2018201820182018"
# m = re.search(patt,data)
# if m:
#     print(m.group(0))

# import itertools
# from itertools import combinations
# s = [1,2,3,4]
# for i in range(1,len(s)):
#     print("value>>>", i)
#     print (list(itertools.combinations(s,i)))

# s = [1,2,3,4,5,6]
# print([x for x in s if x%2==0])
# print(s)



# import os 
# print(os.getcwd())

# import hashlib 
# # print (hashlib.md5('hash.txt').hexdigest())
# s = hashlib.md5(open('hash.txt','rb').read()).hexdigest()
# print(s)



# from collections import defaultdict 
# 
# def defaultvalue():
#     return 0 
# 
# otherdict = defaultdict(defaultvalue)
# otherdict['a']=1
# otherdict['b']=2
# print(otherdict)
# print(otherdict['d'])


# 
# import zipfile, os 
# files = zipfile.ZipFile('Dummy.zip')
# content = files.namelist()
# print(content)


# import zipfile,os 
# newzip= zipfile.ZipFile('new.zip', 'w')
# newzip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# newzip.close()

# a = 5
# # exec('a=47')
# print (eval('a *48'))
# print(a)

# def func():
#     print (5*5) 
#     
# f1 = func()
# exec(f1)


# s1 = "somil"
# s2 = s1 
# s1[0]='T'
# print (s1, s2)
# print (id(s1), id(s2))



# s = set([1,4,3,1,2,4])
# s1 = s 
# s1 |=set([5,6,7])
# print(s1)
# print(s)


# import os 
# print(os.getcwd())
# src = "C:\Users\somijain\py3_workspace\py3learning"
# dst = "C:\Users\somijain"
# os.symlink(src, dst)


# print("i am a {} yeards old boy of {} working in {})".format(29,'wipro','Bangalore'))


import os 
print(os.getcwd())




