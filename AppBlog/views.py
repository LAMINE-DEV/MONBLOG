
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib import messages
from AppBlog.models import Post,Cours
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import CommentForm,CommentForm1,PostForm
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from accounts.models import Profile
from .models import Comment
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView,DeleteView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


def change_password(request):
	data=Profile.objects.get(user=request.user)
	information=User.objects.get(username=request.user)
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			return redirect('userinformation-view')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm()
	return render(request, 'appblog/userinformation.html',{'form': form,'data':data,'information':information})




class Adminpostpage_view(UpdateView):
	model=Post
	fields='__all__'
	template_name='appblog/adminupdatepost.html'
	success_url='/'



class Deleteview(DeleteView):
	model=Post
	template_name='appblog/areyousure.html'
	success_url='/'
	



def Delete(request,pk):
	return redirect('admindeletepost-view',pk=pk)


@login_required(login_url='login-view')
def UploadImage_view(request):
	if request.method=='POST' and request.FILES['photo']:
		photo=request.FILES['photo']
		Profile_pic_update=Profile.objects.get(user=request.user)
		Profile_pic_update.photo=photo
		Profile_pic_update.save()
		messages.success(request,'votre photo de profile est bien mise a jours merci !!!')
		return redirect('userinformation-view')

@login_required(login_url='login-view')
def Userinformation_View(request):
	data=Profile.objects.get(user=request.user)
	information=User.objects.get(username=request.user)

	return render(request,'appblog/userinformation.html',{'data':data,'information':information})

@login_required(login_url='login-view')
def updateProfile(request):

	if request.method=='POST':

		username=request.POST['username']
		last_name=request.POST['last_name']
		first_name=request.POST['first_name']
		telephone=request.POST['telephone']
		email=request.POST['email']

		# creation dun nouvelle instance de user_cible
		user_cible=User.objects.get(username=request.user)


		user_cible.username=username
		user_cible.email=email
		user_cible.last_name=last_name
		user_cible.first_name=first_name
		user_cible.save()


       # creation dun nouvelle instance de user_cible

		profile_user_cible=Profile.objects.get(user=request.user)
		profile_user_cible.telephone=telephone
		profile_user_cible.save()
		messages.success(request,'votre profile est bien mise a jours merci !!!')



		return redirect('userinformation-view')

@login_required(login_url='login-view')
		
def Search_view(request):
	categorie1=Post.objects.filter(categorie="python")
	categorie2=Post.objects.filter(categorie="java")
	categorie3=Post.objects.filter(categorie="django")
	categorie4=Post.objects.filter(categorie="javascript")
	categorie5=Post.objects.filter(categorie="css3")
	categorie6=Post.objects.filter(categorie="c")
	categorie7=Post.objects.filter(categorie="html")
	categorie8=Post.objects.filter(categorie="bootstrap")
	categorie9=Post.objects.filter(categorie="autres")
	post=Post.objects.all()
	if request.method=='GET':
		search_result=request.GET.get('searchdata')
		if search_result:
			resultas=Post.objects.filter(categorie=search_result)
			
			return render(request,'appblog/search.html',{'search_result':search_result,'resultas':resultas,'post':post,'categorie8':categorie8,'categorie9':categorie9,'categorie1':categorie1,'categorie2':categorie2,'categorie3':categorie3,'categorie4':categorie4,'categorie5':categorie5,'categorie6':categorie6,'categorie7':categorie7})
		else:
			return render(request,'appblog/search.html',{'post':post,'categorie8':categorie8,'categorie9':categorie9,'categorie1':categorie1,'categorie2':categorie2,'categorie3':categorie3,'categorie4':categorie4,'categorie5':categorie5,'categorie6':categorie6,'categorie7':categorie7})
	else:
		return render(request,'appblog/search.html',{'search_result':search_result,'post':post,'categorie8':categorie8,'categorie9':categorie9,'categorie1':categorie1,'categorie2':categorie2,'categorie3':categorie3,'categorie4':categorie4,'categorie5':categorie5,'categorie6':categorie6,'categorie7':categorie7})





@login_required(login_url='login-view')

def CoursView(request):

	categorie1=Cours.objects.filter(matier="python")
	categorie2=Cours.objects.filter(matier="java")
	categorie3=Cours.objects.filter(matier="django")
	categorie4=Cours.objects.filter(matier="javascript")
	categorie5=Cours.objects.filter(matier="css3")
	categorie6=Cours.objects.filter(matier="c")
	categorie7=Cours.objects.filter(matier="html")
	categorie8=Cours.objects.filter(matier="bootstrap")
	doc=Cours.objects.all()
	

	context={'doc':doc,'categorie8':categorie8 ,'categorie1':categorie1,'categorie2':categorie2,'categorie3':categorie3,'categorie4':categorie4,'categorie5':categorie5,'categorie6':categorie6,'categorie7':categorie7}
	return render(request,'appblog/cours.html',context)






