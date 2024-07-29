from django.urls import path
from task_application.views import RegisterView,LoginView,LogoutView,TaskManagementView,TaskManagementViewId,TaskstatusFilter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)


urlpatterns = [

    path('register/',RegisterView.as_view(),name="register"),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('task/',TaskManagementView.as_view(),name='task'),
    path('taskid/<int:id>/',TaskManagementViewId.as_view(),name='taskid'),
    path('taskfilter/',TaskstatusFilter.as_view({'get': 'list'}), name="taskfilter"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]