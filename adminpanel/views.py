from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from .models import GlobalSettings , Gallery ,Slider, Hotel_Component ,Key_Feature
from django.contrib.auth.decorators import login_required
from django.conf import settings


def admin_login(request):
    glob = GlobalSettings.objects.all()
    try:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")         
            user_obj = User.objects.filter(username=username)
            
            if not user_obj.exists():
                messages.info(request, "Account not found")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            
            user_obj = authenticate(username=username, password=password)

            if user_obj and user_obj.is_superuser:
                login(request, user_obj)
                return redirect("dashboard")
          
            messages.info(request, "Invalid password")
            # You can also return the render with the messages here if you prefer.
                    
        return render(request, "login.html",{'glob':glob})
       
    except Exception as e:
        print(e)
        # Add a proper response in case of an exception
        return HttpResponse("An error occurred")



@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    glob=GlobalSettings.objects.all()
    component = Hotel_Component.objects.all()
    chec= Check.objects.all()
    
    return render(request, "dashboard.html",{'glob':glob,'component': component,'chec':chec})



def Logoutpage(request):
    logout(request)
    return redirect("admin_login")


@login_required(login_url=settings.LOGIN_URL)
def globalsetting(request):
    glob = GlobalSettings.objects.all()
    try:
        data = GlobalSettings.objects.first()
    except GlobalSettings.DoesNotExist:
        data = None

    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        email = request.POST.get('email')
        brochure = request.FILES.get('brochure')
        logo = request.FILES.get('logo')
        back_image = request.FILES.get('back_image')

        if data is None:
            # Create a new GlobalSettings object
            data = GlobalSettings(SiteName=name, SiteContact=contact, SiteAddress=address, SiteEmail=email)
        else:
            # Update existing GlobalSettings object
            data.SiteName = name
            data.SiteContact = contact
            data.SiteAddress = address
            data.SiteEmail = email
            
        if brochure:
            data.brochure = brochure
        
        if back_image:
            # Set the uploaded image to the 'background' field
            data.back_image = back_image
            

        if logo:
            # Set the uploaded image to the 'logo' field
            data.logo = logo
        

        data.save()

        return redirect('globalsetting')  # Redirect to the same view after saving the data

    return render(request, "globalsetting.html", {"data": data, 'glob' : glob})

@login_required(login_url=settings.LOGIN_URL)
def main_navigation(request, parent_id=None):
    glob=GlobalSettings.objects.all()
    
        
    if parent_id:
        obj = Navigation.objects.filter(Parent=parent_id).order_by('position')
    else:
        obj = Navigation.objects.filter(Parent = None).order_by('position')
 
    return render(request, "main_navigation.html", {'obj' : obj, 'parent_id':parent_id,'glob':glob})


@login_required(login_url=settings.LOGIN_URL)
def navigation(request,parent_id=None):
    glob=GlobalSettings.objects.all()

    obj = Navigation.objects.all()

    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get('name')
        caption = request.POST.get('caption')
        status = request.POST.get('status')
        position = request.POST.get('position')
        page_type = request.POST.get('page_type')
        title = request.POST.get('title')
        title1 = request.POST.get('title1')
        title2 = request.POST.get('title2')
        short_desc = request.POST.get('short_desc')
        short_desc1 = request.POST.get('short_desc1')
        short_desc2 = request.POST.get('short_desc2')
        long_desc = request.POST.get('long_desc')
        banner_image = request.FILES.get('banner_image')
        meta_title = request.POST.get('meta_title')
        meta_keyword = request.POST.get('meta_keyword')
        icon_image = request.FILES.get('icon_image')
        slider_image = request.FILES.get('slider_image')
        back_image = request.FILES.get('back_image')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        description = request.POST.get('description')
        parent_id = request.POST.get('Parent')
        
        if parent_id:
            parent_navigation = Navigation.objects.get(pk=parent_id)
        else:
            parent_navigation = None

        # Create a new Navigation objectj
        obj = Navigation.objects.create(
            name=name,
            caption=caption,
            status=status,
            position=position,
            page_type=page_type,
            title=title,
            title1=title1,
            title2=title2,
            short_desc=short_desc,
            short_desc1=short_desc1,
            short_desc2=short_desc2,
            long_desc=long_desc,
            meta_title=meta_title,
            meta_keyword=meta_keyword,
            description=description,            
            Parent=parent_navigation,  # Assign parent navigation object
        )
        

        # Set uploaded images
        if banner_image:
            obj.banner_image = banner_image
            
        if icon_image:
            obj.icon_image = icon_image
            
        if slider_image:
            obj.slider_image1 = slider_image
        
        if back_image:
            obj.back_image=back_image
        
        if image1:
            obj.image1 = image1
            
        if image2:
            obj.image2 = image2
        

        obj.save()  # Save the new Navigation object to the database

        obj = Navigation.objects.all()  # Update the navigation list with the new object
        
        if parent_id:
            return redirect('main_navigation', parent_id=parent_id)
        
        else:
            return redirect('main_navigation')
   

    return render(request, 'navigation.html', {'obj': obj,'glob':glob,'parent_id':parent_id})
  
