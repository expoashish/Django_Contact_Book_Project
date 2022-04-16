from django.urls import path
from . import views

app_name = 'contact_book_app'

urlpatterns = [
    path('loginpage/', views.loginPage, name="loginpage"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.index, name='index'),
    path('index_message', views.index_message, name='index_message'),
    path('add', views.new_contact, name='new_contact'),
    path('submit-form',views.submit_contact, name='submit_contact'),
    path('upload/', views.image_upload_view),
    path('delete_contact/<int:id>', views.delete_contact, name='delete_contact'),
    path('detail/<int:id>', views.detail_contact, name='detail_contact'),
    path('edit/<int:id>', views.edit_contact, name='edit_contact'),
    path('contactus', views.contact_page, name='contact_page'),
    path('aboutus', views.about_page, name='about_page'),
    path('userprofile', views.UserProfile, name='userprofile'),

]