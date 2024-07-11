from django.urls import path
from .views import *

urlpatterns = [
    path("", BlogListView.as_view(), name="bloglist"),
    path("about/", about, name="about"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blogdetail"),
    path("blogcreate/", BlogCreateView.as_view(), name="blogcreate"), 
    path("blogedit/<int:pk>/", BlogUpdateView.as_view(), name="blogupdate"),  
    path("blogdelete/<int:pk>/", BlogDeleteView.as_view(), name="blogdelete"),  
]
