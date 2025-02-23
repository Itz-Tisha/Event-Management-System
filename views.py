from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django.contrib import messages
from .models import UserType,club,event,event_reg
from .forms import SignUpForm,LoginForm,ClubForm,eventform,EventRegForm
from django . contrib.auth import login,authenticate,logout
from django.contrib.auth.hashers import check_password
from django.db.models import F

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            
         
            if UserType.objects.filter(email=email).exists():
                messages.error(request, "Email is already taken!")
                return redirect('sign_up')  

          
            request.session['username'] = form.cleaned_data['name']
            request.session['email'] = form.cleaned_data['email']
            request.session['password'] = form.cleaned_data['password']
            request.session['user_type'] = form.cleaned_data['user_type']
            
            
            user = form.save(commit=False)
            user.save()

            messages.success(request, "Sign up successful! You can now log in.")
            return redirect('user_login')  
    else:
        form = SignUpForm()

    return render(request, 'sign.html', {'form': form})




def home(request):
    clubs = club.objects.all()
    events = event.objects.all() 
    is_org=False 
    username = request.session.get('username','')
    print(request.session.get('user_type', ''))
    if request.session.get('user_type', '') == 'organizer':
        is_org=True
    return render(request, 'home.html',{'events':events , 'is_org':is_org,'clubs':clubs,'username':username})




def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
               
                user = UserType.objects.get(name=username) 
                
                if check_password(password, user.password):
                     
                    messages.success(request, "Logged in successfully!")
                    request.session['username'] = form.cleaned_data['username']
                    request.session['user_type'] = user.user_type
                    name=user.name
                    return redirect('home')
                else:
                    messages.error(request, "Invalid credentials. Please try again.")
            except UserType.DoesNotExist:
                messages.error(request, "User does not exist. Please sign up.")

        else:
            print(form.errors)  

        return redirect('user_login')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def create_club(request):
    form = ClubForm() 
    if request.method =='POST':
     form = ClubForm(request.POST)
     if form.is_valid():
         club = form.save(commit=False)
         uname=request.session.get('username', '') 
         username = UserType.objects.get(name=uname)
         club.org_name = username
         club.save()
         return redirect('home')
     else:
         form=ClubForm()
    return render(request, 'club.html', {'form': form})



def create_event(request):
    uname = request.session.get('username', '') 
    try:
        user_type = UserType.objects.get(name=uname)  
    except UserType.DoesNotExist:
        user_type = None

    clubs = club.objects.filter(org_name=user_type) if user_type else club.objects.none()
    
    form = eventform(clubs=clubs)  

    if request.method == 'POST':
        form = eventform(request.POST, clubs=clubs)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'event_create.html', {'form': form})


def register_for_event(request, event_id):
    current_event = get_object_or_404(event, id=event_id)

    if request.method == 'POST':
        form = EventRegForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']  
            name = form.cleaned_data['name']
          

            session_email = request.session.get('email', '')
            if email != session_email:
                messages.error(request, 'Invalid email')
                return render(request, 'event_register.html', {'form': form, 'event': current_event})
            
            if event_reg.objects.filter(email=email, event_name=current_event,name=name).exists():
                messages.error(request, "You already registered for this event.")
                return render(request, 'event_register.html', {'form': form, 'event': current_event})  

            
             
           
            form.instance.event_name = current_event
            form.save()

            
            event.objects.filter(id=event_id).update(attendee=F('attendee') + 1)

            messages.success(request, "Successfully registered for the event!")  
            return redirect('home')

    else:
        form = EventRegForm()

    return render(request, 'event_register.html', {'form': form, 'event': current_event})

def club_events(request, clubname):
   
    events = event.objects.filter(club_name__clubname=clubname)
    
    return render(request, 'events.html', {'events': events})

def edit_details(request):
    return render(request,'edit_details.html')
