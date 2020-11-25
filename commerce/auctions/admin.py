from django.contrib import admin

from .models import User, Bid, Comment, Listing, Wishlist
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ("wishlist",)


admin.site.register(User)
admin.site.register(Listing, UserAdmin)
admin.site.register(Bid)
admin.site.register(Comment)
admin.site.register(Wishlist)
