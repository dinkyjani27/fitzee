from datetime import datetime, date

from django.shortcuts import render, redirect
from .models import login, item, exercise, deficiency, blog, diet, contactus, feedback , order ,placeorder
from django.contrib import messages
from django.db.models import Sum



def index(request):
    fetchitem = item.objects.all()[0:8]
    print(fetchitem)
    return render(request, 'index.html', {'products': fetchitem})
    # try:
    #     if request.session.is_empty():
    #         return render(request, 'login.html')
    #     else:
    #         try:
    #             uid = request.session['log_id']
    #             user = login.objects.get(id=uid)
    #
    #         except login.DoesNotExist:
    #             user = None
    #         return render(request, 'index.html')
    # except:
    #     pass


def blogs(request):
    getblog = blog.objects.all()
    print(getblog)
    return render(request, 'blog.html', {'blog': getblog})





def exercises(request):
    uid = request.session['log_id']
    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    getexercise = exercise.objects.all().filter(de_id=deffid)
    print(getexercise)
    return render(request, 'exercise.html', {'exercises': getexercise})


def loginpage(request):
    return render(request, 'login.html')


def vwg(request):
    from datetime import datetime
    datetime.today().strftime('%Y-%m-%d')
    uid = request.session['log_id']
    uemail = request.session['log_user']
    data = login.objects.get(id=uid)
    getdate = data.l_date
    print(getdate)
    tdate = date.today()
    print(tdate)
    ldays = ( tdate - getdate)
    print(ldays.days)
    minusdays = 15 - ldays.days
    print(minusdays)

    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(food_type="Vegetarian", weight_type="Weight-gain", de_id=deffid)[0:3]
    print(fetchdiet)
    if minusdays<1:
        try:

            print('aaa\naaa')
            import smtplib

            gmail_user = 'fitzeeforhealth@gmail.com'
            gmail_password = 'fitzee@1234'

            sent_from = gmail_user
            to = [uemail]
            subject = 'Reminder from Fitzee Health'
            body = 'Seems like you forgot your password for DocVault.\n ' \
                   'Your new password for your DocVault Account is ' \
                   ' '


            email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, ", ".join(to), subject, body)

            try:
                smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                smtp_server.ehlo()
                smtp_server.login(gmail_user, gmail_password)
                smtp_server.sendmail(sent_from, to, email_text)
                smtp_server.close()
                print("Email sent successfully!")
            except Exception as ex:
                print("Something went wrong….", ex)
            return render(request, 'weightgain1.html', {'diet': fetchdiet , 'leftday':minusdays})
        except:
            pass
    return render(request, 'weightgain1.html', {'diet': fetchdiet , 'leftday':minusdays})


def vwgdaywise(request, id):
    from datetime import datetime
    datetime.today().strftime('%Y-%m-%d')
    uid = request.session['log_id']
    data = login.objects.get(id=uid)
    getdate = data.l_date
    print(getdate)
    tdate = date.today()
    print(tdate)
    ldays = (tdate - getdate)
    print(ldays.days)
    minusdays = 15 - ldays.days
    print(minusdays)

    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(food_type="Vegetarian", weight_type="Weight-gain", de_id=deffid, day=id)
    print(fetchdiet)
    return render(request, 'weightgain1.html', {'diet': fetchdiet,'leftday':minusdays})


def vwl(request):
    from datetime import datetime
    datetime.today().strftime('%Y-%m-%d')
    uid = request.session['log_id']
    data = login.objects.get(id=uid)
    getdate = data.l_date
    print(getdate)
    tdate = date.today()
    print(tdate)
    ldays = (tdate - getdate)
    print(ldays.days)
    minusdays = 15 - ldays.days
    print(minusdays)
    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(food_type="Vegetarian", weight_type="Weight-loose", de_id=deffid)[0:3]
    print(fetchdiet)
    return render(request, 'weightloose1.html', {'diet': fetchdiet,'leftday':minusdays})


def vwldaywise(request, id):
    from datetime import datetime
    datetime.today().strftime('%Y-%m-%d')
    uid = request.session['log_id']
    data = login.objects.get(id=uid)
    getdate = data.l_date
    print(getdate)
    tdate = date.today()
    print(tdate)
    ldays = (tdate - getdate)
    print(ldays.days)
    minusdays = 15 - ldays.days
    print(minusdays)

    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(food_type="Vegetarian", weight_type="Weight-loose", de_id=deffid, day=id)
    print(fetchdiet)
    return render(request, 'weightloose1.html', {'diet': fetchdiet,'leftday':minusdays})


def nwg(request):
    from datetime import datetime
    datetime.today().strftime('%Y-%m-%d')
    uid = request.session['log_id']
    data = login.objects.get(id=uid)
    getdate = data.l_date
    print(getdate)
    tdate = date.today()
    print(tdate)
    ldays = (tdate - getdate)
    print(ldays.days)
    minusdays = 15 - ldays.days
    print(minusdays)

    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(food_type="Non-Vegetarian", weight_type="Weight-gain", de_id=deffid)[0:3]
    print(fetchdiet)
    return render(request, 'weightgain2.html', {'diet': fetchdiet,'leftday':minusdays})


