import datetime

from django.utils import timezone
from django.test import TestCase

from polls.models import Question

class QuestionMethodTests(TestCase):

    def test_recent_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.recent(), False)
    
    def test_recent_with_new_question(self):
        
        #SHOULD RETURN TRUE FOR A NEW QUESTION
        
        time=timezone.now() - datetime.timedelta(hours=2)
        new_question=Question(pub_date=time)
        self.assertEqual(new_question.recent(), True)
        
    def test_recent_with_old_question(self):
        
        #SHOULD RETURN FALSE FOR AN OLD QUESTION
        
        time=timezone.now() - datetime.timedelta(days=31)
        old_question=Question(pub_date=time)
        self.assertEqual(old_question.recent(), False)