from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from server.users.api.views import UserViewSet
from server.questions.api.views import QuestionViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("questions", QuestionViewSet)


app_name = "api"
urlpatterns = router.urls