def nwgdaywise(request, id):
    from datetime import datetime
    datetime.today().strftime('%Y-%m-%d')
    uid = request.session['log_id']
    data = login.objects.get(id=uid)
    getdate = data.l_date
    print(getdate)
    tdate = date.today()
    print(tdate)
    ldays = (tdate - getdate)
    print(ldays.days)
    minusdays = 15 - ldays.days
    print(minusdays)

    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(food_type="Non-Vegetarian", weight_type="Weight-gain", de_id=deffid, day=id)
    print(fetchdiet)
    return render(request, 'weightgain2.html', {'diet': fetchdiet,'leftday':minusdays})


def nwl(request):
    from datetime import datetime
    datetime.today().strftime('%Y-%m-%d')
    uid = request.session['log_id']
    data = login.objects.get(id=uid)
    getdate = data.l_date
    print(getdate)
    tdate = date.today()
    print(tdate)
    ldays = (tdate - getdate)
    print(ldays.days)
    minusdays = 15 - ldays.days
    print(minusdays)

    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(food_type="Non-Vegetarian", weight_type="Weight-loose", de_id=deffid)[0:3]
    print(fetchdiet)
    return render(request, 'weightloose2.html', {'diet': fetchdiet,'leftday':minusdays})


def nwldaywise(request, id):
    from datetime import datetime
    datetime.today().strftime('%Y-%m-%d')
    uid = request.session['log_id']
    data = login.objects.get(id=uid)
    getdate = data.l_date
    print(getdate)
    tdate = date.today()
    print(tdate)
    ldays = (tdate - getdate)
    print(ldays.days)
    minusdays = 15 - ldays.days
    print(minusdays)

    fetchdef = login.objects.get(id=uid)
    deffid = fetchdef.de_id
    fetchdiet = diet.objects.all().filter(food_type="Non-Vegetarian", weight_type="Weight-loose", de_id=deffid, day=id)
    print(fetchdiet)
    return render(request, 'weightgain2.html', {'diet': fetchdiet,'leftday':minusdays})


def products(request):
    getproducts = item.objects.all()[0:6]
    print(getproducts)
    return render(request, 'products.html', {'products': getproducts})


def productcatwise(request, id):
    getproducts = item.objects.all().filter(category=id)
    print(getproducts)
    return render(request, 'products.html', {'products': getproducts})


def register(request):
    fetchdef = deficiency.objects.all()
    return render(request, 'register.html', {'def': fetchdef})


def secblog(request, id):
    fetchblog = blog.objects.get(id=id)
    return render(request, 'secblog.html', {'blog': fetchblog})


def single(request, id):
    fetchproduct = item.objects.get(id=id)
    return render(request, 'single.html', {'item': fetchproduct})


def weightgain1(request):
    return render(request, 'weightgain1.html')


def weightgain2(request):
    return render(request, 'weightgain2.html')


def weightloose1(request):
    return render(request, 'weightloose1.html')


def weightloose2(request):
    return render(request, 'weightloose2.html')


def mailus(request):
    return render(request, 'mail.html')

def orderview(request):
    return render(request, 'order.html')

def viewdata(request):
    if request.method == 'POST':
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        address = request.POST.get("address")
        age = request.POST.get("age")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        gender = request.POST.get("gender")
        defid = request.POST.get("Deficiency")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("number")

        logindata = login(firstname=firstname, lastname=lastname,address=address, age=age, height=height, phone_no=phone, weight=weight,
                          gender=gender, de_id=deficiency(id=defid), email_id=email, password=password, role=2,
                          status=1)
        logindata.save()
        messages.info(request, 'Registered Successfully. you can login now')
        return render(request, 'login.html')
    else:
        messages.info(request, 'error occured')
        print("errrorrr")

    return render(request, 'login.html')


def viewblg(request):
    if request.method == 'POST':
        uid = request.session['log_id']
        wr_name = request.POST.get("wr_name")
        b_name = request.POST.get("b_name")
        b_desc1 = request.POST.get("b_desc1")
        b_desc2 = request.POST.get("b_desc2")
        b_media = request.FILES['b_media']

        blogdata = blog(l_id=login(id=uid), wr_name=wr_name, b_name=b_name, b_desc1=b_desc1, b_desc2=b_desc2,
                        b_media=b_media)
        blogdata.save()
        messages.info(request, 'Blog Inserted Successfully.')
        return render(request, 'blog.html')
    else:
        messages.info(request, 'error occured')
        print("errrorrr")

    return render(request, 'blog.html')


def checklogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = login.objects.get(email_id=email, password=password)
            request.session['log_user'] = user.email_id
            request.session['log_id'] = user.id
            request.session.save()
            fetchitem = item.objects.all()[0:8]
            print(fetchitem)

        except login.DoesNotExist:
            user = None

        if user is not None:
            messages.info(request, 'Login Successfull')
            return render(request, 'index.html', {'products': fetchitem})

        else:
            messages.info(request, 'account does not exit plz sign in')
    return render(request, 'index.html')


