from django.urls import path
from . import views
from .views import add_user, NodesFormView,PortsFormView, getNodeById,get_dropdown_options

# getNodeIds

urlpatterns = [
	path('register', views.UserRegister.as_view(), name='register'),
	path('login', views.UserLogin.as_view(), name='login'),
	path('logout', views.UserLogout.as_view(), name='logout'),
	path('user', views.UserView.as_view(), name='user'), 
  path('add_user', add_user, name='add_user'),
  path('nodesForm', NodesFormView, name='nodesForm'),## for nodes table form
  path('portsForm', PortsFormView, name='portsForm'),## for ports table form
  path('nodes/<int:nodeId>/', getNodeById, name='get_node_by_id'),
  path('get_dropdown_options', get_dropdown_options, name='get_dropdown_options')
	# path('getNodeIds', getNodeIds, name='getNodeIds'),

	# path('user1', views.UserView.as_view(), name='user1'), ## for nodes table form
	# path('user2', views.UserView.as_view(), name='user2'),## for ports table form
]