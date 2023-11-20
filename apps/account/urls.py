from django.urls import path
from .views import AccountRegisterView, LoginView, \
    AccountRetrieveUpdateView, AccountListView, ClientListAPIView

app_name = 'account'

urlpatterns = [
    path('register/', AccountRegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('detail/update/<int:pk>/', AccountRetrieveUpdateView.as_view()),
    path('list/', AccountListView.as_view(), name='get_list'),
    path('client/', ClientListAPIView.as_view()),
]