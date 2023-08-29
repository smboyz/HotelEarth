from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from adminpanel.models import *
from adminpanel.models import Contact
from django.contrib import messages

def Base(request):
    home = Navigation.objects.filter(status='Publish', page_type='home')
    services = Navigation.objects.filter(status='Publish', page_type='Service')
    glob = GlobalSettings.objects.all()
    gall=Gallery.objects.all()
    slid = Slider.objects.all()
    r_detail = Room_details.objects.all()
    rev = Review.objects.all()
    component = Hotel_Component.objects.all()
    
    return render(request, "light/home.html", {'home' : home, 'glob': glob,'gall':gall,'slid':slid,'r_detail': r_detail,'rev':rev,'component':component,
                                               'services':services})

def aboutus(request):
    home = Navigation.objects.filter(status='Publish', page_type='home')
    about = Navigation.objects.filter(status='Publish', page_type='about')
    glob = GlobalSettings.objects.all()
    gall=Gallery.objects.all()
 
    return render(request, "light/about.html", {'about' : about, 'glob': glob,'gall':gall,'home':home})
  
def contact(request):
    contact = Navigation.objects.filter(status='Publish', page_type='contact')
    home = Navigation.objects.filter(status='Publish', page_type='home')
    glob = GlobalSettings.objects.all()
    
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        
        if len(name)<2 or len(email)<3 or len(subject)<4 or len(message)<2:
            messages.error(request,"Cannot submit your message. Something went wrong.")

        else:
            data=Contact(name=name,email=email,subject=subject,message=message)
            data.save()
            messages.success(request,"Successfully submitted your message. We will contact you soon...")           
            
        
    
    return render(request, "light/contact.html", {'contact' : contact, 'glob': glob,'home':home})  



def features(request):
    features = Navigation.objects.filter(status='Publish', page_type='features')
    glob = GlobalSettings.objects.all()
    gall=Gallery.objects.all()
    home = Navigation.objects.filter(status='Publish', page_type='home')
    chec= Check.objects.all()
    key = Key_Feature.objects.all()
    f_service = Key_Feature.objects.filter(features_type='PROPERTY FEATURE SERVICES')
    f_facility = Key_Feature.objects.filter(features_type='ROOM FACILITIES')
    f_properties = Key_Feature.objects.filter(features_type='PROPERTY FACILITIES')
    f_component =  Key_Feature.objects.filter(features_type='FEATURE COMPONENTS')
    
    
    
    return render(request, "light/features.html", {'features' : features, 'glob': glob,'gall':gall,'home':home,'chec':chec,'key':key,
                                                   'f_facility':f_facility, 'f_service': f_service, 'f_properties':f_properties, 'f_component':f_component })  

def services(request):
    home = Navigation.objects.filter(status='Publish', page_type='home')
    services = Navigation.objects.filter(status='Publish', page_type='Service')
    glob = GlobalSettings.objects.all()
    gall=Gallery.objects.all()
    
    return render(request, "light/services.html", {'services' : services, 'glob': glob,'gall':gall,'home':home})  

def rooms(request):
    rooms = Navigation.objects.filter(status='Publish', page_type='rooms')
    home = Navigation.objects.filter(status='Publish', page_type='home')
    glob = GlobalSettings.objects.all()
    r_detail=Room_details.objects.all()
    gall=Gallery.objects.all()
    
    
    return render(request, "light/rooms.html", {'rooms' : rooms, 'glob': glob,'r_detail':r_detail,'gall':gall,'home':home})  



  


    

