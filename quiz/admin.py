from django.contrib import admin
from .models import Order, OrderAnswer, Question, Answer


class AnswerAdmin(admin.TabularInline):
    model = Answer
    extra = 3


class OrderAnswerAdmin(admin.ModelAdmin):
    list_display = ('order', )
    inlines = [AnswerAdmin, ]


class UserAnswerAdmin(admin.ModelAdmin):

    list_display = (
        'order',
        'question',
        'choice',
        'additional',
    )
    list_filter = ('order', 'choice', 'question')


admin.site.register(Order)
admin.site.register(Question)
admin.site.register(OrderAnswer, OrderAnswerAdmin)
admin.site.register(Answer, UserAnswerAdmin)
