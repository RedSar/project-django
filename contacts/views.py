from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contact


def contact(req):
    if req.method == 'POST':

        if req.user.is_authenticated:
            has_contacted = Contact.objects.filter(
                user_id=req.POST['user_id'], listing_id=req.POST['listing_id'])

            if has_contacted:
                messages.error(
                    req, 'Your have already make an inquiry for this listing')

                return redirect('/listings/'+req.POST['listing_id'])

        Contact.objects.create(
            user_id=req.POST['user_id'],
            listing_id=req.POST['listing_id'],
            listing=req.POST['listing'],
            name=req.POST['name'],
            email=req.POST['email'],
            phone=req.POST['phone'],
            message=req.POST['message'],
        )

        send_mail('Property Listing Inquiry',
                  'There has been an inquiery for ' +
                  req.POST['listing'] +
                  '. Sign into admin panel for more info .',
                  'redouane.devpurpose@gmail.com',
                  [req.POST['realtor_email'], 'radouane.sintram@gmail.com'],
                  fail_silently=False
                  )

        messages.info(
            req, 'Your request has been submitted , a realtor will get back to you soon')

        return redirect('/listings/'+req.POST['listing_id'])
