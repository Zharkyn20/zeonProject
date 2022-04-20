from django.db import models
from .validators import validate_file_extension


class ContactChoice(models.TextChoices):
    WHATSAPP = u'WA', 'WhatsApp'
    PHONE = u'PH', 'Phone'
    EMAIL = u'EM', 'Email'
    INSTAGRAM = u'INST', 'Instagram'
    TELEGRAM = u'TG', 'Telegram'


class Footer(models.Model):
    icon = models.FileField(".svg, .png formats required",
                            upload_to='media/our_advantages/%Y/%m/%d',
                            validators=[validate_file_extension])
    text = models.TextField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return 'Footer'

    class Meta:
        verbose_name_plural = 'Footer'


class Contact(models.Model):
    footer = models.ForeignKey('Footer', on_delete=models.CASCADE, related_name='contacts')
    contact = models.CharField(max_length=4, choices=ContactChoice.choices)
    link = models.CharField(max_length=150, null=True)

    def save(self):
        if self.contact == ContactChoice.WHATSAPP:
            self.link = f"https://wa.me/{self.link}"
            super(Contact, self).save()
        else:
            self.link = self.link
            super(Contact, self).save()

    def __str__(self):
        return self.contact
