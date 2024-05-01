import os
o2 = []
o3 = []
o5 = []
def mains():
  global data1
  global track
  global heshd
  heshd= input("Type Data : ").lower()
  track = str(input("Type Number : "))
  data1 = []
  for i in heshd:
    if i in "1,2,3,4,5,6,7,8,9,0":
      data1.append(1)
def saver():
  mains()
  if track == "2":
    print(track ,"Saved")
    o2.append(1)
    o3.clear()
    o5.clear()
    if len(o2) >= 4:
      print("3/5")
  elif track == "3":
    o3.append(1)
    print(o3)
    o2.clear()
    o5.clear()
    if len(o3) >= 4:
      print("2/5")
  elif track == "5":
    o5.append(1)
    o3.clear()
    o2.clear()
    if len(o5) >= 2:
      print("3/2")

def history():
  global add
  with open('database.txt' , 'a') as file:
    add = file.write(track + '\n')
  database = open('database.txt')
  print('Recently Data : ' ,'\n', database.read())
  if database.tell() > 10 :
    os.remove('database.txt')
