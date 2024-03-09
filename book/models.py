from django.db import models
from django.contrib.auth.models import User
# Create your models here.

PRIORITY = (
            (0,'0'),
            (1,'1'),
            (2,'2'),
            (3,'3'),
            (4,'4'),
            (5,'5'),
            (6,'6'),
            (7,'7'), 
            (8,'8'),
)
class TaskModel(models.Model): 
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='my_task')
    priority = models.IntegerField(choices=PRIORITY,default = 1)
    taskTitle  = models.CharField(max_length=50) 
    taskDescription = models.CharField(max_length=250) 
    is_completed = models.BooleanField() 
    due_date =models.DateField(null=True,blank=False)
    
    def __str__(self):
        return str(self.taskTitle)
    
# class FilterForm(models.Model): 
#     pass