from django.db import models


from simplenote.core import models as core_models
from . import managers


class Note(core_models.TimeStampedModel):
    title = models.CharField(max_length=255)
    body = models.TextField()
    objects = managers.NoteManager()
