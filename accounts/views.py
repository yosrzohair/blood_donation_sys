from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Citizen, Institute
from .serializers import CitizenSerializer, InstituteSerializer

### TEMPLATE-BASED VIEWS ###

def index(request):
    return render(request, 'index.html')

# CITIZEN SIGNUP (Template)
def CitizenSignupView(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        national_id = request.POST['national_id']
        email = request.POST['email']
        blood_type = request.POST['blood_type']
        city = request.POST['city']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('citizen_signup')

        citizen = Citizen.objects.create(
            first_name=first_name,
            last_name=last_name,
            national_id=national_id,
            email=email,
            blood_type=blood_type,
            city=city,
            address=address,
            password=make_password(password)
        )
        messages.success(request, "Account created successfully! Please sign in.")
        return redirect('citizen_signin')

    return render(request, 'accounts/citizen_signup.html')


# CITIZEN SIGNIN (Template)
def CitizenSigninView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            citizen = Citizen.objects.get(email=email)
            if check_password(password, citizen.password):
                messages.success(request, "Login successful!")
                return redirect('home')  # Replace 'home' with the actual dashboard
            else:
                messages.error(request, "Invalid credentials!")
                return redirect('citizen_signin')
        except Citizen.DoesNotExist:
            messages.error(request, "User not found!")
            return redirect('citizen_signin')

    return render(request, 'accounts/citizen_signin.html')


# INSTITUTE SIGNUP (Template)
def InstituteSignupView(request):
    if request.method == 'POST':
        name = request.POST['name']
        institute_type = request.POST['institute_type']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        city = request.POST['city']
        address = request.POST['address']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('institute_signup')

        institute = Institute.objects.create(
            name=name,
            institute_type=institute_type,
            phone_number=phone_number,
            email=email,
            city=city,
            address=address,
            password=make_password(password)
        )
        messages.success(request, "Account created successfully! Please sign in.")
        return redirect('institute_signin')

    return render(request, 'accounts/institute_signup.html')


# INSTITUTE SIGNIN (Template)
def InstituteSigninView(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            institute = Institute.objects.get(email=email)
            if check_password(password, institute.password):
                messages.success(request, "Login successful!")
                return redirect('home')  # Replace 'home' with the actual dashboard
            else:
                messages.error(request, "Invalid credentials!")
                return redirect('institute_signin')
        except Institute.DoesNotExist:
            messages.error(request, "User not found!")
            return redirect('institute_signin')

    return render(request, 'accounts/institute_signin.html')

### REST API VIEWS ###

# CITIZEN SIGNUP (API)
class CitizenSignupAPI(APIView):
    def post(self, request):
        serializer = CitizenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(password=make_password(request.data['password']))  # Hash password
            return Response({"message": "Citizen created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CITIZEN SIGNIN (API)
class CitizenSigninAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            citizen = Citizen.objects.get(email=email)
            if check_password(password, citizen.password):
                return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials!"}, status=status.HTTP_401_UNAUTHORIZED)
        except Citizen.DoesNotExist:
            return Response({"error": "User not found!"}, status=status.HTTP_404_NOT_FOUND)


# INSTITUTE SIGNUP (API)
class InstituteSignupAPI(APIView):
    def post(self, request):
        serializer = InstituteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(password=make_password(request.data['password']))  # Hash password
            return Response({"message": "Institute created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# INSTITUTE SIGNIN (API)
class InstituteSigninAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            institute = Institute.objects.get(email=email)
            if check_password(password, institute.password):
                return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials!"}, status=status.HTTP_401_UNAUTHORIZED)
        except Institute.DoesNotExist:
            return Response({"error": "User not found!"}, status=status.HTTP_404_NOT_FOUND)
