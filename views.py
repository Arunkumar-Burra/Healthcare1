
from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient, Prescription, Doctor, UserCustom, session
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
import re
import uuid
# Create your views here.
def Home_page(request):
    if request.session.get['key']:
        a = request.session.get("key")
        print("hello world")
        aff = session.objects.
        if a in aff:pass
        elif a in session.username:return render(request,'Home.html')
        else:
            return HttpResponse("need to login")



def login_page(request):

    if request.method == "POST":
        username = request.POST['username'].strip()
        password = request.POST['password']
        print(username, password)
        regex = '^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+.([a-zA-Z0-9{2,4}])+$'
        if (re.search(regex, username)):
            a = UserCustom.objects.filter(email=username, password=password)
        else:
            a = UserCustom.objects.filter(username=username, password=password)


        if a:
            request.session['key'] = uuid.uuid4()
            key = request.session['key']
            print(key)


            ins = session(username=username,key=key)
            ins.save()

            return HttpResponseRedirect(reverse('enquiry:Home'))

    return render(request,'login.html')


def signup_page(request):
    if request.method=="POST":

        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
        print(firstname, lastname, email, username, password)
        a = UserCustom(firstname=firstname, lastname=lastname, email=email, username=username, password=password)
        a.save()
        return HttpResponseRedirect(reverse("enquiry:submit"))

    return render(request,'signup.html')

def submit(request):
    res = HttpResponse()
    res.write("<h1 style=color:green;>form is submitted successfully</h1>")
    return res


def patient_page(request):
    # retrieving the data from database
    # get all patient objects from db
    data = Patient.objects.all()
    context = {"patient": data}
    return render(request,'patient.html', context)

def prescription(request):
    # get all the prescription from db
    data = Prescription.objects.all()
    context = {"prescription": data}
    return render(request, 'prescription.html',context)

def detail_prescription(req, pr_id):
    print('You are asking patient: ', pr_id)
    return HttpResponse('detail prescription')

def doctor_page(request):
    data = Patient.objects.all()
    context = {"patients": data}
    return render(request, 'doctor.html', context)

class pres(generic.ListView):
    model = Prescription
    template_name = 'prescription.html'
    context_object_name = 'all_prescriptions'


def doctor_patient_view(request):
    data = Patient.objects.all()
    context = {"patients": data}
    return render(request, 'doctor_patient.html', context)

def patient_all_prescriptions(request, p_pk):
    data = Prescription.objects.filter(patient__pk=p_pk)
    context = {"prescriptions": data} #[Prescription(), Prescription(), ]
    return render(request, 'all_pre.html', context)