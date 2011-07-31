from django.db import models
from django.contrib.auth.models import User
 
from recipes.models import FoodType
 
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    summary = models.CharField(max_length = 500)
    specialty = models.ManyToManyField(FoodType)
    
    # This makes objects from this model readable in the admin and in shell
    def __unicode__(self):
        return '%s [%s]' % (self.user, self.pk)
    
    # if the UserProfile does not exist then create one
    # adds a property to the User model for convenience instead of having to do get_profile()
    # see http://www.turnkeylinux.org/blog/django-profile
    User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
 

