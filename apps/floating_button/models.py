from django.db import models


class CallbackChoice(models.TextChoices):
    CALLBACK = u'C', 'Callback'


class CallStatusChoice(models.TextChoices):
    YES = u'Y', 'Yes'
    NO = u'N', 'No'


class FloatingButton(models.Model):
    whats_app = models.CharField(max_length=150)
    telegram = models.CharField(max_length=150)

    def __str__(self):
        return 'Floating Button'

    def save(self):
        self.whats_app = f"https://wa.me/{self.whats_app}"
        super(FloatingButton, self).save()


class Callback(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    handle_date = models.DateTimeField(auto_now_add=True)
    call_date = models.DateTimeField(auto_now=True)
    handle_type = models.CharField(max_length=1, choices=CallbackChoice.choices,
                                   default=CallbackChoice.CALLBACK)
    is_called = models.CharField(max_length=1, choices=CallStatusChoice.choices,
                                 default=CallStatusChoice.NO)

    def __str__(self):
        return self.name
