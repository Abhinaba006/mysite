from django.db import models
from django.utils import timezone
from django.urls import reverse
#timezone
#reverse
# Create your models here.

#post-> author(foregin key), title, publication, creation
#auther will be directed to a super user
#model has a text field
#cretae time default time will be timexone.now
# publish func, approve funtion return comment.filter approved comment = true
class Post(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    creation_date = models.TimeField(default=timezone.now())
    published_date = models.DateField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    #def approve_comments(self):
    #    return self.comments.filter(approved_comments=True) this part needed to be fixed

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.post', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateField(default=timezone.now())
    approved_comments = models.BooleanField(default=False)

    def approve(self):
        self.approve_comments = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")
    

    def __str__(self):
        return self.text

