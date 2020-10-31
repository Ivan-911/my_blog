from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.urls import reverse

# Create your views here.
from blogs.models import BlogPost

def chec_blog_owner(owner, user):
	"""Проверяет является текущий пользователь владельцем"""
	return (owner.owner == user.user)

def index(request):
	""" Home's page"""
	return render(request, 'blogs/index.html')

def notes(request):
	"""Displays all notes"""
	all_notes = BlogPost.objects.order_by('date_added')
	context = {"all_notes":all_notes}
	return render(request, 'blogs/notes.html', context)

def note(request, note_id):
	"""Returns the selected note."""
	note = BlogPost.objects.get(id=note_id)
	title = note.title
	text = note.text
	date = note.date_added
	note_id = note.id
	context = {'title':title, 'text':text, 'date': date, 'note_id':note_id}
	return render(request, 'blogs/note.html', context)
@login_required
def new(request):
	"""Пытаемся вывести форму на экран"""
	if request.method != 'POST':
		form = PostForm()
	else:
		form = PostForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('blogs:notes'))
	context = {'form': form}
	return render(request, 'blogs/new.html', context)
@login_required
def edit_blog(request, note_id):
	"""Edit blog"""
	blog = BlogPost.objects.get(id=note_id)
	if not chec_blog_owner(blog, request):
		raise Http404
	if request.method != 'POST':
		form = PostForm(instance=blog)
	else:
		#Отправка данных POST обработать данные
		form = PostForm(instance=blog, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:note', args=[blog.id]))
	context = {'blog':blog, 'form':form}
	return render(request, 'blogs/edit_blog.html', context)
