from django.db import models


from . import querysets


class BaseManager(models.Manager):
    pass


NoteManager = BaseManager.from_queryset(querysets.NoteQuerySet)
