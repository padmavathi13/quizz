from django.db import models
class Quizz(models.Model):
    question=models.CharField(max_length=150);
    choice1=models.CharField(max_length=150);
    choice2=models.CharField(max_length=150);
    choice3=models.CharField(max_length=150);
    choice4=models.CharField(max_length=150);
    answer=models.CharField(max_length=150);
