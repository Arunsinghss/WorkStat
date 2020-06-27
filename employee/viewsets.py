from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, EmployeeSerializer, EmployeeDesignationSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, JsonResponse
from employee.models import Employee, EmployeeDesignation
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        params = request.data if request.data else request.POST
        username = params.get('username', '')
        password = params.get('password', '')

        user = authenticate(username=username, password=password)
        if user is not None:
            user.groups.add(Group.objects.get(name='employee'))
            user.save()
            login(request, user)
            token,_ = Token.objects.get_or_create(user=user)
            empdata = EmployeeSerializer(user.employee).data
            userdata = UserSerializer(user).data
            data = {'token': token.key, 'empdata':empdata, 'userdata':userdata}
            return JsonResponse({"message": "User Logged In Successfully...", "data":data}, status=200)
        return JsonResponse({"message": "Please Enter Valid Credentials..."}, status=400)


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create_user(self, kwargs):
        userkwargs = {
            'username': kwargs.get('username'),
            'first_name': kwargs.get('first_name'),
            'last_name': kwargs.get('last_name'),
            'email': kwargs.get('email'),
        }
        user = User.objects.filter(email=kwargs.get('email'))
        if not user:
            user = User.objects.create(**userkwargs)
        else:
            user.update(**userkwargs)
            user = user.first()
        user.set_password(kwargs.get('password'))
        user.save()
        token,_ = Token.objects.get_or_create(user=user)
        return user, token.key

    def create(self, request, *args, **kwargs):
        params = request.data if request.data else request.POST
        kwargs = {
            'username':  params.get('username', ''),
            'password':  params.get('password', ''),
            'first_name':  params.get('first_name', ''),
            'last_name':  params.get('last_name', ''),
            'email':  params.get('email', ''),
            'age':  params.get('emp_age', ''),
            'exp':  params.get('emp_exp', ''),
            'designation':  params.get('designation', '')
        }

        for key, val in kwargs.items():
            if val == '':
                return JsonResponse({"message": "Please Provide all the fields ..."}, status=400)

        try:
            designation = kwargs.get('designation')
            designation = EmployeeDesignation.objects.get(id=designation)
            user, token = self.create_user(kwargs)
            emp,_ = Employee.objects.get_or_create(user=user, designation=designation, emp_age=kwargs.get('age'), emp_exp=kwargs.get('experience'))
            empdata = self.serializer_class(emp).data
            userdata = UserSerializer(user).data
            return JsonResponse({"message": "Employee Added Successfully...", "data": {'empdata': empdata, 'userdata': userdata}}, status=200)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)



class EmployeeDesignationViewset(viewsets.ModelViewSet):
    queryset = EmployeeDesignation.objects.all()
    serializer_class = EmployeeDesignationSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        params = request.data if request.data else request.POST
        name = params.get('name', '')
        description = params.get('description', '')

        if name.strip():
            if EmployeeDesignation.objects.filter(name=name).exists():
                return JsonResponse({"message": "Designation with same name already exists..."}, status=400)
            else:
                EmployeeDesignation.objects.create(
                    name=name, description=description)
                return JsonResponse({"message": "Employee Designation Added Successfully..."}, status=200)

        return JsonResponse({"message": "Please Enter Valid Designation Name..."}, status=400)

    def update(self, request, pk=None, *args, **kwargs):
        return
