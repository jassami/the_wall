from django.db import models



class Message(models.Model):
    message= models.TextField()
    user= models.ForeignKey('login_app.User', related_name="messages", on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


class Comment(models.Model):
    comment= models.TextField()
    message= models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    user= models.ForeignKey('login_app.User', related_name="comments", on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)


