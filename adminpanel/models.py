from django.db import models

class GlobalSettings(models.Model):
    SiteName = models.CharField(max_length=100)
    SiteContact = models.CharField(max_length=50)
    SiteEmail = models.EmailField()
    SiteAddress = models.CharField(max_length=500)
    logo = models.ImageField(upload_to="images/",max_length=200, null=True, default=None)
    back_image = models.ImageField(upload_to="admin/",null=True)
    brochure = models.FileField(upload_to="brochurefile/",null=True, default=None)

    def __str__(self):
        return self.SiteName
      

class Navigation(models.Model):
    PAGE_TYPE = (
        ('Home', 'Home'),('Service', 'Service'),
        ('about', 'about'),('contact','contact'), ('Features', 'Features'),
        ('group', 'group'),
    )
    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft')
    )

    name = models.CharField(max_length=100, null=False)
    caption = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS, max_length=50)
    position = models.IntegerField()
    page_type = models.CharField(choices=PAGE_TYPE, null=True, blank=True, max_length=50)
    title = models.CharField(max_length=200)
    short_desc = models.TextField(null=True, blank=True)
    long_desc = models.TextField(null=True)
    banner_image = models.ImageField(upload_to="about/")
    meta_title = models.CharField(max_length=100, null=True)
    meta_keyword = models.CharField(max_length=100, null=True)
    icon_image = models.ImageField(upload_to="about/")
    slider_image = models.ImageField(upload_to="about/", null=True)
    back_image = models.ImageField(upload_to="about/", null=True)
    image1 = models.ImageField(upload_to="about/", null=True)
    image2 = models.ImageField(upload_to="about/", null=True)
    description = models.TextField( null=True)
    Parent = models.ForeignKey('self', related_name="childs",on_delete=models.CASCADE,null=True, blank=True)
    title1= models.CharField(max_length=200,null=True)
    title2= models.CharField(max_length=200,null=True)
    short_desc1 = models.TextField(null=True)
    short_desc2 = models.TextField(null=True)


    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    subject = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Gallery(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="gallery/")
    
    def __str__(self):
        return self.name


class Slider(models.Model):
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length=50)
    image = models.ImageField(upload_to="slider/")

    def _str_(self):
        return self.name
    

class Room_details(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='rooms/')
    description = models.TextField(null=True)
    n_bed=models.IntegerField()
    n_people=models.IntegerField()
    room_size=models.IntegerField()
    Ac_NonAc=models.CharField(max_length=50)
    price_single=models.IntegerField()
    price_double=models.IntegerField()
    extra_bed_price=models.IntegerField()
   
    
    
    def __str__(self):
        return self.name

class Review(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()
    star = models.IntegerField(null=True)
    feedback = models.CharField(max_length=10000,null=True)
    
    
    def __str__(self):
        return self.name

class Hotel_Component(models.Model):
    name = models.CharField(max_length=100)
    total = models.IntegerField(null=True)
    icon = models.CharField(max_length=50,null=True)

    
    def __str__(self):
        return self.name

class Check(models.Model):
    check_in =models.CharField(max_length=10,null=False)
    check_out =models.CharField(max_length=10,null=False)
    
    
    
    
class Key_Feature(models.Model):
    FEATURES_TYPE=(
        ('GROUP','GROUP'),
        ('PROPERTY FEATURE SERVICES','PROPERTY FEATURE SERVICES'),
        ('PROPERTY FACILITIES','PROPERTY FACILITIES'),('ROOM FACILITIES','ROOM FACILITIES'),
        ('FEATURE COMPONENTS','FEATURE COMPONENTS')
        )
    
    name = models.CharField(max_length=100)
    features_type =  models.CharField(max_length=100,choices=FEATURES_TYPE,null=True)
    position = models.IntegerField(null=True)
    icon = models.CharField(max_length=50,null=True)
    Parent = models.ForeignKey('self', related_name="childs",on_delete=models.CASCADE,null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
    
    

    
    


