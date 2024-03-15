from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone  


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)  
    

    def __str__(self):
        return self.client_name

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    client = models.ForeignKey(Client,related_name='projects', on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects_assigned', blank=True)

    def __str__(self):
        return self.project_name


######## explanation
    
    
# Things to consider :

# 1. The system has many users.   =======>>>>>> for this condition i have used in build usermodel of django

# 2. The system has many clients. ===> for this condition i have made seperate model for client field

# 3. A client can have many projects ===> for this condition In project model i have connected to client model with ForeignKey

# 4. A single project can be assigned to many users.  =====> for this condition I have use the many to many relation 


    
####Thank you 
