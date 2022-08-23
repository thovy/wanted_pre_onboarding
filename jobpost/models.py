from django.db import models

# 회사
class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    nation = models.CharField(max_length=20)
    region = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# 채용 공고
class JobPost(models.Model):
    company = models.ForeignKey('Company',on_delete=models.CASCADE)
    position = models.CharField(max_length=50)
    reward = models.IntegerField()
    skill = models.CharField(max_length=100)
    article = models.TextField()

    def __str__(self):
        return self.name