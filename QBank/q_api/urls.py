from django.urls import path, include
from .views import QuestionViewSet
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register('question', QuestionViewSet, basename='question')

urlpatterns = [
    path('viewset/', include(router.urls))
]