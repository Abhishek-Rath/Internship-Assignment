### Problem Statement
Suppose we have two websites with different database schema and we have to keep data of the user table the same in both databases, suppose we add one user in the first website then it should automatically be added in another website and vice versa. How can we do that using Django?

### Answer:
- We can use the concept of triggers to update user information in both databases. As we know, triggers are stored programs which get automatically executed or fired when some events occur. An event can be anything like - Delete, insert, update, create, alter, etc

``` 
Django Code:
from django.db.models.signals import pre_save
from dajngo.db import models
from django.contrib.auth.models import AbstractUser

class User1(AbstractUser)
    pass

class User2(models.Model)
    username = models.charField(max_length = 30, blank = False)
    password = models.CharField(max_length = 16, blank = False)

def update_user_info(sender, instance, **kwargs):
    user2 = User2(username = instance.username, password = instance.password)
    if user2.is_valid():
        user2.save()

prev_save.connect(update_user_info, sneder = user1)

```

- A pre-save signal is used in situations where logic has to be executed before data is saved to a database