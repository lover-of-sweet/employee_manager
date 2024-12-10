from django.conf.urls import url

from . import views

app_name = 'manager'

urlpatterns = [
    url(r'^positions_json/', views.positions, name='positions'),
    url(r'^employees_list', views.employee_list, name='employees_list'),
    url(r'^add_position/', views.add_positions, name='add_position'),
    url(r'^positions/', views.positions_templates, name="postitions_templates"),
    url(r'^delete_position/', views.delete_positions, name="delete_position"),
    url(r'^position_view/(?P<pk>[0-9]+)/$', views.position_view, name="position_view"),
    url(r'position/', views.position_template, name='position_template'),
    url(r'^position_update/', views.position_update, name='position_update'),
    url(r'^employees', views.employees, name='employees'),
    url(r'^add_employee', views.add_employee, name='add_employee'),
    url(r'^delete_employee', views.delete_employee, name='delete_employee'),
    url(r'^employee_view/(?P<pk>[0-9]+)/$', views.employee_view, name='employee_view'),
    url(r'^employee_update', views.employee_update, name="employee_update"),
]
