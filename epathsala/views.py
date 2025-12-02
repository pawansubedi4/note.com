from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.db.models import Q 
from .models import comment,classes,subject,publication,unit1,exam1,unit,exam,major12

# Create your views here.
def index(request):
    data1=classes.objects.all()
    return render(request, 'index.html',{'data':data1})


    
@login_required
def home(request):
    user = request.user
    user.is_subscribed = True
    user.save()
    if request.user.staff_status:
        datas=unit.objects.all()
        data2=exam.objects.all()
        search_query = request.GET.get('search', '')
        if search_query:
            datas = datas.filter(Q(class1__num__icontains=search_query) | Q(sub__sub_name__icontains=search_query))
        return render(request, "staff/staff_pannel.html",{'units':datas , 'exams':data2})
    elif request.user.is_subscribed:
        c1="neb"
        data1=classes.objects.filter(
            type__num=c1,
        )
        return render(request, "home.html", {'data':data1})
    return render(request, 'unsubscribed.html')

def user_view(request):
    if request.user.staff_status:
        c1="neb"
        data1=classes.objects.filter(
            type__num=c1,
        )
        return render(request, "home.html", {'data':data1})



def for12(request,major):
    if request.user.is_subscribed:
        c1="11_12"
        major1=major
        data1=classes.objects.filter(
            type__num=c1,
        )
        return render(request, "classes/for12.html", {'data':data1,'major':major1})

    return render(request, 'unsubscribed.html')







def authView(request):
    if request.method == "POST":
        print("POST request received.")
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Form is valid.")
            form.save()
            return redirect("base:login")
        else:
            print("Form is invalid:", form.errors)
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})
import hmac
import hashlib
import base64



@login_required
def subscribe_view(request):
    pid = f"user-{request.user.id}"
    amount = 100
    txAmt = 10
    psc = 0
    pdc = 0
    tAmt = int(amount + txAmt + psc + pdc)
    success_url = request.build_absolute_uri('/payment-success/')
    failure_url = request.build_absolute_uri('/payment-fail/')
    esewa_url = "https://rc-epay.esewa.com.np/api/epay/main/v2/form"
    
    secret_key = '8gBm/:&EnhH.1/q'  # Must be bytes
    message_str = f"total_amount={tAmt},transaction_uuid={pid},product_code=EPAYTEST"
    def gensha256(key,message):
        key=key.encode('utf-8')
        message=message.encode('utf-8')
        hmac_sha256=hmac.new(key,message,hashlib.sha256)
        digest=hmac_sha256.digest()
        signature=base64.b64encode(digest).decode('utf-8')
        return signature




    message = gensha256(secret_key,message_str)

    

    context = {
        'esewa_url': esewa_url,
        'amt': amount,
        'txamt':txAmt,
        'pid': pid,
        'tAmt': tAmt,
        'su': success_url,
        'fu': failure_url,
        'sign':message,
    }
    return render(request, 'subscribe.html', context)
import json
@login_required

def payment_success(request):
    
    if request.method=="GET":
        data=request.GET.get('data')
        decoded_data= base64.b64decode(data).decode('utf-8')
        map_data=json.loads(decoded_data)
        if map_data.get('status')=="COMPLETE":
            user = request.user
            user.is_subscribed = True
            user.save()
            return render(request, 'payment_success.html')

