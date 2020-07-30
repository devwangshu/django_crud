from django.urls import path

from Student import views

app_name = 'Student'

urlpatterns = [
    path('', views.add_student, name='add_student'),
    path('student_manage', views.student_manage, name='student_manage'),
    path('student_edit/<int:pk>', views.student_edit, name='student_edit'),
    path('delete_student/<int:pk>', views.delete_student, name='delete_student'),
    path('show_graph', views.show_graph, name='show_graph'),
    
    path('fetch_sensor_values_ajax', views.fetch_sensor_values_ajax, name='fetch_sensor_values_ajax'),

]