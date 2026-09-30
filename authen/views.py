# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SignupAPI(APIView):

    def post(self, request):

        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')

        if not all([first_name, last_name, email, username, password]):
            return Response(
                {"error": "All fields are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "Email already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "Username already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password
        )

        return Response(
            {"message": "Signup Successful"},
            status=status.HTTP_201_CREATED
        )

class SigninAPI(APIView):

    def post(self, request):

        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            username=username,
            password=password
        )

        if user is None:
            return Response(
                {"error": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "message": "Signin Successful",
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            },
            status=status.HTTP_200_OK
        )                    
           


@login_required(login_url='signin')

def profile(request):
    # current active user details will be available in current request's user details
    data = request.user
    return render(request, 'profile.html', {'data':data})

@login_required(login_url='signin')
def update_profile(request):
    # current user
    user = request.user
    if request.method == 'POST':
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')
        email = request.POST.get('email')
        un = request.POST.get('un')

        # to check whether email is updated and is not as same as previous value
        if User.objects.filter(email = email).exists():
            messages.error(request, "Email cannot be same as previous Email ID...")
            return redirect('update_profile')
        # to check whether usernname is updated and is not same as previous value
        if User.objects.filter(username = un).exists():
            messages.error(request, "Username already exists, provide a new username..")
            return redirect('update_profile')

        # updation of user details
        user.first_name = fn
        user.last_name = ln
        user.email = email
        user.username = un
        user.save()

        messages.success(request, "Profile details aree updated successfully..")
        return render(request, 'profile.html', {'data':user})
    return render(request, 'update_profile.html', {'data':user})

@login_required(login_url='signin')
def update_password(request):
    # current user
    user = request.user
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # to check whether old password == existing password --> user.check_password(old_password)
        if not(user.check_password(old_password)):
            messages.error(request, "Old password is not matching..")
            return redirect('update_password')

        # to check whether the new password is not same as old password
        if new_password == old_password:
            messages.error(request, "New password should not be same as Old password..")
            return redirect('update_password')

        # to check wheth3er the new password is equal to confirm password
        if new_password != confirm_password:
            messages.error(request, "New password does not macth with the confirm password..")
            return redirect('update_password')

        # to encrypt the password and update --> set_password
        user.set_password(confirm_password)
        user.save()

        update_session_auth_hash(request, user)
        messages.success(request, "Password has been updated successfully!!")
        return render(request, 'profile.html', {'data':user})
    return render(request, 'update_password.html')

@login_required(login_url='signin')
def signout(request):
    # current user
    user = request.user
    if request.method == 'POST':
        logout(request)
        messages.success(request, "LOGGED out successfully!!")
        return redirect('signin')
    return render(request, 'signout.html')