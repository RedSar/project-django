from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'list_date',
                    'realtor', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'is_published')
    list_editable = ('is_published', 'price')
    search_fields = ('title', 'description', 'city', 'state')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
