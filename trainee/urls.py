from django.urls import path, include
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from.views import render_pdf_view

urlpatterns = [
    path('', views.base, name="base"),
    path('logout/',views.logoutUser, name="logout"),   
    path('profile/',views.profile, name="profile"),
    path('timetable/',views.fullcalendar, name="fullcalendar"),
    path('payments/',views.payments, name="payments"),   
    path('book/',views.book, name="book"),   
    path('home/',views.home, name="home"),   
    path('report/',views.render_pdf_view, name="test-view"),   
    path('profile/edit',views.edit, name="edit"),   
    path('profile/changepassword',views.change, name="change"), 
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),   
    

    
   
]