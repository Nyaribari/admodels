from enum import unique
import uuid
from django.db import models
from django.db.models import constraints
import datetime

class Tweep(models.Model):

    class Category(models.IntegerChoices):
        CATEGORY_1 = 1, 'More than 5 years of tweeting'
        CATEGORY_2 = 2, 'More than 3.5 years of tweeting'
        CATEGORY_3 = 3, 'More than 2 years of tweeting'
        CATEGORY_4 = 4, 'More than 1 year of tweeting'
        CATEGORY_5 = 5, 'Less than a year of tweeting'
    username = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rating_category = models.PositiveSmallIntegerField(choices=Category.choices, default=Category.CATEGORY_5, help_text='For how long have you been tweeting ?')
    year_born = models.PositiveSmallIntegerField(default=2000)
    daily_tweet_time = models.DurationField(default=datetime.timedelta(hours=1))
    

    class Meta:
        verbose_name = 'Tweep KOT'
        verbose_name_plural = 'Tweeps KOT'
        ordering = ['rating_category']
        constraints = [
            models.CheckConstraint(check=models.Q(year_born__lte=datetime.date.today().year-18), name='users_of_age_only'),
            #Already made unique in models but class meta has that constraint too
            models.UniqueConstraint(fields=['username','email'], name = 'unique_user')
        ]


    def __str__(self):
        return '%s, %s' % ('@'+self.username,self.name)


    
    def save(self, *args, **kwargs):

        if self.daily_tweet_time >= datetime.timedelta(hours=0.5):
            self.rating_category = self.Category.CATEGORY_5


        super(Tweep,self).save(*args, **kwargs)
        