def Contact_view(request):
	categorie1=Post.objects.filter(categorie="python")
	categorie2=Post.objects.filter(categorie="java")
	categorie3=Post.objects.filter(categorie="django")
	categorie4=Post.objects.filter(categorie="javascript")
	categorie5=Post.objects.filter(categorie="css3")
	categorie6=Post.objects.filter(categorie="c")
	categorie7=Post.objects.filter(categorie="html")
	categorie8=Post.objects.filter(categorie="bootstrap")
	categorie9=Post.objects.filter(categorie="autres")
	post=Post.objects.all()
	if request.method == 'GET':
		form = CommentForm1()
	else:
		form = CommentForm1(request.POST,request.FILES)
		if form.is_valid():
			subject =request.POST.get('subject')
			email =request.POST.get('email')
			message = request.POST.get('message')
			email = EmailMessage(
			subject,
			message+"\n\n\n\n\n\n\n "+"Emetteur:"+" "+email,
			email,
			['massalylamine22@gmail.com'],
			headers={'Reply-To': email})
			if request.FILES:
				uploaded_file = request.FILES['document']
				email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
			form.save()
			messages.success(request,"votre message est bien envoyer a l'administrateur du site vous recevrais une reponse en moins de 24 heurs !!!!")
			email.send()
			return redirect('/')
	return render(request, "appblog/contact.html", {'form': form,'categorie8':categorie8 ,'categorie1':categorie1,'categorie2':categorie2,'categorie3':categorie3,'categorie4':categorie4,'categorie5':categorie5,'categorie6':categorie6,'categorie7':categorie7})



def PostView(request):
	categorie1=Post.objects.filter(categorie="python")
	categorie2=Post.objects.filter(categorie="java")
	categorie3=Post.objects.filter(categorie="django")
	categorie4=Post.objects.filter(categorie="javascript")
	categorie5=Post.objects.filter(categorie="css3")
	categorie6=Post.objects.filter(categorie="c")
	categorie7=Post.objects.filter(categorie="html")
	categorie8=Post.objects.filter(categorie="annonces")
	categorie9=Post.objects.filter(categorie="autres")
	post = Post.objects.all()
	paginator = Paginator(post, 3) # Show 3 contacts per page.
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)

	return render(request, 'appblog/index.html',{'post':post,'page_obj': page_obj,'categorie8':categorie8,'categorie9':categorie9,'categorie1':categorie1,'categorie2':categorie2,'categorie3':categorie3,'categorie4':categorie4,'categorie5':categorie5,'categorie6':categorie6,'categorie7':categorie7})


@login_required(login_url='login-view')
def post_detail(request, slug):
	categorie1=Post.objects.filter(categorie="python")
	categorie2=Post.objects.filter(categorie="java")
	categorie3=Post.objects.filter(categorie="django")
	categorie4=Post.objects.filter(categorie="javascript")
	categorie5=Post.objects.filter(categorie="css3")
	categorie6=Post.objects.filter(categorie="c")
	categorie7=Post.objects.filter(categorie="html")
	categorie8=Post.objects.filter(categorie="annonces")
	categorie9=Post.objects.filter(categorie="autres")
	post_data = Post.objects.all()
	# profile
	profile_pic=Profile.objects.get(user=request.user)
	# affciher le bouton sup si log== admin
	if request.user.username=='admin':
		delete_post=True
	else:
		delete_post=False

	template_name ="appblog/detail.html"
	post = get_object_or_404(Post, pk=slug)
	comments = post.comments.all()
	new_comment=None
	if request.method == 'POST':

		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():

			new_comment = comment_form.save(commit=False) 
			new_comment.post = post
			new_comment.photo=profile_pic.photo
			new_comment.email=request.user.email
			new_comment.name=request.user.first_name +" "+request.user.last_name
			new_comment.save()
			messages.success(request,"votre commentaire est bien enregsitrer merci")	
			return redirect('detail-view',slug=post.pk)	
	
	else:
		comment_form = CommentForm()
	return render(request, template_name, {'delete_post':delete_post,'post': post,'comments': comments,'comment_form': comment_form,'categorie8':categorie8,'categorie9':categorie9,'categorie1':categorie1,'categorie2':categorie2,'categorie3':categorie3,'categorie4':categorie4,'categorie5':categorie5,'categorie6':categorie6,'categorie7':categorie7,'postdata':post_data})






	
@login_required(login_url='login-view')
def CategoryView(request,cat_id):

	categorie1=Post.objects.filter(categorie="python")
	categorie2=Post.objects.filter(categorie="java")
	categorie3=Post.objects.filter(categorie="django")
	categorie4=Post.objects.filter(categorie="javascript")
	categorie5=Post.objects.filter(categorie="css3")
	categorie6=Post.objects.filter(categorie="c")
	categorie7=Post.objects.filter(categorie="html")
	data=Post.objects.filter(categorie=cat_id)
	p=Post.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(data, 5)	
	try:
		data = paginator.page(page)
	except PageNotAnInteger:
		data = paginator.page(1)
	except EmptyPage:
		data = paginator.page(paginator.num_pages)
	context={'p':p,'data':data,'categorie1':categorie1,'categorie2':categorie2,'categorie3':categorie3,'categorie4':categorie4,'categorie5':categorie5,'categorie6':categorie6,'categorie7':categorie7}
	return render(request,'appblog/category.html',context)
