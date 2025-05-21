from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.
    

class comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()
    uploaded = models.DateTimeField(auto_now_add=True)

# Create your models here.
class CustomUser(AbstractUser):
    is_subscribed = models.BooleanField(default=False)
    staff_status=models.BooleanField(default=False)

class type12(models.Model):
    num=models.CharField(max_length=20,unique=True)

    def __str__(self):
        return str(self.num)
    
class major12(models.Model):
    sub=models.CharField(max_length=20)
    type = models.ForeignKey(type12,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.sub)


class classes(models.Model):
    num=models.CharField(max_length=20,unique=True)
    type = models.ForeignKey(type12,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.num)
    

class subject(models.Model):
    sub_name=models.CharField(max_length=20)
    type = models.ForeignKey(type12,on_delete=models.CASCADE)
    class1 = models.ForeignKey(classes,on_delete=models.CASCADE,default=1)
    sub_full=models.CharField(max_length=20,default=0)
    major=models.ForeignKey(major12,on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_name

class publication(models.Model):
    pub_name=models.CharField(max_length=20,unique=True)
    type = models.ForeignKey(type12,on_delete=models.CASCADE)
    major=models.ForeignKey(major12,on_delete=models.CASCADE)

    def __str__(self):
        return self.pub_name
def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')
    
class unit1(models.Model):
    name=models.CharField(max_length=20,unique=True)
    # num=models.CharField(max_length=20,default=0)
    # type = models.ForeignKey(type12,on_delete=models.CASCADE)
    # major=models.ForeignKey(major12,on_delete=models.CASCADE)
    # sub=models.ForeignKey(subject,on_delete=models.CASCADE,default='2')
    # class1 = models.ForeignKey(classes,on_delete=models.CASCADE,default=1)


    def __str__(self):
        return self.name

    
class unit(models.Model):
    class1 = models.ForeignKey(classes,on_delete=models.CASCADE)
    sub=models.ForeignKey(subject,on_delete=models.CASCADE)
    pub=models.ForeignKey(publication,on_delete=models.CASCADE)
    # type = models.ForeignKey(type12,on_delete=models.CASCADE)
    major=models.ForeignKey(major12,on_delete=models.CASCADE)
    unit_num=models.ForeignKey(unit1,on_delete=models.CASCADE)
    unit_pdf=models.FileField(upload_to='epathsala/', validators=[validate_pdf])

class exam1(models.Model):
    term=models.CharField(max_length=20,unique=True)
    # num=models.CharField(max_length=20,default=0)
    # type = models.ForeignKey(type12,on_delete=models.CASCADE)
    # major=models.ForeignKey(major12,on_delete=models.CASCADE)
    def __str__(self):
        return self.term

class exam(models.Model):
    ter=models.ForeignKey(exam1,on_delete=models.CASCADE)
    class1 = models.ForeignKey(classes,on_delete=models.CASCADE)
    sub=models.ForeignKey(subject,on_delete=models.CASCADE)
    major=models.ForeignKey(major12,on_delete=models.CASCADE)
    pdf=models.FileField(upload_to='epathsala/', validators=[validate_pdf])
    scl=models.CharField(max_length=20)


