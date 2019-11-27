from django.shortcuts import render
from . models import Video
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class VideoListView(ListView):
	model = Video
	queryset = Video.objects.order_by('title')


class VideoThumbsView(ListView):
	model = Video
	template_name = "videos/video_thumbs.html"
	context_object_name = 'video_thumbs'

	#filtering records by category_id
	def get_queryset(self):
		return Video.objects.filter(category_id = self.kwargs['category_id']).filter(is_active = True)


class VideoDetailView(DetailView):
	model = Video


class VideoCreateView(SuccessMessageMixin, CreateView):
	model = Video
	fields = ['title','author','description','youtube_vid','stars_count','category_id','skill_level_id','is_active']
	success_message = "Video added!"
	success_url = reverse_lazy('videos-list')


class VideoUpdateView(SuccessMessageMixin, UpdateView):
	model = Video
	fields = ['title','author','description','youtube_vid','stars_count','category_id','skill_level_id','is_active']
	success_message = "Video updated!"
	success_url = reverse_lazy('videos-list')


class VideoDeleteView(SuccessMessageMixin, DeleteView):
	model = Video
	success_message = "Video deleted!"
	success_url = reverse_lazy('videos-list')
		