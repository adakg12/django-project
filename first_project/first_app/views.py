from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import *
from first_app.forms import UserInfo,UserProfileInfoForm
# Create your views here.


def index(request):
    my_dict = {'text':'Hello Im from views.py','number':100}
    
    return render(request,'index.html',context=my_dict)

def help(request):
    my_help = {'help':'If you need any Help feel free to Contact us!'}
    return render(request,'help.html',context=my_help)

def register(request):
    registerd = False
    if request.method == "POST":
        user_form = UserInfo(data=request.POST) 
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()  

            registerd = True 
        else:
            print(user_form.errors,profile_form.errors)     
    else:
        user_form = UserInfo()
        profile_form = UserProfileInfoForm()
    return render(request,'register.html',
                  {
                    'user_form':user_form,
                    'profile_form':profile_form,
                    'registerd':registerd
                  })

# def user_display(request):
#     user_list = User.objects.all()

#     return render(request,'user.html',{'users':user_list})