from django.contrib import admin
from quizz.models import Quizz
class QuizzAdmin(admin.ModelAdmin):
    list_display=['question','choice1','choice2','choice3','choice4','answer']
    admin.site.register(Quizz)