@login_required(login_url=settings.LOGIN_URL)
def update(request, pk):
    glob = GlobalSettings.objects.all()
    data = get_object_or_404(Navigation, pk=pk)

    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get('name')
        caption = request.POST.get('caption')
        status = request.POST.get('status')
        position = request.POST.get('position')
        page_type = request.POST.get('page_type')
        title = request.POST.get('title')
        title1 = request.POST.get('title1')
        title2 = request.POST.get('title2')
        short_desc = request.POST.get('short_desc')
        short_desc1 = request.POST.get('short_desc1')
        short_desc2 = request.POST.get('short_desc2')
        long_desc = request.POST.get('long_desc')
        banner_image = request.FILES.get('banner_image')
        meta_title = request.POST.get('meta_title')
        meta_keyword = request.POST.get('meta_keyword')
        icon_image = request.FILES.get('icon_image')
        slider_image = request.FILES.get('slider_image')
        back_image = request.FILES.get('back_image')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        description = request.POST.get('description')
        parent_id = request.POST.get('Parent')
        
        if parent_id:
            parent_navigation = Navigation.objects.get(pk=parent_id)
        else:
            parent_navigation = None
        

        # Update the object with the form data
        data.name = name
        data.caption = caption
        data.status = status
        data.position = position
        data.page_type = page_type
        data.title = title
        data.title1 = title1
        data.title2 = title2
        data.short_desc = short_desc
        data.short_desc1 = short_desc1
        data.short_desc2 = short_desc2
        data.long_desc = long_desc
        data.meta_title = meta_title
        data.meta_keyword = meta_keyword
        data.description = description
        data.Parent = parent_navigation
        

        if banner_image:
            data.banner_image = banner_image

        if icon_image:
            data.icon_image = icon_image
            
        if slider_image:
            data.slider_image = slider_image
        
        if back_image:
            data.back_image = back_image
        
        if image1:
            data.image1 = image1
            
        if image2:
            data.image2 = image2

        data.save()

        if parent_id:
            return redirect('main_navigation', parent_id = parent_id)
        
        else:
            return redirect('main_navigation')
        
    parent_id = data.Parent.id if data.Parent else None

    return render(request, "update.html", {'data': data,'glob':glob,'parent_id':parent_id})

@login_required(login_url=settings.LOGIN_URL)
def delete(request, pk):
    data = get_object_or_404(Navigation, pk=pk)
    parent_id=None

    if request.method == "POST":
        parent_id=data.Parent.id if data.Parent else None 
       
        data.delete()
    if parent_id:
        return redirect('main_navigation', parent_id = parent_id)
        
    else:
        return redirect('main_navigation')
    

@login_required(login_url=settings.LOGIN_URL)   
def contact_us(request):
    data=Contact.objects.all()
    glob=GlobalSettings.objects.all()
    
    return render(request,'contact_us.html',{'data':data,'glob':glob})

