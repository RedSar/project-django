from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


def contact(req):
    if req.method == 'POST':
        Contact.objects.create(
            user_id=req.POST['user_id'],
            listing_id=req.POST['listing_id'],
            listing=req.POST['listing'],
            name=req.POST['name'],
            email=req.POST['email'],
            phone=req.POST['phone'],
            message=req.POST['message'],
        )

        messages.info(
            req, 'Your request has been submitted , a realtor will get back to you soon')

    return redirect('/listings/'+req.POST['listing_id'])


# 'user_id': ['4'],
# 'realtor_email': ['kyle@btrealstate.com'],
# 'listing_id': ['1'],
# 'listing': ['45 Drivewood Circle'],
# 'name': ['Maram GUERCHAL'],
# 'email': ['maram@test.com'],
# 'phone': ['669-996'],
# 'message': ['Very interseted']
