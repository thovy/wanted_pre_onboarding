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

    # 채용공고 작성, 수정 시간
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} {self.article}'

# 사용자
class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# 지원
class Resume(models.Model):
    User = models.ForeignKey("User", on_delete=models.CASCADE)
    JobPost = models.ForeignKey("JobPost", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

