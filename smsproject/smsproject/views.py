from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
import mysql.connector
from django.core.files.storage import FileSystemStorage
import os
from pathlib import Path


def convertToBinaryData(fileName):
 with open(fileName,'rb') as file:
  binaryData = file.read()
 return binaryData
def demofunction(request):
 return HttpResponse("MY NAME")
def home(request):
 return render(request,"home.html")
def aboutus(request):
 return render(request,"aboutus.html")
def loginfunction(request):
 return render(request,"login.html")
def contactfunction(request):
 return render(request,"contact.html")
def index3(request):
    return render(request,"index3.html",{
     "name":name1,
 })
def userSignup(request):
 if request.method=="POST":
  username = request.POST.get('name')
  email=request.POST.get('email')
  password=request.POST.get('password12')
  mydb = mysql.connector.connect(
      user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='user'
  )
  mycursor = mydb.cursor()
  mycursor.execute("select * from signup where email='%s'" % (email))
  ulist = mycursor.fetchall()
  if ulist.__len__() >= 1:
   return render(request, "userSignup.html",{
       "message":"user already exists exists"
   })
  mycursor1 = mydb.cursor()
  mycursor1.execute("INSERT INTO signup  VALUES(null,%s,%s,%s)", (username,email,password))
  mycursor2 = mydb.cursor()
  mycursor2.execute("select * from signup where email='%s'" % (email))
  ulist2=mycursor2.fetchall()
  id=str(ulist2[0][0])
  mycursor4 = mydb.cursor()
  mycursor4.execute("CREATE TABLE user2_"+id+"(id int AUTO_INCREMENT key,hotelId int,roomno int,roomType varchar(100))")
  mydb.commit()
  return render(request,"userSignup.html",{
      "message":"your details saved successfully none"
  })
 return render(request,"userSignup.html")

def userLogin(request):
 if request.method=="POST":
  email=request.POST.get('email1')
  password=request.POST.get('password1')
  mydb = mysql.connector.connect(
      user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com',database='user'
  )
  mycursor = mydb.cursor()
  mycursor.execute("select * from signup where email='%s'" % (email))
  ulist = mycursor.fetchall()
  if ulist.__len__() == 0:
   return render(request, "userSignup.html", {
          "message": "mail not exists exists"
   })
  mycursor1 = mydb.cursor()
  mycursor1.execute("SELECT * FROM signup WHERE email=%s and password=%s ", (email, password))
  login1 = mycursor1.fetchall()
  if login1.__len__() >= 1:
   global id1
   id1=str(login1[0][0])
   global name1
   name1=login1[0][1]
   return redirect('user0')
  else:
      return render(request, "userSignup.html", {
          "message": "entered password is incorrect incorrect"
      })
 return HttpResponse("MANNAVA KAMAL")

def user0(request):
 mydb = mysql.connector.connect(
  user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='Admin'
 )
 mycursor = mydb.cursor()
 mycursor.execute("SELECT id,hotelname FROM signup")
 adminDetails = mycursor.fetchall()
 if adminDetails.__len__() == 0:
    return render(request,"AdminsNotAvailable.html")
 mydb.commit()
 print(adminDetails)
 return render(request,'user0.html',{
     "name": name1,
     "adminDetails":adminDetails,
 })
def hotelSelect(request):
 if request.method == "GET":
  global data
  data = request.GET['data']
  print(data)
  return HttpResponse("yes Iam there")
 return HttpResponse("yes Iam there")
def user1(request):
 mydb = mysql.connector.connect(
  user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='Admin'
 )
 mycursor = mydb.cursor()
 mycursor.execute("SELECT * FROM user1_"+data)
 roomdetails = mycursor.fetchall()
 if roomdetails.__len__() == 0:
  return render(request,"RoomsNotAvailable.html")
 mydb.commit()
 return render(request,"user1.html",{
     'name':name1,
  'roomdetails': roomdetails,
  'booked':0
 })
def bookedrooms(request):
    if request.method == "GET":
        data2 = request.GET['data']
        roomType = request.GET['roomType']
        global data1
        data1 = int(data2)
    return HttpResponse("kaalmla")
def bookingProcess(request):
 mydb1 = mysql.connector.connect(
 user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='Admin'
    )

 mycursor1 = mydb1.cursor()
 mycursor1.execute("select * from user1_"+data+" where roomNo=(%d)" % (data1))
 adminRoom=mycursor1.fetchall()
 return render(request,"booking process.html",{
  'roomnoimg': adminRoom[0][4],
  'roomno':adminRoom[0][0],
  'roomtype':adminRoom[0][1],
 })
