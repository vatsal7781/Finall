from django.contrib.auth import get_user_model, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Nodes
from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.db import transaction

from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer,NodeSerializer
from rest_framework import permissions, status

from .utils import generate_fake_ip


from .validations import custom_validation, validate_email, validate_password
from .models import (Nodes, Ports, Test, OS, Operator, Circle)

class UserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		clean_data = custom_validation(request.data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		data = request.data
		assert validate_email(data)
		assert validate_password(data)
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)
			return Response(serializer.data, status=status.HTTP_200_OK)
        
        
## Step 1 Create a forget password API View(similar to user login)
## Retrieve email from input
## Logic to send email (add data to table- OTP Current date time +10)

## Response from Email basis- Success or Failed
## Otp & new pass input field if response success ||  

## STEP 2 NEW API Retrieve Email, Otp and New Password from the front end. Verify from the database(OTP)
## If valid then change the password in the database and remove otp entry. Respond with Success

class UserLogout(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)
	
class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	##
	def get(self, request):
		serializer = UserSerializer(request.user) ##instance of UserSerializer class. and passing argument to UserSerializer class. 
		return Response({'user': serializer.data}, status=status.HTTP_200_OK)




@csrf_exempt
def NodesFormView(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Ip = data.get('Ip', '')
        Username = data.get('Username', '')
        Password = data.get('Password', '')
        OS = data.get('OS', '')
        # SysoId = data.get('SysoId', '')
        Node_type = data.get('Node_type', '')
        # Fake_ip = data.get('Fake_ip', '')

        # Live = data.get('Live', '')
        # ParentId = data.get('ParentId', '')
        # is_Intermediate = data.get('is_Intermediate', '')
        # is_Banned = data.get('is_Banned', '')
        Operator = data.get('Operator','')
        # ServerName = data.get('ServerName', '')
        HostName = data.get('HostName', '')
        Circle = data.get('Circle', '')
        # Status = data.get('Status', '')
        # Comment = data.get('Comment', '')
        # Cygwin_Version = data.get('Cygwin_Version', '')
        # Transfer_Status = data.get('Transfer_Status', '')
        # Installation_Status = data.get('Installation_Status', '')
        Time_Sync = data.get('Time_Sync', '')
        # Key_Enabled = data.get('Key_Enabled', '')

        try:
            with transaction.atomic():
                fake_ip = generate_fake_ip(Operator)
                # Create a new User instance and save it to the database
                node = Nodes(
                    Ip=Ip,
                    Username=Username,
                    Password=Password,
                    OS=OS,
                    # SysoId=SysoId,
                    Node_type=Node_type,
                    Fake_ip=fake_ip,
                    # Live=Live,
                    # ParentId=ParentId,
                    # is_Intermediate=is_Intermediate,
                    # is_Banned=is_Banned,
                    Operator=Operator,
                    # ServerName=ServerName,
                    HostName=HostName,
                    Circle=Circle,
                    # Status=Status,
                    # Comment=Comment,
                    # Cygwin_Version=Cygwin_Version,
                    # Transfer_Status=Transfer_Status,
                    # Installation_Status=Installation_Status,
                    Time_Sync=Time_Sync,
                    # Key_Enabled=Key_Enabled
                )
                node.save()
                return JsonResponse({'message': 'Nodes form filled and added successfully', 'node': model_to_dict(node)}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def getNodeById(request, nodeId):
    try:
        # Use 'id' instead of 'Id' in the filter
        node_instance = Nodes.objects.get(Id=nodeId)
        # Serialize the node instance using the NodeSerializer
        serialized_node = NodeSerializer(node_instance).data
        return JsonResponse(serialized_node)
    except Nodes.DoesNotExist:
        return JsonResponse({'error': 'Node not found'}, status=404)

@csrf_exempt
def PortsFormView(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        NodeId = data.get('NodeId', '')
        RemotePort = data.get('RemotePort', '')
        LocalPort = data.get('LocalPort', '')
        Direction = data.get('Direction', '')
        SocketPath = data.get('SocketPath', '')
        Status = data.get('Status', '')
        Comment = data.get('Comment', '')
        print('Received Data:', data)        
        try:
            node_instance = Nodes.objects.get(Id=NodeId)
        except Nodes.DoesNotExist:
            # Handle the case where the node does not exist
            return JsonResponse('Invalid NodeId', status=400)

        # Create a new User instance and save it to the database
        port = Ports(
            NodeId=node_instance,
            RemotePort=RemotePort,
            LocalPort=LocalPort,
            Direction=Direction,
            SocketPath=SocketPath,
            Status=Status,
            Comment=Comment)
        port.save()

        return JsonResponse({'message': 'Ports instance created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=400)

        
def get_dropdown_options(request):
    os_options = OS.objects.values_list('name', flat=True)
    circle_options = Circle.objects.values_list('name', flat=True)
    operator_options = Operator.objects.values_list('name', flat=True)

    return JsonResponse({
        'os_options': list(os_options),
        'circle_options': list(circle_options),
        'operator_options': list(operator_options),
    })


@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('Username', '')
        fname = data.get('Fname', '')

        # Create a new User instance and save it to the database
        user = Test(Username=username, Fname=fname)
        user.save()

        return JsonResponse({'message': 'User added successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)