import uuid
from django.db import models
from .consts import CARS_BRANDS, TRANSMISSION_OPTIONS
from users.models import Profile, Location
from .utils import user_listing_path

class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    brand = models.CharField(max_length=24, choices=CARS_BRANDS, default=None)
    model = models.CharField(max_length=64)
    Fuel = models.CharField(max_length=17)
    prix = models.IntegerField(default=0)
    color = models.CharField(max_length=24)
    description = models.TextField()
    engine = models.CharField(max_length=24)
    transmission = models.CharField(max_length=24, choices=TRANSMISSION_OPTIONS, default=None)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=user_listing_path)


    def __str__(self):
        return f"{self.seller.user.username}'s Listing - {self.model}"
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email} - {self.message[:20]}"  


class RentList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    renter = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    message = models.TextField()
    email = models.EmailField(max_length=254, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.listing} {self.renter} - {self.message[:20]}" 
    
    