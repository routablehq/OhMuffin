# 2020-04-06 - Needs review

# Python imports
import uuid
from django.db import models


# --------------------
# Helpers
# --------------------


# --------------------
# Models
# --------------------


class BaseModel(models.Model):
    """
    Base Model
    - Sets the ID field to UUID and the created/modified fields
    """

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    id = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Interest(BaseModel):
    """User Profile for storing user/interests"""

    # Private attributes

    # Manager

    # Fields

    name = models.CharField(max_length=200)

    # Nested classes

    class Meta:
        verbose_name = "Interest"
        verbose_name_plural = "Interests"

    # Special method overrides

    def __str__(self):
        return self.name

    # Private methods

    # Class methods

    # Properties

    # Overrides

    # Methods


class Profile(BaseModel):
    """User Profile for storing user/interests"""

    # Private attributes

    # Manager

    # Fields

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    slack_id = models.CharField(max_length=200)
    interests = models.ManyToManyField(Interest, related_name="interests")

    # Nested classes

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    # Special method overrides

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # Private methods

    # Class methods

    # Properties

    # Overrides

    # Methods

    def simple_dict(self):
        return {
            "name": str(self),
            "id": self.id,
            "slack_id": self.slack_id
        }


class Match(BaseModel):
    profiles = models.ManyToManyField(Profile, related_name="matches")
    interests = models.ManyToManyField(Interest, related_name="matches")