def logout(request):
    try:
        del request.session['log_user']
        del request.session['log_id']
    except:
        pass
    return render(request, 'login.html')


# Create your views here.
def insertcontact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email_id = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("msg")
        contactdata = contactus(name=name, email_id=email_id, subject=subject, message=message)
        contactdata.save()
        messages.success(request, 'Query Submitted.')
        return render(request, 'mail.html')
    else:
        messages.error(request, 'error occured')
        print("errrorrr")

    return render(request, 'mail.html')


def insertfeedback(request):
    if request.method == 'POST':
        uid = request.session['log_id']
        review = request.POST.get("star")
        comment = request.POST.get("comment")
        fetchitem = item.objects.all()[0:8]
        print(fetchitem)
        feedbackdata = feedback(l_id=login(id=uid), review=review, comment=comment)
        feedbackdata.save()
        messages.success(request, 'Feedback Inserted Successfully.')
        return render(request, 'index.html', {'products': fetchitem})
    else:
        messages.error(request, 'error occured')
        print("errrorrr")

    return render(request, 'index.html')


def addtocart(request, id):
    pid = id
    uid = request.session['log_id']
    fetchprice = item.objects.get(id=pid)
    price = fetchprice.i_price
    print(price)
    getproducts = item.objects.all()[0:8]
    cartdata = order(i_id=item(id=pid), loginid=login(id=uid), o_quantity=1, total=price , o_status=1)
    cartdata.save()
    messages.success(request, 'Product Added In Your Cart')
    return render(request, 'index.html',{'products': getproducts})

def deleteproduct(request, id):
    obj = order.objects.get(i_id=id,o_status=1)
    obj.delete()
    uid = request.session['log_id']
    fetchcart = order.objects.filter(loginid=uid,o_status=1)
    print(fetchcart)
    fetchpid = order.objects.values('i_id').filter(loginid=uid)
    print(fetchpid)
    fetchpro = item.objects.filter(id__in=fetchpid).values()
    print(fetchpro)
    return redirect(checkout)

def ucart(request, id):
    num = request.POST.get("qua")
    price = request.POST.get("price")
    q = int(num)
    t = int(price)
    total = q * t
    obj = order.objects.get(i_id=id,o_status=1)
    obj.o_quantity = num
    obj.total = total
    obj.save()
    uid = request.session['log_id']
    fetchcart = order.objects.filter(loginid=uid)
    print(fetchcart)
    fetchpid = order.objects.values('i_id').filter(loginid=uid)
    print(fetchpid)
    fetchpro = item.objects.filter(id__in=fetchpid).values()
    print(fetchpro)
    return redirect(checkout)


def checkout(request):
    uid = request.session['log_id']
    add = login.objects.filter(id=uid).first()
    nadd = add.address
    print(nadd)
    fetchcart = order.objects.filter(loginid=uid,o_status=1)

    if not fetchcart:
        fetchcart = None
    else:
        fetchcart = fetchcart

    print(fetchcart)
    fetchpid = order.objects.values('i_id').filter(loginid=uid)
    print(fetchpid)
    fetchpro = item.objects.filter(id__in=fetchpid).values()
    print(fetchpro)
    items = order.objects.filter(loginid=uid,o_status=1).aggregate(Sum('total'))
    print(items)
    return render(request, 'checkout.html',{'products':fetchpro , 'cart':fetchcart,'login':nadd,'total':items})

def vieworder(request):
    uid = request.session['log_id']
    add = login.objects.filter(id=uid).first()
    nadd = add.address
    print(nadd)
    fetchcart = order.objects.filter(loginid=uid, o_status=0)

    if not fetchcart:
        fetchcart = None
    else:
        fetchcart = fetchcart

    print(fetchcart)
    fetchpid = order.objects.values('i_id').filter(loginid=uid)
    print(fetchpid)
    fetchpro = item.objects.filter(id__in=fetchpid).values()
    print(fetchpro)
    items = order.objects.filter(loginid=uid).aggregate(Sum('total'))
    print(items)
    return render(request, 'order.html', {'products': fetchpro, 'cart': fetchcart, 'login': nadd, 'total': items})

def placeorderitem(request):
    uid = request.session['log_id']
    fetchcart = order.objects.filter(loginid=uid, o_status=1).update(o_status=0)
    # fetchcart.o_status = 0
    # fetchcart.save()
    return redirect(index)


# def viewadd(request,id):
#     if request.method == 'POST':
#         uid = request.session['log_id']
#         oid =id
#         address = request.POST.get("address")
#
#         addressdata = placeorder(l_id=login(id=uid),orderid=order(id=oid), address=address)
#         addressdata.save()
#         messages.success(request, 'Data Inserted Successfully.')
#         return render(request, 'checkout.html')
#     else:
#         messages.error(request, 'error occured')
#         print("errrorrr")

# return render(request, 'checkout.html')

