# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model


# class EmailBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(email=email)
#         except UserModel.DoesNotExist:
#             return None
#         if user.check_password(password):
#             return user
#         return None


from django.contrib.auth.backends import ModelBackend
from .models import CustomUser


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Django admin používa "username", aj keď ty máš email
        email = username or kwargs.get("email")
        if email is None or password is None:
            return None
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except CustomUser.objects.model.DoesNotExist:
            return None
