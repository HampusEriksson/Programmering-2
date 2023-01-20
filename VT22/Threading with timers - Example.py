import threading

def t1():
  threading.Timer(1, t1).start ()
  print ("Every second")

def t2():
  threading.Timer(3, t2).start ()
  print ("Every three second")



t1()
t2()