from django.urls import path

from interviewprocess_controll.cam2 import *
# from .crud.questions_retrieve import *
from .crud.imageupload import *
from .crud.videocam import *
# from .views import *

urlpatterns =[
    # path('questions',questions.as_view()),
    path('img',ImageUploader.as_view()),
    path('interview',interview,name='interview'),
    path('videocam',madhu.as_view(),name='interview'),
    path('interviewend',camStatue,name='interviewend'),
]
