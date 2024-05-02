from django.contrib import admin

from .models import Listing,Message, RentList


class ListingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Listing, ListingAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')

admin.site.register(Message, MessageAdmin)


class RentListAdmin(admin.ModelAdmin):
    list_display = ('id', 'listing', 'renter', 'start_date', 'end_date', 'message', 'email', 'phone')
    list_filter = ('start_date', 'end_date')
    search_fields = ('listing__brand', 'listing__model')

admin.site.register(RentList, RentListAdmin)