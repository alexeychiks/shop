from django.urls import path, include

from clothes import views

urlpatterns = [
    path('', views.index, name='main'),
    path('category/<slug:slug>', views.products, name = 'products'),
    path('<slug:product_url>', views.product, name = 'product'),
    path('login/', views.BBLoginView.as_view(), name='login'),
    path('accounts/profile/', views.profile, name = 'profile'),
    path('logout/', views.BBLogoutView.as_view(), name='logout'),
    path('register/', views.user_register, name = 'register'),
    path ('<uidb64>/<token>/', views.activate_account,name='activate'),
]