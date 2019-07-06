from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate,login,logout
import review.views as rv
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('write-review', views.writeReview, name='write-review'),
    path('search-review', views.searchReview, name='search-review'),
    path('review', views.review, name='review'),
    path('register', views.register, name='register'),
    path('login', views.userlogin, name='login'),
    path('about', views.about, name='about'),
    path('logout', views.userlogout, name='logout'),
    path('review-detail/<int:id>/', views.detailReview, name='detail'),
    # path('write-comment', views.comment, name='comment'),
    # path('comment-detail', views.detailComment, name='detail-comment'),
    
]