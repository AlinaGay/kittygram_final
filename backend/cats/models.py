"""
Models for the cats application.

Defines models for Cat, Achievement, and the intermediate AchievementCat model
to represent achievements earned by cats.
"""

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Achievement(models.Model):
    """
    Model representing an achievement that can be earned by a cat.

    Fields:
        name (CharField): The name of the achievement.
    """

    name = models.CharField(max_length=64)

    class Meta:
        """Meta options for the Achievement model."""

        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

    def __str__(self):
        """Return a string representation of the achievement."""
        return self.name


class Cat(models.Model):
    """
    Model representing a cat.

    Fields:
        name (CharField): The name of the cat.
        color (CharField): The color of the cat.
        birth_year (IntegerField): The year the cat was born.
        owner (ForeignKey): The user who owns the cat.
        achievements (ManyToManyField): Achievements earned by the cat.
        image (ImageField): An optional image of the cat.
    """

    name = models.CharField(max_length=16)
    color = models.CharField(max_length=16)
    birth_year = models.IntegerField()
    owner = models.ForeignKey(
        User, related_name='cats',
        on_delete=models.CASCADE
    )
    achievements = models.ManyToManyField(
        Achievement,
        through='AchievementCat'
    )
    image = models.ImageField(
        upload_to='cats/images/',
        null=True,
        default=None
    )

    class Meta:
        """Meta options for the Cat model."""

        verbose_name = 'Cat'
        verbose_name_plural = 'Cats'

    def __str__(self):
        """Return a string representation of the cat."""
        return self.name


class AchievementCat(models.Model):
    """
    Model representing the relationship between Cat and Achievement.

    Fields:
        achievement (ForeignKey): The related achievement.
        cat (ForeignKey): The related cat.
    """

    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    class Meta:
        """Meta options for the AchievementCat model."""

        verbose_name = 'Cat Achievement'
        verbose_name_plural = 'Cat Achievements'

    def __str__(self):
        """Return a string representation of the cat's achievement."""
        return f'{self.achievement} {self.cat}'
