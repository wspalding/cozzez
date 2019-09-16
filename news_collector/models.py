from django.db import models
from datetime import datetime

class Protest(models.Model):
    """docstring for Protest"""
    title = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=80)
    active = models.BooleanField(default=False)
    num_protesters = models.PositiveIntegerField()
    # tags = models.
    site = models.URLField(null=True)
    comments = models.URLField(null=True)
        




# Create your models here.
# class Test(models.Model):
#     name = models.CharField(max_length=20)
#     date = models.DateTimeField(default=datetime.now)

# class Topic(models.Model):
#     # name = models.CharField(max_length=50)
#     label1 = models.ForeignKey("Label", on_delete=models.CASCADE, null=True, related_name="top_label")
#     label2 = models.ForeignKey("Label", on_delete=models.CASCADE, null=True, related_name="middle_label")
#     label3 = models.ForeignKey("Label", on_delete=models.CASCADE, null=True, related_name="bottom_label")
#     date = models.DateTimeField()
#     articles = models.ManyToManyField("Article", related_name="related_articles")
# #    personalities = models.ManyToManyField('Personality')

#     class Meta:
#         ordering = ['-date']
    
# #    @property
# #    def to_str(self):
# #        return '%s, %s, %s' % (self.label1, self.label2, self.label3)
# #
# #    def __str__(self):
# #        return str(self.label1)+", "+str(self.label2)+", "+str(self.label3)

#     @property
#     def get_articles(self):
#         return self.articles.all()

# class Article(models.Model):
# #    POLITICAL_BIAS = (
# #                      ('L', 'Left'),
# #                      ('R', 'Right'),
# #                      ('M', 'Middle'),
# #                      ('U', 'Unknown')
# #                      )
#     affiliation = models.CharField(max_length=20)
#     date = models.DateTimeField()
#     title = models.CharField(max_length=100)
#     url = models.URLField()
#     source_url = models.URLField(null=True)
# #    media_url = models.URLField(null=True)
# #    bias = models.CharField(max_length=1, choices=POLITICAL_BIAS)
#     topic = models.ManyToManyField(Topic)
# #    personalities = models.ManyToManyField('Personality')
# #    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

#     #class Meta:
#     #    ordering = ['topic']

#     def __str__(self):
#       return self.title

# class Label(models.Model):
#     word = models.CharField(max_length=50)
#     score = models.IntegerField()
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    
#     class Meta:
#         ordering = ['-score']
    
#     def __str__(self):
#         return self.word

#class Comment(models.Model):
#    user = models.CharField(max_length=50)
#    quote = models.CharField(max_length=1000)
#    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#    # reply = models.ForeignKey(Comment, on_delete=models.CASCADE, default=NULL)
#
#    def __str__(self):
#        return self.quote

#class Personality(models.Model):
#    name = models.CharField(max_length=100)
#    #last_name = models.CharField(max_length=50)
#    position = models.CharField(max_length=50, null=True)
#    topics = models.ManyToManyField(Topic)
#    articles = models.ManyToManyField(Article)
#
#    def _str__(self):
#        return str(name)

#class Author(models.Model):
#    name = models.CharField(max_length=100)
#    #last_name = models.CharField(max_length=50)
#    affiliation = models.CharField(max_length=20)
#
#    def _str__(self):
#        return str(name)
#
#


