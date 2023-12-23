import razorpay
from django.shortcuts import render, redirect

from Frontend.models import contactdb, signupdb, cartdb, bookingdb
from ShopApp.models import productdb
from ShopApp.models import catdb
from django.contrib import messages
# Create your views here.

def shop_index(request):
    cat = catdb.objects.all()
    return render(request,"Shop_index.html",{'cat':cat})

def product_page(request):
    product = productdb.objects.all()
    cat = catdb.objects.all()
    return render(request,"Product.html",{'product':product , 'cat':cat})

def product_filter(request,cat_name):
    cat = catdb.objects.all()
    data = productdb.objects.filter(catname=cat_name)
    return render(request,"product_filter.html",{'data':data, 'cat':cat })

def single_product(request,pro_id):
    data = productdb.objects.get(id=pro_id)
    return render(request,"single_product.html",{'data':data})

def about_us(request):
    return render(request,"about_us.html")

def contact_us(request):
    return render(request,"contact_us.html")

def contactdata(request):
    if request.method == "POST":
        cona = request.POST.get('contactname')
        ema = request.POST.get('email')
        conum = request.POST.get('contactnumber')
        sub = request.POST.get('subject')
        sugg = request.POST.get('suggestion')
        obj = contactdb(contactname=cona,email=ema,contactnumber=conum,subject=sub,suggestion=sugg)
        obj.save()
        return redirect(contact_us)


# USER LOGIN AND SIGN UP

def signup_user(request):
    return render(request,"signup_user.html")

def signupdata(request):
    if request.method == "POST":
        fna = request.POST.get('fullname')
        mob = request.POST.get('mobile')
        ema = request.POST.get('email')
        una = request.POST.get('username')
        pas = request.POST.get('password')
        obj = signupdb(fullname=fna,mobile=mob,email=ema,username=una,password=pas)
        obj.save()
        return redirect(signup_user)

def login_user(request):
    return render(request,"login_user.html")

def Userlogin(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if signupdb.objects.filter(username=un,password=pwd).exists():
            request.session['username']=un
            request.session['password']=pwd
            messages.success(request,"Login Success")
            return redirect(shop_index)
        else:
            messages.error(request,"Invalid username or password")
            return redirect(login_user)
    else:
        return redirect(login_user)

def Userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_user)

# cart

def cart_page(request):
    data = cartdb.objects.filter(username=request.session['username'])
    total_price=0
    for i in data:
        total_price=total_price+i.totalprice
    return render(request,"Cart_page.html", {'data':data, 'total_price':total_price})

def cartdata(request):
    if request.method == "POST":
        una = request.POST.get('username')
        pna = request.POST.get('productname')
        qua = request.POST.get('quantity')
        tpri = request.POST.get('totalprice')
        des = request.POST.get('description')
        obj = cartdb(username=una,productname=pna,quantity=qua,totalprice=tpri,description=des)
        obj.save()
        messages.success(request,"Added to Cart")
        return redirect(cart_page)

def delete_cart(request,pro_id):
    data = cartdb.objects.filter(id=pro_id)
    data.delete()
    messages.error(request,"Item deleted From cart")
    return redirect(cart_page)

def checkout_page(request):
    data = cartdb.objects.filter(username=request.session['username'])
    total_price = 0
    for i in data:
        total_price = total_price + i.totalprice
    return render(request,"Checkout.html",{'data':data , 'total_price':total_price})



def bookingdata(request):
    if request.method=="POST":
        fna =  request.POST.get('fullname')
        una =  request.POST.get('username')
        addr =  request.POST.get('address')
        cty =  request.POST.get('city')
        pin =  request.POST.get('pincode')
        mob =  request.POST.get('mobile')
        ema =  request.POST.get('email')
        prona =  request.POST.get('productname')
        ttpri = request.POST.get('totalprice')
        obj = bookingdb(fullname=fna,username=una,address=addr,city=cty,pincode=pin,mobile=mob,email=ema,productname=prona,totalprice=ttpri)
        obj.save()
        return redirect(payment_product)




def payment_product(request):

    last_object = bookingdb.objects.order_by('-id').first()
    payy = last_object.totalprice
    payy_str_hotel = str(payy)
    for ptotl in payy_str_hotel:
        print(ptotl)

    if request.method == "POST":
        amount=50000
        order_currency='INR'
        client = razorpay.Client(auth=('rzp_test_jcVIUHkalKhqwa','Gwt5sgqFhjy0ur0qJUKQxTwY'))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
    return render(request,"pay.html",{'payy_str_hotel':payy_str_hotel})