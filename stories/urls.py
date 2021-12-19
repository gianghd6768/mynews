from django.urls import path
from stories import views

app_name = 'stories'
urlpatterns = [
    path('Masterbase.html', views.Masterbase),
    path('', views.index, name='trang_chu'),
    path('trang_chu/', views.index, name='trang_chu'),
    path('lien_he/', views.contact, name='lien_he'),
    path('contact_ok/', views.contact_ok, name='contact_ok'),
    path('nha_dat_ban/', views.blogs, name='nha_dat_ban'),
    path('nha_dat_cho_thue/', views.single, name='nha_dat_cho_thue'),
    path('tin_tuc/', views.news, name='tin_tuc'),
    path('chi_tiet/<int:id>/', views.detail_single, name='chi_tiet'),
    path('tim_kiem/', views.search, name='tim_kiem'),

]