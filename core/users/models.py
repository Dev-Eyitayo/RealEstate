from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")
        
        user = self.model(
            email=self.normalize_email(email).lower(),
            first_name=first_name,
            last_name=last_name,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_realtor(self, email, first_name, last_name, password=None):
        user = self.create_user(email, first_name, last_name, password)
        user.is_realtor = True
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, first_name, last_name, password=None):
        user = self.create_user(email, first_name, last_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

        

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_realtor = models.BooleanField(default=False)
    objects = CustomUserManager()
     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return self.email