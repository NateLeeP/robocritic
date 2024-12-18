from django.db import models


class Game(models.Model):
    # Primary keys automatic - adding for readability
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    art_url = models.CharField(max_length=200)
    youtube_gameplay_url = models.CharField(max_length=200, blank=True, null=True)
    critic_score_average = models.IntegerField(blank=True, null=True)
    normalized_title = models.CharField(max_length=100, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = "game"
        ordering = ["-release_date"]


class Platform(models.Model):
    # Primary keys automatic - adding for readability
    id = models.BigAutoField(primary_key=True)
    platform_name = models.CharField(max_length=50, unique=True)
    platform_abbreviation = models.CharField(max_length=50)

    def __str__(self):
        return self.platform_name

    class Meta:
        managed = False
        db_table = "platform"


class PlatformGame(models.Model):
    # Primary keys automatic - adding for readability
    id = models.BigAutoField(primary_key=True)
    platform = models.ForeignKey(Platform, on_delete=models.DO_NOTHING)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = "platform_game"


class Publisher(models.Model):
    # Primary keys automatic - adding for readability
    id = models.BigAutoField(primary_key=True)
    publisher_name = models.CharField(max_length=50, unique=True)
    publisher_domain_name = models.CharField(max_length=100)
    rating_scale = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.publisher_name

    class Meta:
        managed = False
        db_table = "publisher"


class Reviewer(models.Model):
    # Primary keys automatic - adding for readability
    id = models.BigAutoField(primary_key=True)
    reviewer_full_name = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    reviewer_bio_url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.reviewer_full_name

    class Meta:
        managed = False
        db_table = "reviewer"


class Review(models.Model):
    # Primary keys automatic - adding for readability
    id = models.BigAutoField(primary_key=True)
    review_url = models.CharField(max_length=200)
    robo_score = models.DecimalField(max_digits=3, decimal_places=1)
    critic_score = models.DecimalField(max_digits=3, decimal_places=1)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.DO_NOTHING)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.game.title + " - " + self.publisher.publisher_name

    class Meta:
        managed = False
        db_table = "review"
        ordering = ["-created_at"]


class ReviewPro(models.Model):
    # Primary keys automatic - adding for readability
    id = models.BigAutoField(primary_key=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    pros = models.JSONField(default=list, null=True)

    class Meta:
        managed = False
        db_table = "review_pro"


class ReviewCon(models.Model):
    # Primary keys automatic - adding for readability
    id = models.BigAutoField(primary_key=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    cons = models.JSONField(default=list, null=True)

    class Meta:
        managed = False
        db_table = "review_con"
