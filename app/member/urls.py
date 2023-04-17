from django.urls import path
from member import views

app_name = "member"

urlpatterns = [
    path('create/', views.CreateMemberView.as_view(), name="create"),
    path('token/', views.MemberAuthToken.as_view(), name="token"),
    path('profile/', views.MemberProfileView.as_view(), name="profile"),
]