def roomConformed(request):
    mydb1 = mysql.connector.connect(
        user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com',database='Admin'
    )
    mycursor1 = mydb1.cursor()
    mycursor1.execute("select * from user1_" + data + " where roomNo=(%d)" % (data1))
    adminRoom = mycursor1.fetchall()
    mydb1.commit()
    mydb2 = mysql.connector.connect(
        user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='Admin'
    )
    mycursor2 = mydb2.cursor()
    mycursor2.execute("UPDATE user1_"+data+" SET booked =%2d WHERE roomno=%2d" % (1,data1))
    mydb2.commit()
    mydb3 = mysql.connector.connect(
        user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='Admin'
    )
    mycursor3 = mydb3.cursor()
    mycursor3.execute("INSERT INTO user2_"+data+"  VALUES(%s,%s,%s)", (adminRoom[0][0],adminRoom[0][1],id1))
    mydb3.commit()
    mydb4 = mysql.connector.connect(
        user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='user'
    )
    mycursor4 = mydb4.cursor()
    mycursor4.execute("INSERT INTO user2_" + id1 + "  VALUES(null,%s,%s,%s)", (data,adminRoom[0][0],adminRoom[0][1]))
    mydb4.commit()
    return render(request, "roomConformed.html", {
        'roomnoimg': adminRoom[0][4],
        'roomno': adminRoom[0][0],
        'roomtype': adminRoom[0][1],
    })
def user2(request):
 mydb = mysql.connector.connect(
  user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='user'
 )
 mycursor = mydb.cursor()
 mycursor.execute("select * from user2_"+id1)
 roomdetails = mycursor.fetchall()
 if roomdetails.__len__() == 0:
     return render(request,"RoomBookedNotAvailable.html")
 return render(request, "user2.html",{
         "name": name1,
  'roomdetails': roomdetails,
 })
def adminDetailsId(request):
     if request.method == "GET":
         global adminDetailsId
         data2 = int(request.GET['data'])
         adminDetailsId = data2
         return HttpResponse("userBookedId")
     return HttpResponse("userBookedId")
def adminDetails(request):
    mydb = mysql.connector.connect(
        user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='Admin'
    )
    mycursor = mydb.cursor()
    mycursor.execute("select name,email from signup where id=%2d " % (adminDetailsId))
    details = mycursor.fetchall()
    mydb.commit()
    return render(request, "adminDetails.html", {
        "name": details[0][0],
        "email": details[0][1],
    })
def roomEntry(request):
  roomNo = request.POST['roomNo']
  roomNo1 = int(roomNo)
  roomType = request.POST['roomType']
  img1 = request.FILES['img']
  simg1=str(img1)
  mydb = mysql.connector.connect(
   user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='Admin'
  )
  mycursor = mydb.cursor()
  mycursor.execute("SELECT roomno FROM user1_"+id+" where roomno=%2d " % (roomNo1))
  roomNo2 = mycursor.fetchall()
  res_len = roomNo2.__len__()
  if (res_len == 1):
   return HttpResponse("you entered roomNo already exists")
  fs = FileSystemStorage()
  fs.save(img1.name, img1)
  BASE_DIR = Path(__file__).resolve().parent.parent
  sdir=str(BASE_DIR) + "\media"
  path = os.path.join(sdir, img1.name)
  str1 = convertToBinaryData(path)
  sqlr="user1_"+id+"img"+roomNo
  mycursor1 = mydb.cursor()
  mycursor1.execute("INSERT INTO user1_"+id+" VALUES (%s,%s,%s,%s,%s)",(roomNo,roomType,0,str1,sqlr))
  mydb.commit()
  os.remove(path)
  return redirect('Admin2')
def adminSignup(request):
 if request.method=="POST":
  username = request.POST.get('name')
  email=request.POST.get('email')
  password=request.POST.get('password12')
  hotelName = request.POST.get('hotelname')
  mydb = mysql.connector.connect(
      user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='Admin'
  )
  mycursor = mydb.cursor()
  mycursor.execute("select * from signup where email='%s'" % (email))
  ulist = mycursor.fetchall()
  if ulist.__len__() >= 1:
      return render(request, "adminSignup.html", {
          "message": "Admin already exists exists"
      })
  mycursor1 = mydb.cursor()
  mycursor1.execute("INSERT INTO signup  VALUES(null,%s,%s,%s,%s)", (username,email,password,hotelName))
  mycursor2 = mydb.cursor()
  mycursor2.execute("select * from signup where email='%s'" % (email))
  ulist2=mycursor2.fetchall()
  id=str(ulist2[0][0])
  mycursor3 = mydb.cursor()
  mycursor3.execute("CREATE TABLE user1_"+id+"(roomno int UNIQUE,roomtype varchar(100),booked int,image mediumblob,imgstr varchar(100))")
  mycursor3 = mydb.cursor()
  mycursor3.execute( "CREATE TABLE user2_"+id+"(roomno int UNIQUE,roomtype varchar(100),id int)")
  mydb.commit()
  return render(request,"adminSignup.html")
 return render(request,"adminSignup.html")
