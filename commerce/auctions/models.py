from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class User(AbstractUser):
    pass

class Listing(models.Model):
    #Getting the time that the listing was created
    now = datetime.datetime.now()

    #User Data
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE, default="")

    #Data about the product
    product = models.CharField(max_length=64)
    price = models.CharField(max_length=15)
    #price = models.DecimalField(max_digits=10,decimal_places=2)
    image_url = models.URLField(default=0, blank=True)
    description = models.CharField(max_length=360)
    num_bids = models.IntegerField(default=0)
    active = models.IntegerField(default=1)
    category = models.CharField(max_length=64,default="")
    date = models.CharField(max_length=10, default=f"{now.month}/{now.day}/{now.year}")
    #top_bid = models.DecimalField(max_digits=10, decimal_places=2)
    top_bid = models.CharField(max_length=15, default=0)

    wishlist = models.ManyToManyField(User, blank=True, related_name="wishlisted_listings")

    def __str__(self):
        if self.active:
            return f"{self.id}: {self.author.username} selling {self.product} for {self.price} is active"
        return f"{self.id}: {self.author.username} selling {self.product} for {self.price}"



class Bid(models.Model):
    #User Data
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")

    #Bid Data
    #bid = models.DecimalField(max_digits=10, decimal_places=2)
    bid = models.CharField(max_length=15, default="")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, default="") 
    win = models.IntegerField(default=0)

    def __str__(self):
        if self.win:
            return f"{self.id}: {self.user.username} has winning bid on {self.listing.product} for {self.bid}"
        return f"{self.id}: {self.user.username} made bid on {self.listing.product} for {self.bid}"



class Comment(models.Model):
    now = datetime.datetime.now()

    #User Data
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, default="")

    #Comment Data
    comment = models.CharField(max_length=360)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    date = models.CharField(max_length=10, default=f"{now.month}/{now.day}/{now.year}")



    def __str__(self):
        return f"{self.id}:{self.commenter} \n {self.comment}"
    


class Wishlist(models.Model):
    pass
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    listing = models.ManyToManyField(Listing, blank=True)

    def __str__(self):
        return f"{self.user.username} has wishlisted {self.listing.product}"

        """