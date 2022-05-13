from django.db import models


class Order(models.Model):
    receiver_name = models.CharField(max_length=120, blank=True)
    receiver_phone = models.CharField(max_length=20, blank=True)
    sender_name = models.CharField(max_length=120, blank=True)
    sender_phone = models.CharField(max_length=20, blank=True)
    track_id = models.CharField(max_length=20, default="RV123456")

    def __str__(self):
        return f"ID: {self.pk} - {self.track_id}"


class OrderAnswer(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='user')

    def __str__(self):
        return f"ID: {self.pk} - {self.order.track_id}"


class Question(models.Model):
    question = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    YES = 'Yes'
    NO = 'No'

    CHOICES = ((YES, "Yes"), (NO, "No"),)
    order = models.ForeignKey(OrderAnswer, on_delete=models.CASCADE, null=True, blank=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, blank=True)
    choice = models.CharField(max_length=255, choices=CHOICES, default=NO)
    additional = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"ID: {self.pk} - {self.order}"

    class Meta:
        verbose_name = "User answer"
        verbose_name_plural = "User answers"

