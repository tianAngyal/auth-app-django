from django.shortcuts import render

# Create your views here.

from rest_framework.authtoken.models import Token
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpRequest
import json
from django.views.decorators.csrf import ensure_csrf_cookie


def login_user(request):
    print(request)
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        user = authenticate(request, email=email, password=password)

        # print("login type:", type(login), login)

        if user is not None:
            login(request, user)
            return JsonResponse({
                "success": True,
                "message": "Login successful",
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "full_name": user.full_name
                }
            })
        else:
            return JsonResponse({
                "success": False,
                "message": "Invalid credentials"
            }, status=201)
    else:
        return JsonResponse({
            "success": False,
            "message": "Only POST requests are allowed"
        }, status=405)


def logout_user(request):
    # print(request.headers)
    # print("logout type:", type(logout), logout)
    # print(request.user)
    # headers = dict(request.headers)
    # return JsonResponse({"headers": headers})

    if not request.method == "GET":
        return JsonResponse({"success": False, "message": "Invalid method. - Use GET"}, status=405)

    if not request.user.is_authenticated:
        return JsonResponse({"succes": False, "message": "Only authenticated user can logout."}, status=401)
    else:
        logout(request)
        return JsonResponse({"success": True, "message": "User logged out"}, status=200)


def signup_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except Exception as e:
            return JsonResponse({"error": "Invalid Json"}, status=400)

        try:
            username = data.get("username")
            password1 = data.get("password1")
            # password2=data.get("password2")
            first_name = data.get("first_name", "")
            last_name = data.get("last_name", "")
            email = data.get("email", "")
            phone = data.get("phone", "")
        except Exception as e:
            return JsonResponse({"error": "Invalid data"}, status=400)

        user = CustomUser.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password1,
            email=email,
            phone=phone
        )

        return JsonResponse({"message": "User created"}, status=201)

    else:
        return JsonResponse({"error": "Invalid method"}, status=400)


@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({"message": "CSRF cookie set"})


def get_user_info(request):
    if request.method != "GET":
        return JsonResponse({"error": "Invalid method"}, status=405)

    if not request.user.is_authenticated:
        return JsonResponse({"error": "User not authenticated"}, status=401)

    user = request.user
    return JsonResponse({"success": True,
                        "message": "Login successful",
                         "user": {
                             "id": user.id,
                             "email": user.email,
                             "full_name": user.full_name
                         }
                         })
