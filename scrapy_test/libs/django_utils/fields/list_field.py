#http://stackoverflow.com/questions/5216162/how-to-create-list-field-in-django
#https://github.com/django-extensions/django-extensions/blob/9008bac65cdb57dfce0cb78a69eb1639285363a5/django_extensions/db/fields/json.py#L91
from django.db import models
import ast


class ListField(models.TextField):
  __metaclass__ = models.SubfieldBase
  description = "Stores a python list"

  def __init__(self, *args, **kwargs):
    super(ListField, self).__init__(*args, **kwargs)

  def to_python(self, value):
    if not value:
      value = []

    if isinstance(value, list):
      return value

    return ast.literal_eval(value)

  def get_prep_value(self, value):
    if value is None:
      return value

    return unicode(value)

  def value_to_string(self, obj):
    value = self._get_val_from_obj(obj)
    return self.get_db_prep_value(value)

  def south_field_triple(self):
    "Returns a suitable description of this field for South."
    # We'll just introspect the _actual_ field.
    from south.modelsinspector import introspector

    field_class = "django.db.models.fields.TextField"
    args, kwargs = introspector(self)
    # That's our definition!
    return (field_class, args, kwargs)

