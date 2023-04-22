from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    @property
    def is_visit_long(self, minutes=60):
        leaved_at = localtime(self.leaved_at) if self.leaved_at else localtime()
        delta = leaved_at - localtime(self.entered_at)
        return delta.seconds > minutes * 60

    @property
    def get_duration(self):
        leaved_at = localtime(self.leaved_at) if self.leaved_at else localtime()
        delta = leaved_at - localtime(self.entered_at)
        return delta.seconds

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )
