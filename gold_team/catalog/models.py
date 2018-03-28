from django.db import models

# Create your models here.

class Hashtag(models.Model):
    """
    Model representing a hashtag (e.g. #YOLO #Covfefe etc.).
    """
    name = models.CharField(max_length=15, help_text="Enter a hashtag (e.g. #YOLO #Covfefe etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

class Post(models.Model):
    """
    Model representing a post.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular post across entire history")
    text = models.CharField(max_length=256)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey('Topic', on_delete=models.SET_NULL, null=True)
    upvote_count = models.IntegerField()
    hashtags = None #TODO: make this into a list of hashtags similar to genre in locallibrary
    reaction_counts = None #TODO: make this into a list of counts for each reaction
    
    # Foreign Key used because post can only have one user, but users can have multiple posts
    # User as a string rather than object because it hasn't been declared yet in the file.

    # This will need to be changed, but the idea might work somewhere else
    REACTION = (
        ('a', 'Angry'),
        ('f', 'Funny'),
        ('s', 'Sad'),
        ('w', 'Wow'))
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.text
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('post-detail', args=[str(self.id)])

class User(models.Model):
    """
    Model representing a user.
    """
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    post_history = None #TODO: make this into a list of posts the user has made

    class Meta:
        ordering = ["username"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular user instance.
        """
        return reverse('user-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {1}'.format(self.last_name,self.first_name)

class Topic(models.Model):
    """
    Model representing a topic.
    """
    text = models.CharField(max_length=200)
    creator = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    active_date = models.DateField()
    
class Feed(models.Model):
    """
    Model representing the main feed.
    """
    daily_topic = models.CharField(max_length=200)
    next_topic = models.Charfield(max_length=200)