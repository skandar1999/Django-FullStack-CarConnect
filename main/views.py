from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ContactForm, RentForm

from .models import Listing

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "views/contact.html", {'form': form, 'alert_message': 'Message sent successfully!'})
    else:
        form = ContactForm()
    return render(request, "views/contact.html", {'form': form})

def blog_view(request):
    return render(request, "views/blog.html")

def home_view(request):
    # Fetch all listings
    listings = Listing.objects.all()

    # Fetch available models and brands from listings
    available_models = Listing.objects.values_list('model', flat=True).distinct()
    available_brands = Listing.objects.values_list('brand', flat=True).distinct()
    prix = Listing.objects.values_list('prix', flat=True).distinct()
    available_Fuel = Listing.objects.values_list('Fuel', flat=True).distinct()


    context = {
        'listings': listings,
        'available_models': available_models,
        'available_brands': available_brands,
        'prix': prix,
        'Fuel': available_Fuel,


    }
    return render(request, "views/main.html", context)



def list_view(request):
    if request.method == 'POST':
        pass            
    elif request.method == 'GET':
        pass
    return render(request, 'views/list.html', {} )



def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    form = RentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            rent_request = form.save(commit=False)
            rent_request.listing = listing
            rent_request.start_date = form.cleaned_data['start_date']
            rent_request.end_date = form.cleaned_data['end_date']
            rent_request.message = form.cleaned_data['message']
            rent_request.phone = form.cleaned_data['phone']
            rent_request.email = form.cleaned_data['email']
            # Save the rent request
            rent_request.save()
            # Handle successful form submission (e.g., redirect to a thank you page)
    return render(request, 'views/list.html', {'listing': listing, 'form': form})