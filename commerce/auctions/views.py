from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Bid, Comment, Wishlist

#Helper Functions
def make_decimal(num):
    """
    takes a string that is taken from post and converts it to a dollar format
    """
    return '{:.2f}'.format(round(float(num),2))

#Views
def index(request):
    listings= Listing.objects.all()
    return render(request, "auctions/index.html",{
        "listings": listings
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if request.method == "POST":
        user = User.objects.get(username=request.POST["user"])
        price = make_decimal(request.POST["price"])

        listing = Listing(
            author=user,
            product = request.POST["product"],
            price = price,
            top_bid = price,
            category= request.POST["category"],
            image_url = request.POST["image"],
            description = request.POST["description"]
            )
        listing.save()
       # return render(request,"auctions/index.html") #Rember to make it so it brings the user to the listing created
        return HttpResponseRedirect(reverse("index")) #When doing post I should HttpREsponse ot avoid posting multiple times
    else:
        return render(request, "auctions/create.html")


def listing(request, listing_id):
    winning_bid = "" 
    listing = Listing.objects.get(id=listing_id)
    message = ""
    
    #Check for the forms that were submitted then make the correct modifications
    if request.method =="POST":

        #Closes the current listing
        if "close" in request.POST:
            listing.active = 0
            listing.save()
        
        #submits a new bid to the listing
        elif "bid" in request.POST:
            bid = request.POST["bid_amount"]
            
            try:
                float(bid)
                bid = make_decimal(bid)

                if float(listing.top_bid) < float(bid):
                    bid_model = Bid(user=User.objects.get(id=request.POST["current_user_id"]), bid=bid, listing=listing)

                    listing.top_bid = bid
                    listing.num_bids += 1

                    listing.save()
                    bid_model.save()

                    message="Bid was placed"
                
                else:
                    message="Bid is not high enough"
        
            except ValueError:
                message="Invalid price has been entered"


        #Lets the user add it to their wishlist
        elif "wishlist" in request.POST:
            current_user = User.objects.get(id=request.POST["current_user_id"])
            listing.wishlist.add(current_user)
            listing.save()


        #Lets the user post a comment on the post
        elif "comment" in request.POST:
            comment_text = request.POST["comment_text"]
            comment_model = Comment( commenter=User.objects.get(id=request.POST["current_user_id"]), comment=comment_text, listing=listing)
            comment_model.save()

    #If the bidding is closed it will find the winning bid
    if listing.num_bids != 0 and listing.active == 0:
        winning_bid = Bid.objects.get(bid=listing.top_bid,listing=listing)

    #Make sure you just draw the whole thing
    return render(request, "auctions/listing.html", {
        "listing": listing,
        "winning_bid": winning_bid,
        "comments": Comment.objects.filter(listing=listing),
        "message": message
    })

def wishlist(request, username):
    user = User.objects.get(username=username)
    
    all_wishlisted = user.wishlisted_listings.all() #tryin to get all of the listings that i can

    return render(request, "auctions/wishlist.html",{
        "listings": all_wishlisted
    })

def categories(request):
    method="get"
    listings_selected=""
    if request.method =="POST":
        selected_category = request.POST["category_link"]
        listings_selected = Listing.objects.filter(category=selected_category)
        method ="post"

    categories_list = []
    listings = Listing.objects.all()

    for listing in listings:
        if listing.category not in categories_list:
            categories_list.append(listing.category)

    return render(request, "auctions/categories.html",{
        "categories":categories_list,
        "listings": listings_selected,
        "method":method
    })

