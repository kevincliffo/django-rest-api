from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', views.ArticleViewSet, basename='articles')
router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('api/', include(router.urls)),
    # path('', views.index, name="index"),
    # path('articles/', views.article_list, name="articles"),
    # path('article/<int:pk>/', views.article_details, name="article"),
    # path('articles/', views.ArticleList.as_view(), name="articles"),
    # path('article/<int:id>/', views.ArticleDetails.as_view(), name="article"),
]
