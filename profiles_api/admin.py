from django.contrib import admin

from profiles_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
admin.site.register(models.Product)
admin.site.register(models.Invoice)
admin.site.register(models.InvoiceItem)
