from Blog.views import index, profile, single_info, category_info, getlogin, getlogout, create, login_profile, get_update, get_delete, registration, get_topic, create_topics
from django.urls import path

app_name='Blog'
urlpatterns = [
    path('', index.as_view(), name='index'),
    path('profile/<name>', profile,  name='profile'),
    path('single/<int:id>', single_info, name="single"),
    path('topic/<abc>',category_info, name="category"),
    path('login',getlogin, name='login'),
    path('logout', getlogout, name='logout'),
    path('create', create, name='create'),
    path('login_profile', login_profile, name='login_profile'),
    path('update/<int:pid>', get_update, name='update'),
    path('delete/<int:pid>', get_delete, name='delete'),
    path('register', registration, name='register'),
    path('topics', get_topic, name='topic'),
    path('create/topics',create_topics,name='create_topic'),

]
