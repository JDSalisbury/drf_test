from rest_framework.response import Response
from rest_framework import status


def check_list(func):
    def w(self, request, *args, **kwargs):
        user = request.user
        print(request.user)
        if user is 'admin':
            return func(self, request, *args, **kwargs)
        else:
            return Response("Admins Only", status=status.HTTP_401_UNAUTHORIZED)
    return w
