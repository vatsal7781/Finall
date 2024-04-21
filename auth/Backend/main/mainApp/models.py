from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

##Auth
class AppUserManager(BaseUserManager):
	def create_user(self, email, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save()
		return user
	def create_superuser(self, email, password=None):
		if not email:
			raise ValueError('An email is required.')
		if not password:
			raise ValueError('A password is required.')
		user = self.create_user(email, password)
		user.is_superuser = True
		user.save()
		return user


class AppUser(AbstractBaseUser, PermissionsMixin):
	user_id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=50, unique=True)
	username = models.CharField(max_length=50)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	objects = AppUserManager()
	def __str__(self):
		return self.username
	

##Form

class Test(models.Model):
  Id = models.AutoField(primary_key=True)
  Username = models.CharField(max_length=50, null=False)	
  Fname = models.CharField(max_length=50, null=False)

class Nodes(models.Model):
  Id = models.AutoField(primary_key=True)
  Ip = models.CharField(max_length=50, null=False)
  Username = models.CharField(max_length=50, null=False)
  Password = models.CharField(max_length=50, null=False)
  OS = models.CharField(max_length=30, null=False)
  SysoId = models.CharField(max_length=25,null=True, blank=True )
  Node_type = models.CharField(max_length=20, null=False)
  Fake_ip = models.CharField(max_length=50, null=False,unique=True)
  Live = models.SmallIntegerField(default=1, null=False)
  ParentId = models.IntegerField( null=True, blank=True)
  is_Intermediate = models.SmallIntegerField( null=True, blank=True)
  is_Banned = models.SmallIntegerField(default=0 ,null=True, blank=True)
  Operator = models.CharField(max_length=50, null=False)
  ServerName = models.CharField(max_length=10 ,null=True, blank=True)
  HostName = models.CharField(max_length=10, null=False)
  Circle = models.CharField(max_length=100, null=False)
  Status = models.CharField(max_length=50,null=True, blank=True )
  Comment = models.CharField(max_length=500,null=True, blank=True )
  Cygwin_Version = models.CharField(max_length=50,null=True, blank=True )
  Transfer_Status = models.CharField(max_length=500,null=True, blank=True )
  Installation_Status = models.CharField(max_length=500,null=True, blank=True )
  Time_Sync = models.SmallIntegerField()
  Key_Enabled = models.IntegerField(null=True, blank=True)
	

class Ports(models.Model):
  TunnleId = models.AutoField(primary_key=True)
  NodeId = models.ForeignKey(Nodes,max_length=100, null=False, on_delete=models.CASCADE, related_name='ports', db_column='NodeId')
  RemotePort = models.IntegerField( null=False)
  LocalPort = models.IntegerField( null=False)
  Direction = models.CharField(max_length=100, null=False)
  SocketPath = models.CharField(max_length=100, null=False)
  Status = models.CharField(max_length=50, null=False)
  Comment = models.CharField(max_length=2000, null=False)
  def Id(self):		
    return self.NodeId.Id
	
# dropdown models

class Operator(models.Model):
    name = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['name']
    def __str__(self):
			        return self.name
    

class OS(models.Model):
    name = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['name']
    def __str__(self):
			        return self.name
    

class Circle(models.Model):
    name = models.CharField(max_length=100)
    REQUIRED_FIELDS = ['name']
    def __str__(self):
			        return self.name

# class Test1(models.Model):
#   Id = models.AutoField(primary_key=True)
#   Username = models.CharField(max_length=50, null=False)	
#   Fname = models.CharField(max_length=50, null=False)