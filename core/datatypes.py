from django.db import models
from django.utils.translation import gettext_lazy as gl


# A Nullable CharField
class NullableChar(models.CharField):
    description = "A nullable CharField"

    def __init__(self, *args, **kwargs):
        kwargs['default'] = None
        kwargs['blank'] = True
        kwargs['null'] = True
        super().__init__(*args, **kwargs)


# A Nullable DecimalField
class NullableDecimal(models.DecimalField):
    description = "A nullable DecimalField"

    def __init__(self, *args, **kwargs):
        kwargs['default'] = None
        kwargs['blank'] = True
        kwargs['null'] = True
        super().__init__(*args, **kwargs)


# A Nullable FloatField
class NullableFloatField(models.FloatField):
    description = "A nullable float field"

    def __init__(self, *args, **kwargs):
        kwargs['default'] = None
        kwargs['blank'] = True
        kwargs['null'] = True
        super().__init__(*args, **kwargs)


# A Nullable ForeignKey
class NullableForeignKey(models.ForeignKey):
    description = "A nullable ForeignKey"

    def __init__(self, *args, **kwargs):
        kwargs['default'] = None
        kwargs['blank'] = True
        kwargs['null'] = True
        super().__init__(*args, **kwargs)


# A Nullable PositiveIntegerField
class NullablePositiveInteger(models.PositiveIntegerField):
    description = "A nullable PositiveIntegerField"

    def __init__(self, *args, **kwargs):
        kwargs['default'] = None
        kwargs['blank'] = True
        kwargs['null'] = True
        super().__init__(*args, **kwargs)


# A Nullable URLField
class NullableURL(models.URLField):
    description = "A nullable URLField"

    def __init__(self, *args, **kwargs):
        kwargs['default'] = None
        kwargs['blank'] = True
        kwargs['null'] = True
        super().__init__(*args, **kwargs)