@login_required(login_url=settings.LOGIN_URL)
def delete_contact_us(request,pk):
    data=get_object_or_404(Contact,pk=pk)
    if request.method == "POST":
        data.delete()
        
        return redirect('contact_us')
    return redirect('contact_us')

@login_required(login_url=settings.LOGIN_URL)
def gallery(request):
    glob=GlobalSettings.objects.all()
    gall=Gallery.objects.all()
    
    
    return render(request,'gallery.html',{'glob':glob,'gall':gall})

@login_required(login_url=settings.LOGIN_URL)
def gallery_create(request):
    glob = GlobalSettings.objects.all()
    gall=Gallery.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
     
        image = request.FILES.get('image')
            # Create a new Gallery object
        gall =Gallery(name=name)
    

        if image:
            # Set the uploaded image to the 'image' field
            gall.image = image

        gall.save()
        return redirect('gallery')

    return render(request,'create_gallery.html',{'gall':gall,'glob':glob})  # Redirect to the same view after saving the data

@login_required(login_url=settings.LOGIN_URL)
def gallery_update(request, pk):
    glob = GlobalSettings.objects.all()
    gall = get_object_or_404(Gallery, pk=pk)
    
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get('name')
        image = request.FILES.get('image')
        
        gall.name=name
        if image:
            # Set the uploaded image to the 'image' field
            gall.image = image
            
        gall.save()  
        
        return redirect('gallery')
    return render(request,'update_gallery.html',{'gall':gall,'glob':glob})  
            
            
@login_required(login_url=settings.LOGIN_URL)
def gallery_delete(request,pk):
    gall=get_object_or_404(Gallery,pk=pk)
    if request.method == "POST":
        gall.delete()
        
        return redirect('gallery')
    return redirect('gallery')

@login_required(login_url=settings.LOGIN_URL)
def slider(request):
    glob = GlobalSettings.objects.all()
    slid = Slider.objects.all()
    
    return render(request, "slider.html",{'slid':slid, 'glob' : glob})
    

@login_required(login_url=settings.LOGIN_URL)
def slider_create(request):
    glob = GlobalSettings.objects.all()
    slid = Slider.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        caption = request.POST.get('caption')
        image = request.FILES.get('image')

        slid = Slider(name=name,caption=caption)

        if image:
            slid.image = image

        slid.save()

        return redirect('slider')  

    return render(request, "create_slider.html",{'slid':slid,'glob':glob})

@login_required(login_url=settings.LOGIN_URL)
def slider_update(request, pk):
    glob = GlobalSettings.objects.all()
    slid = get_object_or_404(Slider, pk=pk)
    
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get('name')
        caption = request.POST.get('caption')
        image = request.FILES.get('image')
        
        slid.name=name
        slid.caption=caption
        if image:
            # Set the uploaded image to the 'image' field
            slid.image = image
            
        slid.save()  
        
        return redirect('slider')
    return render(request,'update_slider.html',{'slid':slid,'glob':glob})  

@login_required(login_url=settings.LOGIN_URL)
def slider_delete(request,pk):
    slid=get_object_or_404(Slider,pk=pk)
    if request.method == "POST":
        slid.delete()
        
        return redirect('slider')
    return redirect('slider')
 
@login_required(login_url=settings.LOGIN_URL)
def room_details(request):
    glob = GlobalSettings.objects.all()
    r_detail=Room_details.objects.all()
    
    return render(request,'room_details.html',{'glob' : glob,'r_detail':r_detail})

@login_required(login_url=settings.LOGIN_URL)
def room_create(request):
    glob = GlobalSettings.objects.all()
    r_detail=Room_details.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        n_bed = request.POST.get('n_bed')
        n_people = request.POST.get('n_people')
        room_size= request.POST.get('room_size')
        Ac_NonAc = request.POST.get('Ac_NonAc')
        price_single = request.POST.get('price_single')
        price_double = request.POST.get('price_double')
        extra_bed_price = request.POST.get('extra_bed_price')
        
        r_detail=Room_details(
            name=name,
            description=description,
            n_bed=n_bed,
            n_people=n_people,
            room_size=room_size,
            Ac_NonAc=Ac_NonAc,
            price_single=price_single,
            price_double=price_double,
            extra_bed_price=extra_bed_price,
            
        )
        
        if image:
            r_detail.image=image
            
        r_detail.save()
        
        return redirect('room_details')
    
    return render(request,'create_room.html',{'glob' : glob,'r_detail':r_detail})

