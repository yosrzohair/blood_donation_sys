from django.db import models
from django.contrib.auth.hashers import make_password

class Citizen(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    blood_type = models.CharField(max_length=5)
    city = models.CharField(max_length=100, choices=[('Shmesani', 'Shmesani'), ('Khalda', 'Khalda'), ('Makka Street', 'Makka Street')])
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=255)


    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):  # Prevent double hashing
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Institute(models.Model):
    name = models.CharField(max_length=255, unique=True)
    institute_type = models.CharField(max_length=50, choices=[('Hospital', 'Hospital'), ('Blood Bank', 'Blood Bank'), ('Clinic', 'Clinic')])
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100, choices=[('Shmesani', 'Shmesani'), ('Khalda', 'Khalda'), ('Makka Street', 'Makka Street')])
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=255)



    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)



