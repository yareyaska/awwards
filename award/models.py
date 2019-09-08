from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    profile_photo= models.ImageField(upload_to = 'awards/', blank = True)
    bio=models.CharField(max_length =50)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    contact=models.CharField(max_length =50)
    def __str__(self):
        return self.bio
    def save_profile(self):
        self.save()
class Image(models.Model):
    image = models.ImageField(upload_to = 'landingpage/')
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=50)
    live_link = models.CharField(max_length=30)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.image_name

    '''return objects on database'''
    @classmethod
    def images_all(cls):
        posts = Image.objects.all()
        return posts

    '''save function'''
    def save_post(self):
        self.save()

    '''delete function'''
    def delete_post(self):
        self.delete()

    
class Rating(models.Model):
  RATINGS = (
      (1, '1'),
      (2, '2'),
      (3, '3'),
      (4, '4'),
      (5, '5'),
      (6,'6'),
      (7,'7'),
      (8,'8'),
      (9,'9'),
      (10,'10')
  )
  image = models.ForeignKey(Image)
  user = models.ForeignKey(User)
  usability_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
  design_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
  content_rating = models.IntegerField(default=0, choices=RATINGS, null=True)
  review = models.CharField(max_length=200)