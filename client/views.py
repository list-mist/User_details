
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import Login,Signup
from .models import AddUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Show
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.generic import UpdateView,DeleteView

def index(request):
    try:
        if request.session['email']:
            data=AddUser.objects.all()
            return render(request,"user.html",{"data":data})
    except:
        f=Login()
        return render(request,'login.html',{"form":f})

def signUp(request):
    try:
        if request.session['email']:
            data=AddUser.objects.all()
            print("data --> ",data)
            return render(request,'user.html',{"data":data})
    except:
        f=Signup()
        return render(request,'signup.html',{"form":f})
def after_signup(request):
    if request.method=="GET":
            return redirect("/signup/")
    else:
            form=Signup(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                confirm_password=form.cleaned_data['confirm_password']
                address=form.cleaned_data['address']
                try:
                    AddUser.objects.get(email=email)
                    msg="User already exists"
                    form=Signup()
                    return render(request,'signup.html',{'msg':msg,'form':form})
                except:
                    if password==confirm_password:
                        AddUser.objects.create(username=username,email=email,password=password,confirm_password=confirm_password,address=address)
                        f=Login()
                        msg="Account created successfully"
                        m="Please login to continue"
                        return render(request,'login.html',{'msg':msg,'form':f,'m':m})
                    else:
                        msg="Password do not match"
                        form=Signup()
                        return render(request,'signup.html',{'msg':msg,'form':form})
            else:
                msg = "Please Fill The Entries Correctly"
                form = Signup()
                return render(request, "signup.html", {'form': form, 'msg': msg})
def afterlogin(request):
    if request.method=="GET":
        return redirect('/index/')
    else:
        form=Login(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            try:
                AddUser.objects.get(email=email)
            except:
                msg="Invalid email or password"
                form=Login()
                return render(request,'login.html',{"msg":msg,"form":form})
            else:
                if AddUser.objects.get(email=email).password==password:
                    request.session['email']=email
                    data=AddUser.objects.all()
                    return render(request,"user.html",{"data":data})
                msg="Invalid email or password"
                form=Login()
                return render(request,'login.html',{"msg":msg,"form":form})


class UserAPI(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

    def get(self,reqeust):
        all_=AddUser.objects.all()
        serializer=Show(all_,many=True)
        return Response({'status':200,'payload':serializer.data})
    def post(self,request):
        serializer=Show(data=request.data)
        if not serializer.is_valid():
            return Response({'status':401,'payload':serializer.errors,'message':'Some error has occured'})
        serializer.save()
        user=AddUser.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        print(Response.access_token)
        return Response({'status':200,'payload':serializer.data,'refresh': str(refresh),
        'access': str(refresh.access_token),'message':'Your data has been saved'})
def logout(request):
   del request.session['email']
   return redirect('/')
class Update_data(UpdateView):
    model=AddUser
    template_name='update.html'
    fields=['username','email','address']
    success_url ="/"

class Delete_data(DeleteView):
    model=AddUser
    template_name='delete.html'
    fields=['username','email','address']
    success_url ="/"