from django.contrib import admin
from .models import Profile, Location, Clients

class ProfileAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

class Registration(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone', 'password')

admin.site.register(Clients, Registration) 
    

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Location, LocationAdmin)


