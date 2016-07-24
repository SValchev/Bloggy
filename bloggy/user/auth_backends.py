from django.db.models import Q
from django.http import Http404

from .models import CustomUser

class EmailAuthBackend(object):
    def authenticate(self, username=None, password=None):
        try:
            user = CustomUser.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username))
            if user.check_password(password):
                return user
            raise CustomUser.DoesNotExist('User does not exists.')
        except User.DoesNotExist:
            raise CustomUser.DoesNotExist('User does not exists.')

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
