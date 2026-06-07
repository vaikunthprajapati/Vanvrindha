from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

from master.services.ProductService import ProductService
from master.services.CategoryService import CategoryService
from master.services.UserService import UserService
from master.services.OrderService import OrderService

from django.contrib.auth.decorators import login_required

service = ProductService()
catService = CategoryService()
userService = UserService()
orderService = OrderService()


def signup(request):

    if request.method == "POST":

        result = userService.signup(request)

        return HttpResponse(result)

    return render(request, "signup.html")


def signin(request):
    print("SIGNIN VIEW CALLED")

    if request.method == "POST":

        print("POST RECEIVED")

        user = userService.signin(request)

        print("USER =", user)

        if user:

            login(request, user)

            return redirect("homepage")

        else:

            return HttpResponse("Invalid Username or Password")

    return render(request, "signin.html")


def logoutUser(request):

    logout(request)

    return redirect("signin")


@login_required
def addProduct(request):
    if not request.user.is_superuser:
        return HttpResponse("Access Denied")
    if request.method == "POST":

        result = service.addProduct(request)
        product_name = request.POST.get("pname")
        messages.success(request,f"{product_name} added successfully")
        return redirect('addProduct')

    categories = catService.getAll()

    return render(request, "admin/addproduct.html", {"categories": categories})


@login_required
def productList(request):
    if not request.user.is_superuser:
        return HttpResponse("Access Denied")
    products = service.getAllProducts()
    return render(request, "admin/productlist.html", {"products": products})


@login_required
def editProduct(request, id):
    if not request.user.is_superuser:
        return HttpResponse("Access Denied")
    if request.method == "POST":

        result = service.updateProduct(request, id)

        return redirect("products")

    product = service.getProductById(id)

    return render(request, "admin/editproduct.html", {"product": product})


@login_required
def deleteProduct(request, id):
    if not request.user.is_superuser:
        return HttpResponse("Access Denied")
    service.deleteProduct(id)
    return redirect("products")


@login_required
def productDetail(request, id):

    product = service.getProductById(id)

    return render(
        request,
        "productdetail.html",
        {"product": product, "cart_count": len(request.session.get("cart", []))},
    )


@login_required
def addToCart(request, id):
    cart = request.session.get("cart", {})

    id = str(id)

    if id in cart:

        cart[id] += 1

    else:

        cart[id] = 1

    request.session["cart"] = cart

    return redirect("homepage")


@login_required
def cart(request):
    cart_data = request.session.get("cart", {})
    ids = list(cart_data.keys())
    products = service.getProductsByIds(ids)
    cart_items = []

    for product in products:

        qty = cart_data[str(product[0])]
        subtotal = float(product[3]) * qty
        cart_items.append({"product": product, "qty": qty, "subtotal": subtotal})
    total = 0
    for p in products:
        qty = cart_data[str(p[0])]
        total += float(p[3]) * qty
    item_count = sum(cart_data.values())
    return render(
        request,
        "cart.html",
        {"cart_items": cart_items, "total": total, "item_count": item_count},
    )


@login_required
def removeFromCart(request, id):
    cart = request.session.get("cart", {})
    id = str(id)
    if id in cart:
        del cart[id]
    request.session["cart"] = cart
    return redirect("cart")


@login_required
def increaseQuantity(request, id):

    cart = request.session.get("cart", {})

    id = str(id)

    if id in cart:

        cart[id] += 1

    request.session["cart"] = cart

    return redirect("cart")


@login_required
def decreaseQuantity(request, id):

    cart = request.session.get("cart", {})

    id = str(id)

    if id in cart:

        cart[id] -= 1

        if cart[id] <= 0:

            del cart[id]

    request.session["cart"] = cart

    return redirect("cart")


@login_required
def checkout(request):

    cart_data = request.session.get("cart", {})

    ids = list(cart_data.keys())

    products = service.getProductsByIds(ids)

    total = 0

    for p in products:

        qty = cart_data[str(p[0])]

        total += float(p[3]) * qty

    if request.method == "POST":

        fullname = request.POST["fullname"]

        phone = request.POST["phone"]

        address = request.POST["address"]

        order_id = orderService.addOrder(
            request.user.id, fullname, phone, address, total
        )

        for p in products:

            pid = p[0]

            qty = cart_data[str(pid)]

            orderService.addOrderItem(order_id, pid, qty, p[3])

        request.session["cart"] = {}

        return redirect("ordersuccess")

    return render(request, "checkout.html", {"products": products, "total": total})


@login_required
def orderSuccess(request):

    return render(request, "ordersuccess.html")


@login_required
def orders(request):

    if not request.user.is_superuser:

        return HttpResponse("Access Denied")

    orders = orderService.getAllOrders()

    return render(request, "admin/orders.html", {"orders": orders})


@login_required
def updateOrderStatus(request, order_id):

    if not request.user.is_superuser:

        return HttpResponse("Access Denied")

    status = request.GET.get("status")

    orderService.updateStatus(order_id, status)

    return redirect("orders")


def location(request):
    return render(request, "location.html")
