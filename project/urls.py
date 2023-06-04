"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from comment.views import Questions_list,Questions_details,Questions_edit,delete_question


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/' , Questions_list),
    path('blog/<int:question_id>' , Questions_details),
    path('blog/<int:question_id>/edit' , Questions_edit),
    path('blog/<int:question_id>/delete' , delete_question),

]
