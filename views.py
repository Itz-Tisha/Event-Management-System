
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import participants,organizer,gdg

def HomePage(request):
    if 'user_id' not in request.session:
        return redirect('LoginPage')  

    user_id = request.session['user_id']
    role = request.session.get('role')
    is_org=False
    if(role == 'Participant'):
      user = participants.objects.get(id=user_id)  
    else:
        user = organizer.objects.get(id=user_id)
        is_org=True  

    return render(request, "home.html", {'uname': user.name,'is_org':is_org})  

def SignupPage(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('emailid')
        passw = request.POST.get('pass')
        role = request.POST.get('role')
        
        if(role=='Participant'):
          
          if participants.objects.filter(name=name).exists():
            return HttpResponse("Username already exists! Try a different one.")
          hashed_password = make_password(passw)
          participant = participants.objects.create(name=name, email=email, password=hashed_password)
          participant.save()
        else:
            if organizer.objects.filter(name=name).exists():
                return HttpResponse("Username already exists! Try a different one.")
            hashed_password = make_password(passw)
            org = organizer.objects.create(name=name,email=email,password=hashed_password)
            org.save()
        return redirect('LoginPage')  

    return render(request, "signup.html")
def LoginPage(request):
    if request.method == 'POST':
        name = request.POST.get('uname')  
        password = request.POST.get('pass') 
        try:
            user = organizer.objects.get(name=name)
            if check_password(password, user.password):
                request.session['user_id'] = user.id  
                request.session['username'] = user.name
                request.session['role'] = 'Organizer' 
                return redirect("HomePage")
        except organizer.DoesNotExist:
            pass 


        try:
            user = participants.objects.get(name=name)
            if check_password(password, user.password):
                request.session['user_id'] = user.id  
                request.session['username'] = user.name
                request.session['role'] = 'Participant' 
                return redirect("HomePage")
        except participants.DoesNotExist:
            return HttpResponse("Invalid username or password")

    return render(request, "login.html")



def logoutv(request):
    request.session.flush()
    return redirect('LoginPage')

 

def service(request):
    return render(request, "service.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def createeventform(request):
    if request.method == 'POST':
        event_name = request.POST.get('event_name')
        email = request.POST.get('email')
        contactno = request.POST.get('contactno')
        date = request.POST.get('date')
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        location = request.POST.get('location')
        desc=request.POST.get('desc')
        event_img=request.POST.get('event_img')
        purpose=request.POST.get('Purpose_of_event')
          
        if gdg.objects.filter(event_name=event_name).exists():
            return HttpResponse("event already exists! Try a different one.")
        event = gdg.objects.create(event_name=event_name,location=location,date=date,starttime=starttime,endtime=endtime,desc=desc,purpose_of_even=purpose,event_img=event_img,conact=contactno)
        event.save()
       
        return redirect('HomePage')  

    return render(request, "createevent.html")
