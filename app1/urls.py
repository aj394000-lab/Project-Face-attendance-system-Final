from django.urls import path
from . import views

urlpatterns = [
    # --- Home & Auth ---
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    # --- Student Registration & Capture ---
    path('capture_student/', views.capture_student, name='capture_student'),
    path('selfie-success/', views.selfie_success, name='selfie_success'),
    
    # --- Attendance Marking ---
    path('capture-and-recognize/', views.capture_and_recognize, name='capture_and_recognize'),

    # --- Manage Students ---
    path('students/', views.student_list, name='student-list'), 
    path('students/<int:pk>/', views.student_detail, name='student-detail'),
    path('students/<int:pk>/authorize/', views.student_authorize, name='student-authorize'),
    path('students/<int:pk>/delete/', views.student_delete, name='student-delete'),

    # --- Attendance Details ---
    path('students/attendance/', views.student_attendance_list, name='student_attendance_list'),

    # --- Camera Settings (DOUBLE ENTRY TO FIX ALL ERRORS) ---
    
    # 1. Create
    path('camera-config/', views.camera_config_create, name='camera_config_create'), # For views.py
    path('camera-config/', views.camera_config_create, name='camera-config-create'), # For HTML
    
    # 2. List (Fixes Home Page AND Cancel Button)
    path('camera-config/list/', views.camera_config_list, name='camera_config_list'), # For views.py & Home
    path('camera-config/list/', views.camera_config_list, name='camera-config-list'), # For HTML
    
    # 3. Update
    path('camera-config/update/<int:pk>/', views.camera_config_update, name='camera_config_update'),
    path('camera-config/update/<int:pk>/', views.camera_config_update, name='camera-config-update'),
    
    # 4. Delete
    path('camera-config/delete/<int:pk>/', views.camera_config_delete, name='camera_config_delete'),
    path('camera-config/delete/<int:pk>/', views.camera_config_delete, name='camera-config-delete'),
]