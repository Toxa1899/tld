from django.db import models
import uuid
# Create your models here.


class Chat(models.Model):
    chat_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )
    companion_id = models.IntegerField(verbose_name='companion id')
    my_id = models.IntegerField(verbose_name='my id', blank=True , null=False)




class Message(models.Model):
    chat = models.ForeignKey(Chat,on_delete=models.CASCADE)
    message = models.TextField(verbose_name='message')
    user_id = models.IntegerField(verbose_name='id user chat')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)