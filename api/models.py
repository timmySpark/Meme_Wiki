from django.db import models
import uuid

# Create your models here.


class Joke(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=100,default='none',null=False)
    setup = models.TextField()
    punchline = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = ("Joke")
        verbose_name_plural = ("Jokes")

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse("Joke_detail", kwargs={"pk": self.pk})



# class Meme(models.Model):
    
    

#     class Meta:
#         verbose_name = ("Meme")
#         verbose_name_plural = ("Memes")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("Meme_detail", kwargs={"pk": self.pk})
