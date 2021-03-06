import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    ques_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.ques_text
    def recent(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    recent.admin_order_field = 'pub_date'
    recent.boolean = True
    recent.short_description = 'Published recently?'


class Choice(models.Model):
    ques = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        vote=str(self.votes)
        retstr=self.choice_text+" -- "+vote
        return retstr