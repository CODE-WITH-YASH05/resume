from django.urls import path
from accounts.views import admin_login, admin_dashboard, admin_logout, create_school_settings, about_us_view
from accounts.views import gallery_views

urlpatterns = [
    path('api/admin/login/', admin_login),
    path('api/admin/dashboard/', admin_dashboard),
    path('api/admin/logout/', admin_logout),
    path('api/admin/school-settings/', create_school_settings),
    path('api/admin/school-settings/about-us/', about_us_view),
    path('gallery/categories/', gallery_views.gallery_categories , name='gallery_categories'),
    path('gallery/albums/<str:category_name>/' , gallery_views.albums_by_category , name='albums_by_category'),

]
