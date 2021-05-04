from django.db import models

# Create your models here.
 

class PersonalDetails(models.Model):
    image = models.FileField(upload_to='images/')
    f_name = models.CharField(max_length=50, verbose_name="First Name", blank=True, null=True)
    m_name = models.CharField(max_length=50, verbose_name="Middle Name", blank=True, null=True)
    l_name = models.CharField(max_length=50, verbose_name="Last Name", blank=True, null=True)
    age = models.IntegerField()

    def __str__(self):
        return self.l_name