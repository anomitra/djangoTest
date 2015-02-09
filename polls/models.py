from django.db import models

class ques(models.Model):
    ques_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    ques = models.ForeignKey(ques)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)