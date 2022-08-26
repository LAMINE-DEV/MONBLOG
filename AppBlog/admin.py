from django.contrib import admin

# Register your models here.
from AppBlog.models import Post,Comment,Cours,Email


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject','message','document')
    search_fields = ('subject','email','message')


@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('matier', 'pdf_cours','name')
    search_fields = ('matier','pdf_cours','name')

@admin.register(Post)
class VenueAdmin(admin.ModelAdmin):
 	list_display = ('categorie', 'body', 'image','document_pdf','document_video')
 	search_fields = ('categorie','body')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'post')
    list_filter = ['created_on']
    search_fields = ('name', 'email', 'content')
    actions = ['approve_comments']


    def approve_comments(self, request, queryset):
        queryset.update(active=True)




admin.site.site_header = 'My Blog : SENEGAL-CODE 2022'