from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout
from master.services.UserService import UserService
from master.services.ProductService import ProductService
from master.services.CategoryService import CategoryService

userService = UserService()
productService = ProductService()
catService = CategoryService()


def front(request):
    return render(request, "front.html")


def homepage(request):
    search = request.GET.get("search", "")
    category = request.GET.get("category", "")
    selected_category = request.GET.get("category", "")
    if selected_category:
        selected_category = int(selected_category)

    if search and category:
        products = productService.searchProductsByCategory(search, category)
    elif search:
        products = productService.searchProducts(search)
    elif category:
        products = productService.getProductsByCategory(category)
    else:
        products = productService.getAllProducts()
    cart = request.session.get("cart", {})
    cart_count = sum(cart.values())
    categories = catService.getAll()
    return render(
        request,
        "homepage.html",
        {
            "products": products,
            "cart_count": cart_count,
            "categories": categories,
            "selected_category": selected_category,
        },
    )


def signin(request):

    if request.method == "POST":

        user = userService.signin(request)

        if user:

            login(request, user)

            return redirect("homepage")

        else:

            messages.error(request, "Invalid Username or Password")
            return render(request, "signin.html")

    return render(request, "signin.html")


from django.contrib import messages


def signup(request):
    
    if request.method == "POST":
        result = userService.signup(request)
        if result == "Username already exists":
            messages.error(request, result)
            return render(request, "signup.html")
        messages.success(request, result)
        return redirect("signin")
    return render(request, "signup.html")


def logoutUser(request):

    logout(request)

    return redirect("signin")


def addProduct(request):
    return render(request, "addproduct.html")


def founder(request):
    return render(request, "founder.html")
