from django.db import models

# Create your models here.
class person(models.Model):
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHERS', 'Others'),
    ]

    QUALIFICATION_CHOICES = [
        ('BSC', 'BSc'),
        ('MSC', 'MSc'),
        ('BCA', 'BCA'),
        ('MCA', 'MCA'),
        ('BTECH', 'BTech'),
        ('MTECH', 'MTech'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('MARRIED', 'Married'),
        ('SINGLE', 'Single'),
        ('DIVORCED', 'Divorced'),
        ('WIDOWED', 'Widowed'),
    ]

    INTEREST_CHOICES = [
        ('INTERESTED', 'Interested'),
        ('NOTINTERESTED', 'Not Interested'),
        ('UNDECIDED', 'Undecided'),
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    phonenumber = models.CharField(max_length=15)
    qualifications = models.CharField(max_length=10, choices=QUALIFICATION_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dateofbirth = models.DateField()
    maritalstatus = models.CharField(max_length=15, choices=MARITAL_STATUS_CHOICES)
    interests = models.CharField(max_length=15, choices=INTEREST_CHOICES)


    def __str__(self) -> str:
        return f'{self.firstname}'