def adminLogin(request):
 if request.method=="POST":
  email=request.POST.get('email1')
  password=request.POST.get('password1')
  mydb = mysql.connector.connect(
      user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com',database='Admin'
  )
  mycursor = mydb.cursor()
  mycursor.execute("select * from signup where email='%s'" % (email))
  ulist = mycursor.fetchall()
  if ulist.__len__() == 0:
      return render(request, "adminSignup.html", {
          "message": "Admin email does not exists exists"
      })
  mycursor1 = mydb.cursor()
  mycursor1.execute("SELECT * FROM signup WHERE email=%s and password=%s ", (email, password))
  login1 = mycursor1.fetchall()
  if login1.__len__() >= 1:
   print(login1)
   global id
   id=str(login1[0][0])
   global name
   name=login1[0][4]
   return render(request,"Admin1.html",{
        'name': name,
    })
  else:
      return render(request, "adminSignup.html", {
          "message": "Admin password is incorrect exists"
      })
 return HttpResponse("MANNAVA KAMAL")
def Admin1(request):
 return render(request, "Admin1.html",{
        'name': name,
    })
def Admin2(request):
 mydb = mysql.connector.connect(
  user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='Admin'
 )
 mycursor = mydb.cursor()
 mycursor.execute("SELECT * FROM user1_"+id )
 roomdetails = mycursor.fetchall()
 if(roomdetails.__len__() == 0):
     return render(request, "AdminRoomsNotAvailable.html")
 for x1 in roomdetails:
  mycursor.execute("SELECT * FROM user1_"+id+" where roomno = {0}".format(x1[0]))
  c3 = mycursor.fetchone()[3]
  c4 = "user1_"+id+"img{0}.png".format(x1[0])
  path = os.path.join(r"C:\Users\acer\OneDrive - K L University\KL\2.2\PFSD\SampleProject\smsproject\static", c4)
  with open(path, "wb") as file:
   file.write(c3)
   file.close()
 return render(request, "Admin2.html", {
  'roomdetailslength': range(0, roomdetails.__len__()),
  'roomdetails': roomdetails,
         'name': name,
 })
def deleteAdminRooms(request):
 data = request.GET['data']
 roomType = request.GET['roomType']
 data1 = int(data)
 c4 = "user1_"+id+"img{0}.png".format(data1)
 BASE_DIR = Path(__file__).resolve().parent.parent
 sdir = str(BASE_DIR) + "\static"
 path = os.path.join(sdir, c4)
 os.remove(path)
 mydb = mysql.connector.connect(
  user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='Admin'
 )
 mycursor = mydb.cursor()
 mycursor.execute("DELETE FROM user1_"+id+" WHERE roomno=%2d  " % (data1))
 mydb.commit()
 var1 = "room"+data+"deleated suceessfully just reload the page"
 return HttpResponse({var1})
def Admin3(request):
 mydb = mysql.connector.connect(
  user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='Admin'
 )
 mycursor = mydb.cursor()
 mycursor.execute("SELECT * FROM user2_"+id)
 roomdetails = mycursor.fetchall()
 if (roomdetails.__len__() == 0):
     return render(request, "AdminLiveRoomsNotAvailable.html",{
        'name': name,
    })
 print(roomdetails)
 return render(request, "Admin3.html", {
  'roomdetails': roomdetails,
         'name': name,
 })
def userBookedId(request):
 if request.method == "GET":
  global userBookedId
  data2 = int(request.GET['data'])
  userBookedId=data2
  return HttpResponse("userBookedId")
 return HttpResponse("userBookedId")

def userDetails(request):
 mydb = mysql.connector.connect(
  user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='user'
 )
 mycursor = mydb.cursor()
 mycursor.execute("select name,email from signup where id=%2d "% (userBookedId))
 details = mycursor.fetchall()
 mydb.commit()
 return render(request,"userDetails.html",{
     "name" :details[0][0],
      "email":details[0][1],
 })
def deleteLiveRoom(request):
 if request.method == "GET":
  roomNo=(request.GET['data'])
  roomNo1=int(roomNo)
  mydb = mysql.connector.connect(
      user='kamal', password='1234567890', host='hotelmanagement1.c54a00es87k3.us-east-1.rds.amazonaws.com', database='Admin'
  )
  mycursor = mydb.cursor()
  mycursor.execute("DELETE FROM user2_"+id+" WHERE roomno=%2d  " % (roomNo1))
  mycursor1=mydb.cursor()
  mycursor1.execute("UPDATE user1_"+id+" SET booked =%2d WHERE roomno=%2d" % (0,roomNo1))
  mydb.commit()
  return HttpResponse("kamal")
 return HttpResponse("kamal")


def adminOrUserChoice(request):
    return render(request,"adminOrUserChoice.html")
def defaultNavbar(request):
 return render(request,"defaultNavbar.html")

def AdminRoomsNotAvailable(request):
    return render(request,"AdminRoomsNotAvailable.html")
def AdminLiveRoomsNotAvailable(request):
    return render(request,"AdminLiveRoomsNotAvailable.html")
def AdminsNotAvailable(request):
    return render(request,"AdminsNotAvailable.html")
def RoomsBookedNotAvailable(request):
    return render(request, "RoomsBookedNotAvailable.html")

def RoomsNotAvailable(request):
    return render(request,"RoomsNotAvaiable.html")