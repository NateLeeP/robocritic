from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    art_url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Platform(models.Model):
    platform_name = models.CharField(max_length=50, unique=True)
    platform_abbreviation = models.CharField(max_length=50)

    def __str__(self):
        return self.platform_name

class PlatformGame(models.Model):
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=50, unique=True)
    publisher_domain_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.publisher_name

class Reviewer(models.Model):
    reviewer_full_name = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    reviewer_bio_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.reviewer_full_name

class Review(models.Model):
    review_url = models.CharField(max_length=200)
    robo_score = models.DecimalField(max_digits=3, decimal_places=1)
    critic_score = models.DecimalField(max_digits=3, decimal_places=1)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.DO_NOTHING)
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

class ReviewPro(models.Model):
    review = models.ForeignKey(Review, on_delete=models.DO_NOTHING)
    pros = models.TextField()

class ReviewCon(models.Model):
    review = models.ForeignKey(Review, on_delete=models.DO_NOTHING)
    cons = models.TextField()