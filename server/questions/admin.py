from django.contrib import admin
from .models import QuestionMedia, Question, SolutionMedia

admin.site.register(QuestionMedia)
admin.site.register(Question)
admin.site.register(SolutionMedia)
