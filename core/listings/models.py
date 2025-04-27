from django.db import models
from django.utils.timezone import now
class Listing(models.Model):
    class SalesType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'
        
    class BuidlingType(models.TextChoices):
        BUNGALOW = 'Bungalow'
        DUPLEX = 'Duplex'
        STOREY_BUILDING = 'Storey Building'
        
    realtor = models.EmailField(max_length=255)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.DecimalField(decimal_places=1, max_digits=2)
    sale_type = models.CharField(max_length=15, choices=SalesType.choices, default = SalesType.FOR_RENT)
    building_type = models.CharField(choices=BuidlingType.choices, max_length = 15, default = BuidlingType.BUNGALOW)
    main_photo = models.ImageField(upload_to='listings/')
    main_photo = models.ImageField(upload_to='listings/')
    extra_photo1 = models.ImageField(upload_to='listings/')
    extra_photo2 = models.ImageField(upload_to='listings/')
    extra_photo3 = models.ImageField(upload_to='listings/', null=True, blank=True)
    is_published = models.BooleanField(default= False)
    date_created = models.DateTimeField(default=now)
    
    
    def __str__(self):
        return self.title