@login_required
def payment_fail(request):
    return render(request, 'payment_fail.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email= request.POST.get('email')
        message = request.POST.get('message')
        comment.objects.create(name=name,email=email,message=message)
        return redirect('base:home')
    return render(request, 'contact.html')






@login_required
def subject1(request,id,tpye):
    if request.user.is_subscribed:
        class1=id
        type=tpye
        data2=subject.objects.filter(
            type__num=type,
        )
        return render(request, 'classes/subject.html',{'data':data2,'class1':class1,'type':type})
    return render(request, 'unsubscribed.html')

@login_required   
def subject12(request,id,tpye,major):
    if request.user.is_subscribed:
        class1=id
        type=tpye
        major1=major
        data2=subject.objects.filter(
            type__num=type,
            major__sub=major1
        )
        return render(request, 'classes/subject.html',{'data':data2,'class1':class1,'type':type})
    return render(request, 'unsubscribed.html')
@login_required
def publication1(request,sub,id,tpye,major):
    if request.user.is_subscribed:
        data2=publication.objects.filter(
            type__num=tpye,
        )
        return render(request, 'classes/publication.html',{'data':data2,'class':id ,'sub':sub,'type':tpye,'major1':major})
    return render(request, 'unsubscribed.html')

@login_required
def unit21(request,pub,sub,id,tpye,major):
    if request.user.is_subscribed:
        data4=unit.objects.filter(
            pub__pub_name=pub,
            sub__sub_name=sub,
            class1__num=id
        )
        data3=exam.objects.filter(
            sub__sub_name=sub,
            class1__num=id
            
        )
        return render(request, 'classes/unit.html',{'data12':data3,'data4':data4,'pub':pub,'sub':sub,'class1':id,'major':major})
    return render(request, 'unsubscribed.html')
@login_required
def unit22(request,uid,pub,sub,id):
    if request.user.is_subscribed:
        uid1=uid
        pub1=pub
        sub1=sub
        cla=id
        data2=unit.objects.filter(
            unit_num__name=uid1,
            pub__pub_name=pub1,
            sub__sub_name=sub1,
            class1__num=cla 
        )
        return render(request, 'classes/unit12.html',{'data':data2})
    return render(request, 'unsubscribed.html')
@login_required
def exam12(request,eid,pub,sub,id):
    if request.user.is_subscribed:
        uid1=eid
        pub1=pub
        sub1=sub
        cla=id

        data2=exam.objects.filter(
            ter__term=uid1,
            sub__sub_name=sub1,
            class1__num=cla
        )
        return render(request, 'classes/exam.html',{'data':data2})
    return render(request, 'unsubscribed.html')
@login_required
def allsub(request,pub,id,major):
    if request.user.is_subscribed:
        pub1=pub
        cla=id

        data2=unit.objects.filter(
            major__sub=major,
            class1__num=cla,
            pub__pub_name=pub1,
        )
        return render(request, 'classes/unit12.html',{'data':data2})
    return render(request, 'unsubscribed.html')
@login_required
def allunit(request,sub,pub,id):
    if request.user.is_subscribed:
        pub1=pub
        cla=id
        sub=sub

        data2=unit.objects.filter(
            class1__num=cla,
            pub__pub_name=pub1,
            sub__sub_name=sub
        )
        return render(request, 'classes/unit12.html',{'data':data2})
    return render(request, 'unsubscribed.html')
@login_required
def allexam(request,id,major):
    if request.user.is_subscribed:
        uid1=id
        data2=exam.objects.filter(
            class1__num=uid1,
            major__sub=major,
            
        )
        return render(request, 'classes/exam.html',{'data':data2})
    return render(request, 'unsubscribed.html')

def about(request):
    return render(request, 'about.html')

def term(request):
    return render(request, 'term.html')

def privacy(request):
    return render(request, 'privacy.html')


def major(request):
    tpye="11_12"
    data2=major12.objects.filter(
        type__num=tpye,
    )
    return render(request, 'classes/major.html',{'data':data2})




















#for staff views
from .forms import UnitsForm,ExamForm
from .models import comment

@login_required
def upload_units(request):
    if request.user.staff_status:
        if request.method == "POST":
            form = UnitsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('base:home')
        else:
            form = UnitsForm()
            return render(request, 'staff/upload_notes.html', {'form': form})
        
@login_required
def upload_exam(request):
    if request.user.staff_status:
        if request.method == "POST":
            form = ExamForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('base:views_exam')
        else:
            form = ExamForm()
            return render(request, 'staff/upload_exam.html', {'form': form})
        
def views_contact(request):
    if request.user.staff_status:
        data1=comment.objects.all()
        search_query = request.GET.get('search', '')
        if search_query:
            data1 = data1.filter(Q(name__icontains=search_query)|Q(email__icontains=search_query))
        return render(request, 'staff/views_contact.html', {'units': data1})
    

def views_exam(request):
    if request.user.staff_status:
        data1=exam.objects.all()
        search_query = request.GET.get('search', '')
        if search_query:
            data1 = data1.filter(Q(class1__num__icontains=search_query))
        return render(request, 'staff/views_exam.html', {'units': data1})

def del_units(request,id):
    if request.user.staff_status:
        try:
            u = unit.objects.get(id=id)
            u.delete()
        except unit.DoesNotExist:
            pass 
        return redirect('base:home')
    
def edit_units(request,id):
    if request.user.staff_status:
        if request.method=='POST':
            obj = unit.objects.get(id=id)
            class_id = request.POST.get('class1')
            obj.class1 = classes.objects.get(id=class_id)
            obj.sub = subject.objects.get(id=request.POST.get('sub'))
            obj.pub = publication.objects.get(id=request.POST.get('pub'))
            obj.unit_num = unit1.objects.get(id=request.POST.get('unit_num'))
            unit_pdf_file = request.FILES.get('unit_pdf')
            if unit_pdf_file:
                obj.unit_pdf = unit_pdf_file
                obj.save()
            return redirect('base:home')
        else:
            form = UnitsForm()
            u = unit.objects.get(id=id)
            return render(request, 'staff/edit_notes.html', {'units': u,'form': form})
        
def del_comments(request,id):
    if request.user.staff_status:
        try:
            u = comment.objects.get(id=id)
            u.delete()
        except comment.DoesNotExist:
            pass 
        return redirect('epathsala:views_contact')
    
def del_exam(request,id):
    if request.user.staff_status:
        try:
            u = exam.objects.get(id=id)
            u.delete()
        except exam.DoesNotExist:
            pass 
        return redirect('base:views_exam')
    
def edit_exam(request,id):
    if request.user.staff_status:
        if request.method=='POST':
            obj = exam.objects.get(id=id)
            ter_id = request.POST.get('ter')
            obj.ter = exam1.objects.get(id=ter_id)
            obj.class1 = classes.objects.get(id=request.POST.get('class1'))
            obj.sub = subject.objects.get(id=request.POST.get('sub'))
            unit_pdf_file = request.FILES.get('pdf')
            obj.scl = request.POST.get('scl')
            if unit_pdf_file:
                obj.pdf = unit_pdf_file
                obj.save()
            return redirect('base:views_exam')
        else:
            form = ExamForm()
            u = exam.objects.get(id=id)
            return render(request, 'staff/edit_notes.html', {'units': u,'form': form})






