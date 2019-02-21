from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


from listings.models import Listing
from .choices import *


def listings(req):
    listings = Listing.objects.order_by('-list_date')
    paginator = Paginator(listings, 25)  # Show 25 listings per page

    page = req.GET.get('p')  # getting the value of the page from the URL
    listings_pages = paginator.get_page(page)

    context = {
        'listings': listings_pages,
    }

    return render(req, 'listings/listings.html', context)


def listing(req, listing_id: int):

    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }

    return render(req, 'listings/listing.html', context)


def search(req):
    queryset_list = Listing.objects.order_by('-list_date')

    # keywords:
    if 'keywords' in req.GET:
        keywords = req.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    # city:
    if 'city' in req.GET:
        city = req.GET['city']
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)
    # state:
    if 'state' in req.GET:
        state = req.GET['state']
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)
    # bedrooms:
    if 'bedrooms' in req.GET:
        bedroom = req.GET['bedrooms']
        if bedroom:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedroom)
    # price:
    if 'price' in req.GET:
        price = req.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    context = {
        'listings': queryset_list,
        'states': states,
        'bedrooms': bedrooms,
        'prices': prices,
        'queryParams': req.GET
    }
    return render(req, 'listings/search.html', context)
