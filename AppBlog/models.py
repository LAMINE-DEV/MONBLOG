from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Email(models.Model):
    email=models.EmailField(max_length=100,null=False,blank=False)
    subject=models.CharField(max_length=100,null=False,blank=False)
    datatime=models.DateTimeField(auto_now_add=True)
    document=models.FileField(null=True,blank=True,upload_to='Email_documents/')
    message=models.TextField(max_length=10000,null=False,blank=False)
    class Meta:
        db_table='Email'
        ordering=('-datatime',)


    def __str__(self):
        return self.subject+" "+self.message

class Cours(models.Model):
    choix=(
         ('', ''),
        ('python', 'python'),
        ('javascript', 'javascript'),
        ('django', 'django'),
        ('css3', 'css3'),
        ('html', 'html'),
        ('java', 'java'),
        
    )
    matier=models.CharField(max_length=300, choices=choix,blank=True,null=True,help_text='selection la matier svp')
    pdf_cours = models.FileField(help_text='selectionner le cours concerner',upload_to='cours/',null=False,blank=False)
    datetime=models.DateTimeField(auto_now=True)
    name=models.CharField(help_text='Non du document cest tres important pour les eleves',max_length=400,default='cours python')

    class Meta:
        db_table="cours"
        ordering=('-datetime',)
    def __str__(self):
        return self.name+" "+self.matier+" "+str(self.datetime)



class Post(models.Model):
    choix=(
		 ('', ''),
        ('python', 'python'),
        ('javascript', 'javascript'),
        ('django', 'django'),
        ('css3', 'css3'),
        ('html', 'html'),
        ('java', 'java'),
        ('annonce', 'annonce'),
        ('autres', 'autres')
    )
    categorie=models.CharField(max_length=300, choices=choix,blank=True,null=True)
    body=QuillField()
    image = models.ImageField(help_text='image',upload_to='images',null=True,blank=True)
    document_pdf = models.FileField(help_text='pdf',upload_to='document_pdf/',null=True,blank=True)
    datetime=models.DateTimeField(auto_now=True)
    document_video=models.FileField(help_text='video',upload_to='document_video/',null=True,blank=True)
	


    class Meta:
        db_table='Post'
        ordering = ('-datetime',)
    def __str__(self):
        return self.categorie+" "+str(self.datetime)



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    photo=models.ImageField(upload_to='commentprofile',null=True,blank=True)
    content=QuillField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.name)


