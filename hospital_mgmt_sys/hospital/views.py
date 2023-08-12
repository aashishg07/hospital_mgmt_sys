from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import Doctor, Patient, Appointment

from django.contrib import messages, auth

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

def view_doctor(request):
    if not request.user.is_staff:
        return render(request, 'login.html')
    doctor = Doctor.objects.all()
    doc = {'doctor': doctor}
    return render(request, 'view_doctor.html', doc)

def delete_doctor(request, pk):
    if not request.user.is_staff:
        return render(request, 'login.html')
    doctor = Doctor.objects.get(id=pk)
    doctor.delete()
    return redirect('view_doctor')

def add_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        special = request.POST["special"]
        
        Doctor.objects.create(name = name, phone = phone, special = special)
        return redirect('view_doctor')
    
    return render(request, 'add_doctor.html')


def add_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        name = request.POST["name"]
        phone = request.POST["phone"]
        gender = request.POST["gender"]
        age = request.POST["age"]
        problem = request.POST["problem"]

        Patient.objects.create(name = name, phone = phone, gender = gender, age = age, problem = problem)
        return redirect('view_patient')

    return render(request, 'add_patient.html')


def view_patient(request):
    if not request.user.is_staff:
        return render(request, 'login.html')
    patient = Patient.objects.all()
    pat = {'patient': patient}
    return render(request, 'view_patient.html', pat)


def delete_patient(request, pk):
    if not request.user.is_staff:
        return render(request, 'login.html')
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return redirect('view_patient')


def add_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method == "POST":
        doctor = request.POST["doctor"]
        patient = request.POST["patient"]
        date = request.POST["date"]
        time = request.POST["time"]

        doctor2 = Doctor.objects.filter(name = doctor).first()
        patient2 = Patient.objects.filter(name = patient).first()

        Appointment.objects.create(doctor_app = doctor2, patient_app = patient2, date = date, time = time)

        return redirect('view_appointment')
    
    appointment = {'doctor': doctor1, 'patient': patient1}
    return render(request, 'add_appointment.html', appointment)


def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appointment.objects.all()
    app = {'appointment':appointment}
    return render(request, 'view_appointment.html', app)

def delete_appointment(request, pk):
    if not request.user.is_staff:
        return redirect('login')
    app = Appointment.objects.get(id=pk)
    app.delete()
    return redirect('view_appointment')


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            auth_login(request, user)
            messages.success(request, "Logged-in successfully!")
            return redirect('index')
        else:
            messages.error(request, 'Username and Password incorrect!')
            # return redirect('login')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)
    messages.success(request, "Logged out successfully!")
    return render(request, 'login.html')

