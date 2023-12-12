from django.shortcuts import render,redirect
from home.models import Enroller
from django.core.mail import send_mail
from .utils import send_email_to_enrollers
from django.contrib.auth import authenticate, login, logout as auth_logout


# Create your views here.


def admin(request):

    if request.user.username == "combatfitnesscenterthewarriors":

        enrollers = Enroller.objects.all().values()
            
        content = {
            'enrollers' : enrollers
        }

        return render(request,'admin.html',content)
     
    else:
        
        return redirect('/adminsignin')



def approval(request):
    
    if request.user.username == "combatfitnesscenterthewarriors":

        enroller_id = request.POST['enrollerid']
        name = request.POST['name']
        email = request.POST['mail']
        confirm = request.POST.get('confirm',False)
        wait = request.POST.get('wait',False)

        

        if confirm is not False:

            subject = "CFC - Hurray your fitness journey is started"
            msg = "Hey, "+ name + " Few days ago you have submited a form on our website. So this mail is sent you to inform you your form has been accepted. \n So visit our gym by following address and if any query then you can call on number which we have given below:\n\n Address: this this Phone Number: 87797234 Thank You"
            message = msg
            send_email_to_enrollers(
                subject,
                message,
                [email]
            )
            Enroller.objects.filter(id=enroller_id).update(confirm=True)
            Enroller.objects.filter(id=enroller_id).update(wait=False)

            return redirect('/cfcadmin')


        elif wait is not False:

            subject = "CFC - Wait for our response"
            msg = "Hey "+ name + ", Due to some reasons we have put your on hold, will soon send a mail regarding admission so, wait for the response and if any query then you can call on number which we have given below:\n\n Address: this this \n Phone Number: 87797234 Thank You"
            message = msg
            send_email_to_enrollers(
                subject,
                message,
                [email]
            )
            Enroller.objects.filter(id=enroller_id).update(wait=True)
            Enroller.objects.filter(id=enroller_id).update(confirm=False)

            return redirect('/cfcadmin')

    else:
        return redirect('/adminsignin')


    



def confirmlist(request):
    if request.user.username == "combatfitnesscenterthewarriors":
        enrollers = Enroller.objects.all().values()
            
        content = {
            'enrollers' : enrollers
        }


        return render(request, 'confirmlist.html', content)
    else:
        return redirect('/adminsignin')


def waitinglist(request):

    if request.user.username == "combatfitnesscenterthewarriors":
        enrollers = Enroller.objects.all().values()
        
        content = {
            'enrollers' : enrollers
        }


        return render(request, 'waitinglist.html', content)
    else:
        return redirect('/adminsignin')

    

def adminsignin(request):

    username = request.POST.get('username')
    password = request.POST.get('password')

# cfcsohailsir1234
    if username == "combatfitnesscenterthewarriors":
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('cfcadmin')
        else:
            return redirect('/adminsignin')
    else:
        return render(request, 'signin.html')

    




def adminlogout(request):

    auth_logout(request)

    return redirect('/adminsignin')
        
