from django.db import models
class  Event(models.Model):

  CATEGORY_CHOICES  = [
    ('CON', 'Concert'),
    ('SPR', 'Sports'),
    ('TEC', 'Technology'),
    ('ART', 'Art'),
  ]

  title  =  models.CharField(max_length=200)
  description  =  models.TextField()
  date  =  models.DateField()
  location  =  models.CharField(max_length=100)
  category  =  models.CharField(max_length=3, choices=CATEGORY_CHOICES, default='CON')
  participant_count  =  models.IntegerField(default=0)
  is_active  =  models.BooleanField(default=True)

  def  __str__(self):
    return  self.title
