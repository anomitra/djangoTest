import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    ques_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.ques_text
    def recent(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    ques = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        vote=str(self.votes)
        retstr=self.choice_text+" -- "+vote
        return retstr