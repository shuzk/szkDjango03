from django.conf.urls import url  # 导入url函数

from booktest import views  # 导入视图模块

urlpatterns = [
    url(r'^$', views.index),  # 建立url和views.index视图函数的关联
]
