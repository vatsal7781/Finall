from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import Nodes, Ports

UserModel= get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model=UserModel
    fields='__all__'
  def create(self, clean_data):
    user_obj =UserModel.objects.create_user(email=clean_data['email'],password=clean_data['password'])
    user_obj.username=clean_data['username']
    user_obj.save()
    #logic to sending approval for user to admin. library to send mails
    return user_obj

class UserLoginSerializer(serializers.Serializer):
  email=serializers.EmailField()
  password=serializers.CharField()

  def check_user(self, clean_data):
    user =authenticate(username=clean_data['email'],password=clean_data['password'])
    if not user: #user.isapproved==False, If false then error(must be approved user)
      raise serializers.ValidationError("User not found")
    return user

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model=UserModel
    fields=('email','username')

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nodes
        fields = ('Id','Ip','Username','Password','OS','SysoId','Node_type','Fake_ip','Live','ParentId','is_Intermediate','is_Banned','Operator','ServerName','HostName','Circle','Status','Comment','Cygwin_Version','Transfer_Status','Installation_Status','Time_Sync','Key_Enabled')


# class NodesSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Nodes
#     fields = ('Id','Ip','Username','Password','OS','SysoId','Node_type','Fake_ip','Live','ParentId','is_Intermediate','is_Banned','Operator','ServerName','HostName','Circle','Status','Comment','Cygwin_Version','Transfer_Status','Installation_Status','Time_Sync','Key_Enabled')

# class PortSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Ports
#     fields = ('TunnleId','NodeId','RemotePort','LocalPort','Direction','SocketPath','Status','Comment')