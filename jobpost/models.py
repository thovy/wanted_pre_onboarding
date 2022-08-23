from django.db import models

# 회사
class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# 채용 공고
class JobPost(models.Model):
    company_name = models.CharField(max_length=100)
    company_nation = models.CharField(max_length=20)
    company_region = models.CharField(max_length=20)
    position = models.CharField(max_length=50)
    reward = models.IntegerField()
    skill = models.CharField(max_length=100)
    article = models.TextField()

    def __str__(self):
        return f'{self.pk}, {self.company_name} {self.position} {self.reward} {self.skill}'