@login_required(login_url=settings.LOGIN_URL)
def room_update(request,pk):
    glob = GlobalSettings.objects.all()
    r_detail=get_object_or_404(Room_details,pk=pk)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        n_bed = request.POST.get('n_bed')
        n_people = request.POST.get('n_people')
        room_size= request.POST.get('room_size')
        Ac_NonAc = request.POST.get('Ac_NonAc')
        price_single = request.POST.get('price_single')
        price_double = request.POST.get('price_double')
        extra_bed_price = request.POST.get('extra_bed_price')
        
        
        r_detail.name=name
        r_detail.description=description
        r_detail.n_bed=int(n_bed)
        r_detail.n_people=n_people
        r_detail.room_size=room_size
        r_detail.Ac_NonAc=Ac_NonAc
        r_detail.price_single=price_single
        r_detail.price_double=price_double
        r_detail.extra_bed_price=extra_bed_price
            
       
        
        if image:
            r_detail.image=image
            
        r_detail.save()
        
        return redirect('room_details')
    
    return render(request,'update_room.html',{'r_detail':r_detail,'glob':glob})

@login_required(login_url=settings.LOGIN_URL)
def room_delete(request,pk):
    r_detail=get_object_or_404(Room_details,pk=pk)
    if request.method =='POST':
        r_detail.delete()
        
        return redirect('room_details')
    return redirect('room_details')


@login_required(login_url=settings.LOGIN_URL)
def review_details(request):
    glob = GlobalSettings.objects.all()
    rev=Review.objects.all()
    
    return render(request,'review_details.html',{'rev':rev,'glob': glob})

@login_required(login_url=settings.LOGIN_URL)
def review_create(request):
    glob = GlobalSettings.objects.all()
    rev=Review.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        star = request.POST.get('star')
        feedback = request.POST.get('feedback')
        date = request.POST.get('date')
        
        rev=Review(
            name=name,
            feedback=feedback,
            date = date,
            star=star,
        )   
        
        rev.save()
        
        return redirect('review_details')
    
    return render(request,'review.html',{'rev':rev,'glob': glob})

@login_required(login_url=settings.LOGIN_URL)
def review_update(request,pk):
    glob = GlobalSettings.objects.all()
    rev = get_object_or_404(Review,pk=pk)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        star = request.POST.get('star')
        feedback = request.POST.get('feedback')
        date = request.POST.get('date')
        
        rev.star=star
        rev.name=name
        rev.feedback=feedback
        rev.date = date
        
        rev.save()
        
        return redirect('review_details')
     
    
    return render(request,'update_review.html',{'rev':rev,'glob': glob})

@login_required(login_url=settings.LOGIN_URL)
def review_delete(request,pk):
    rev = get_object_or_404(Review,pk=pk)
    if request.method == "POST":
        rev.delete()
        
        return redirect('review_details')
        
    return redirect('review_details')

@login_required(login_url=settings.LOGIN_URL)
def hotel_component(request):
    glob = GlobalSettings.objects.all()
    component = Hotel_Component.objects.all()
    
   

    if request.method == "POST":
        name = request.POST.get('name')
        total = request.POST.get('total')
        icon = request.POST.get('icon')
        
        # Create a new Hotel_Component object
        component = Hotel_Component( name = name, total = total, icon=icon)

        component.save()

        return redirect('hotel_component')  # Redirect to the same view after saving the component

    return render(request, 'hotel_component.html', {"component": component,'glob':  glob})



