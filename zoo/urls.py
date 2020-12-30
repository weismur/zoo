
from django.contrib import admin
from django.urls import path
from firstapp import views
from django.views.generic import TemplateView
from django.conf.urls import include, url

admin.autodiscover()



urlpatterns = [
    path('catalog/',views.great, name='great'),
    url(r'^admin/backups/', include('dbbackup_ui.urls')),
    url(r'^admin/', admin.site.urls),
    path('zoo/', views.index, name='home'),
    path('animal/', views.index_animal, name='animal'),
    path('area/', views.index_habitat_area, name='area'),
    path('user/', views.index_user, name='user'),
    path('ration/', views.index_feeding_ration, name='ration'),
    path('bird/', views.index_bird, name='bird'),
    path('reptile/', views.index_reptile, name='reptile'),
    #пути для животных
    path('animal/add/', views.view_animal.add_animal, name='add_animal'),
    path("animal/del/", views.view_animal.del_animal, name="del_animal"),
    path("animal/up/", views.view_animal.update_animal, name="update_animal"),
    #пути для зон обитания
    path('area/adde/', views.view_habitat_area.add_habitat_area, name='add_habitat_area'),
    path("area/dele/", views.view_habitat_area.del_habitat_area, name="del_habitat_area"),
    path("area/upe/", views.view_habitat_area.update_habitat_area, name="update_habitat_area"),
    #пути для пользователей
    path('user/addc/', views.view_user.add_user, name='add_author'),
    path("user/delc/", views.view_user.del_user, name="del_data"),
    path("user/upc/", views.view_user.update_user, name="update_data"),
    #пути для рационов
    path('ration/addo/', views.view_feeding_ration.add_feeding_ration, name='add_ration'),
    path("ration/delo/", views.view_feeding_ration.del_feeding_ration, name="del_ration"),
    path("ration/upo/", views.view_feeding_ration.update_feeding_ration, name="update_ration"),
    #пути для птиц
    path('bird/addb/', views.view_bird.add_bird, name='add_bird'),
    path("bird/delb/", views.view_bird.del_bird, name="del_bird"),
    path("bird/upb/", views.view_bird.update_bird, name="update_bird"),
    #пути для рептилий
    path('reptile/addr/', views.view_reptile.add_reptile, name='add_reptile'),
    path("reptile/delr/", views.view_reptile.del_reptile, name="del_reptile"),
    path("reptile/upr/", views.view_reptile.update_reptile, name="update_reptile"),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]