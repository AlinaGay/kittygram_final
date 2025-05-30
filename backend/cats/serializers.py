"""
Serializers for the cats application.

This module defines custom and model serializers
for Cat, Achievement, and related models.
It includes custom fields for color representation
and image handling, as well as
custom create and update logic for nested relationships.
"""

import base64
import datetime as dt

import webcolors
from django.core.files.base import ContentFile
from rest_framework import serializers

from .models import Achievement, AchievementCat, Cat


class Hex2NameColor(serializers.Field):
    """
    Custom serializer field to convert a hex color code to its name.

    Converts hex color codes to color names using the webcolors library.
    Raises a validation error if the color name does not exist.
    """

    def to_representation(self, value):
        """Return the color value as is for representation."""
        return value

    def to_internal_value(self, data):
        """
        Convert a hex color code to a color name.

        Args:
            data (str): Hex color code.

        Returns:
            str: Color name.

        Raises:
            serializers.ValidationError: If the color name does not exist.
        """
        try:
            data = webcolors.hex_to_name(data)
        except ValueError:
            raise serializers.ValidationError('Для этого цвета нет имени')
        return data


class AchievementSerializer(serializers.ModelSerializer):
    """
    Serializer for the Achievement model.

    Serializes the id and name (as achievement_name) fields.
    """

    achievement_name = serializers.CharField(source='name')

    class Meta:
        """Meta options for AchievementSerializer."""

        model = Achievement
        fields = ('id', 'achievement_name')


class Base64ImageField(serializers.ImageField):
    """Custom serializer field to handle image uploads in base64 format."""

    def to_internal_value(self, data):
        """
        Convert a base64-encoded image to a ContentFile.

        Args:
            data (str): Base64-encoded image string.

        Returns:
            ContentFile: Decoded image file.
        """
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class CatSerializer(serializers.ModelSerializer):
    """Serializer for the Cat model."""

    achievements = AchievementSerializer(required=False, many=True)
    color = Hex2NameColor()
    age = serializers.SerializerMethodField()
    image = Base64ImageField(required=False, allow_null=True)
    image_url = serializers.SerializerMethodField(
        'get_image_url',
        read_only=True,
    )

    class Meta:
        """
        Meta options for CatSerializer.

        Specifies the model, fields to include, and read-only fields.
        """

        model = Cat
        fields = (
            'id', 'name', 'color', 'birth_year', 'achievements',
            'owner', 'age', 'image', 'image_url'
        )
        read_only_fields = ('owner',)

    def get_image_url(self, obj):
        """
        Return the URL of the cat's image if it exists.

        Args:
            obj (Cat): Cat instance.

        Returns:
            str or None: Image URL or None if no image.
        """
        if obj.image:
            return obj.image.url
        return None

    def get_age(self, obj):
        """
        Calculate the age of the cat based on the current year and birth year.

        Args:
            obj (Cat): Cat instance.

        Returns:
            int: Age of the cat.
        """
        return dt.datetime.now().year - obj.birth_year

    def create(self, validated_data):
        """
        Create a new Cat instance, handling nested achievements if provided.

        Args:
            validated_data (dict): Validated data for the Cat.

        Returns:
            Cat: Created Cat instance.
        """
        if 'achievements' not in self.initial_data:
            cat = Cat.objects.create(**validated_data)
            return cat
        achievements = validated_data.pop('achievements')
        cat = Cat.objects.create(**validated_data)
        for achievement in achievements:
            current_achievement, status = Achievement.objects.get_or_create(
                **achievement
            )
            AchievementCat.objects.create(
                achievement=current_achievement, cat=cat
            )
        return cat

    def update(self, instance, validated_data):
        """Update an existing Cat instance."""
        instance.name = validated_data.get('name', instance.name)
        instance.color = validated_data.get('color', instance.color)
        instance.birth_year = validated_data.get(
            'birth_year', instance.birth_year
        )
        instance.image = validated_data.get('image', instance.image)

        if 'achievements' not in validated_data:
            instance.save()
            return instance

        achievements_data = validated_data.pop('achievements')
        lst = []
        for achievement in achievements_data:
            current_achievement, status = Achievement.objects.get_or_create(
                **achievement
            )
            lst.append(current_achievement)
        instance.achievements.set(lst)

        instance.save()
        return instance
