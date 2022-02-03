from django.db import models


# Field Choices
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

MEDIATYPE = (
    (0,"Music"),
    (1,"Videos"),
    (2,"Music_Videos")
)

class BrandonMedia(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    # mediafile = 
    pub_date = models.DateTimeField(auto_now_add=True)
    mediatype = models.IntegerField(choices=MEDIATYPE, default=0)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.title}, {self.mediatype}'