@login_required(login_url=settings.LOGIN_URL)
def hotel_component_update(request,pk):
    glob = GlobalSettings.objects.all()
    component = get_object_or_404(Hotel_Component,pk=pk)


    if request.method == "POST":
        name = request.POST.get('name')
        total = request.POST.get('total')
        icon = request.POST.get('icon')
        
        #updateHotel_Component object
        component.name = name
        component.total = int(total)
        component.icon = icon

        component.save()

        return redirect('hotel_component')
    
    return render(request,'update_component.html',{'glob':glob,'component':component})


@login_required(login_url=settings.LOGIN_URL)
def hotel_component_delete(request,pk):
    component=get_object_or_404(Hotel_Component,pk=pk)
    
    if request.method == 'POST':
        component.delete()
        return redirect('hotel_component')
    
    return redirect('hotel_component')


 
@login_required(login_url=settings.LOGIN_URL)   
def check(request):
    glob = GlobalSettings.objects.all()
    
    
    try:
        checks = Check.objects.first()
        
    except Check.DoesNotExist:
        checks = None

    if request.method == "POST":
        check_in= request.POST.get('check_in')
        check_out = request.POST.get('check_out')
       

        if checks is None:
            # Create a new Check object
            checks = Check(check_in=check_in, check_out=check_out)
        else:
            # Update existing Check object
            checks.check_in = check_in
            checks.check_out = check_out
           
        checks.save()

        return redirect('check')  # Redirect to the same view after saving the data

    return render(request, "check.html", {'checks':checks,'glob' : glob})


@login_required(login_url=settings.LOGIN_URL)
def key_features(request, parent_id=None):
    glob = GlobalSettings.objects.all() 
    key = Key_Feature.objects.all()
  
    
    if parent_id:
        key = Key_Feature.objects.filter(Parent=parent_id)
        
        
    else:
        key = Key_Feature.objects.filter(Parent=None)
        
    
    return render(request,'key_features.html',{'key':key,'glob':glob,'parent_id':parent_id})


@login_required(login_url=settings.LOGIN_URL)
def create_features(request,parent_id=None):
    glob = GlobalSettings.objects.all()
    key = Key_Feature.objects.all()
    
    if request.method == "POST":
        name = request.POST.get('name')
        position = request.POST.get('position')
        features_type = request.POST.get('features_type')
        icon = request.POST.get('icon')
        parent_id = request.POST.get('Parent')
        
        if parent_id:
            parent_features = Key_Feature.objects.get(pk=parent_id)
            
        else:
            parent_features = None

        key = Key_Feature.objects.create(
            name=name,
            position=position,
            features_type = features_type,
            icon = icon,
            Parent=parent_features,            
            
        )
        
        key.save()
        
        if parent_id:
            return redirect('key_features', parent_id=parent_id)
        
        else:
            return redirect('key_features')
        
    
    return render(request,'create_features.html',{'key':key,'glob':glob,'parent_id':parent_id})

@login_required(login_url=settings.LOGIN_URL)
def update_features(request,pk):
    glob = GlobalSettings.objects.all()
    key = get_object_or_404(Key_Feature,pk=pk)
    
    if request.method == "POST":
        name = request.POST.get('name')
        position = request.POST.get('position')
        icon = request.POST.get('icon')
        features_type = request.POST.get('features_type')
        parent_id = request.POST.get('Parent')
        
        if parent_id:
            parent_features=Key_Feature.objects.get(pk=parent_id)
        else:
            parent_features = None
        
        
        key.name=name
        key.position=position
        key.features_type = features_type
        key.icon = icon
        key.Parent = parent_features
        
        key.save()
               
        
        if parent_id:
            return redirect('key_features', parent_id=parent_id)
        
        else:
            return redirect('key_features')
        
    parent_id = key.Parent.id if key.Parent else None
        
    
    return render(request,'create_features.html',{'key':key,'glob':glob,'parent_id':parent_id})
    

    
@login_required(login_url=settings.LOGIN_URL)
def delete_features(request,pk):
    key = get_object_or_404(Key_Feature,pk=pk)
    parent_id=None
    
    if request.method == "POST":
        parent_id = key.Parent.id if key.Parent else None
        key.delete()
        
    if parent_id:
        return redirect('key_features', parent_id=parent_id)
        
    else:
        return redirect('key_features')

    