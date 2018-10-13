from django.db import models

class Chat(models.Model):

   messagedata = models.CharField(max_length = 150, null= True)
   chatid= models.CharField(max_length = 150, null= True)
   user_msg = models.PositiveIntegerField(null= True)
   roomname= models.CharField(max_length = 150, null= True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   class Meta:
      db_table = "Chat"
      
   def __str__(self,name):
      return self.name


class Chat_ID(models.Model):

   chatid= models.CharField(max_length = 150, null= True)
   roomname= models.CharField(max_length = 150, null= True)
   channel_name= models.CharField(max_length = 150, null= True)
   username= models.CharField(max_length = 150, null= True)
   is_active = models.BooleanField(default= True)


   class Meta:
      db_table = "Chat_ID"
      
   def __str__(self,name):
      return self.name