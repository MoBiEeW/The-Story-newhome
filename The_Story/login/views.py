import tornado.ioloop
import tornado.web
from django.shortcuts import render, redirect
from django.http import HttpResponse
from login.models import Story, Post
from django.contrib.auth.models import User, auth
from django.contrib import messages
import json


# Create your views here.


class uploadImgHandler(tornado.web.RequestHandler):
    def post(self):
        files = self.request.files["fileImage"]
        for f in files:
            fh = open(f"upload/{f.filename}", "wb")
            fh.write(f.body)
            fh.close()
        self.write(f"http://localhost:8080/img/{f.filename}")

    def get(self):
        self.render("index.html")


if (__name__ == "__main__"):
    app = tornado.web.Application([
        ("/", uploadImgHandler),
        ("/img/(.*)", tornado.web.StaticFileHandler, {'path': 'upload'})
    ])

    app.listen(8080)
    print("Listening on port 8080")
    tornado.ioloop.IOLoop.instance().start()


def register(request):
    return render(request, 'register.html')


def loginForm(request):
    return render(request, 'login.html')


def home(request):
    namestory = Story.objects.all()
    # id = Story.objects.values()
    # list_id = [x for x in id]
    # ID = list_id[]['id']
    for n in namestory:
        print(n.id)
    print(namestory[1].id)
    return render(request, 'homepage.html', {'posts': namestory})


def search(request):
    search = request.GET['search']
    story = Story.objects.all
    return render(request, 'search.html', {'key': search, 'posts': story})


def readpage(request, id):
    # story = Story.objects.all()
    # result = Story.objects.values()
    # print(namestory[1].id)
    # list_result = [x for x in result]
    # text1 = list_result[3]['text1'].split(',')
    # text2 = list_result[3]['text2'].split(',')
    # new_text = []
    # print(result)
    # for i in range(len(text1)):
    #     new_text.append(text1[i])
    #     new_text.append(text2[i])
    # obj = Story.objects.get(id=1)
    # id = request.GET['id']
    story = Story.objects.get(id=id)
    name1 = story.namechat1
    name2 = story.namechat2
    text1 = story.text1.split(',')
    text2 = story.text2.split(',')
    return render(request, 'reader.html', {'text1': text1, 'text2': text2, 'name1': name1, 'name2': name2})
    # new_text = []
    # for i in range(len(text1)):
    #     new_text.append(story.namechat1)
    #     new_text.append(text1[i])
    #     new_text.append(story.namechat2)
    #     new_text.append(text2[i])
    # leftchat = []
    # rightchat = []
    # for i in range(0, len(new_text), 4):
    #     leftchat.append(new_text[i])
    #     leftchat.append(new_text[i+1])
    # for i in range(2, len(new_text), 4):
    #     rightchat.append(new_text[i])
    #     rightchat.append(new_text[i+1])
    # print(story)

    # return render(request, 'reader.html', {'new_text': new_text, 'leftchat': leftchat, 'rightchat': rightchat})


def catergorypage(request, key):
    story = Story.objects.all()
    return render(request, 'catergory.html', {'posts': story, 'key': key})


def addUser(request):
    username = request.GET['username']
    firstname = request.GET['firstname']
    lastname = request.GET['lastname']
    email = request.GET['email']
    password = request.GET['password']
    repassword = request.GET['repassword']

    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'UserName นีมีคนใช้แล้ว')
            return redirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email นี้เคยลงทะเบียนแล้ว')
            return redirect('/register')
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=firstname,
                last_name=lastname
            )
            user.save()
            return redirect('/home')
    else:
        messages.info(request, 'รหัสผ่านไม่ตรงกัน')
        return redirect('/register')


def addstoryform(request):
    return render(request, 'addstory.html')


def savestory(request):
    title = request.GET['title']
    textcharacter1 = request.GET['text1']
    textcharacter2 = request.GET['text2']
    charactername1 = request.GET['namechat1']
    charactername2 = request.GET['namechat2']
    desc = request.GET['desc']
    if request.method == 'GET':
        catergory = request.GET.getlist('vehicle1')
    catergory = ','.join(catergory)
    # cat = request.GET['vehicle1']
    username = request.user.username
    obj = Story(
        title=title,
        text1=textcharacter1,
        text2=textcharacter2,
        namechat1=charactername1,
        namechat2=charactername2,
        user=username,
        desc=desc,
        catergory=catergory
    )
    obj.save()
    return redirect('/home')


def login(request):
    data = request.POST
    body = data.dict()
    username = body['username']
    password = body['password']
    # login
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect("/home")
    else:
        messages.info(request, 'ไม่พบข้อมูล')
        return redirect('/loginForm')


def logout(request):
    auth.logout(request)
    return redirect('/home')
