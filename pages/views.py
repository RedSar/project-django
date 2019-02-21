from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import *


def index(req):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[0:3]

    context = {
        'listings': listings,
        'states': states,
        'bedrooms': bedrooms,
        'prices': prices,
    }

    return render(req, 'pages/index.html', context)


def about(req):
    realtors = Realtor.objects.order_by('hire_date')
    mvp_realtors = Realtor.objects.filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }

    return render(req, 'pages/about.html', context)
