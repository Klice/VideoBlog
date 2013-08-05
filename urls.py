from django.conf.urls import patterns
from django.views.generic import TemplateView
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'add_video_url/$', 'videoblog.views.Add_Video_URL'),
    (r'add_video_url/$', 'videoblog.views.Add_Video_URL', {}),
    (r'movie/(?P<name>.+)-(?P<video_id>\d+)/$', 'videoblog.views.detail_video', {}, 'detail_video'),
    (r'movie/delete/(?P<id>\d+)/$',  'videoblog.views.delete_video', {}, 'delete_video'),
    (r'movie/edit_desc/(?P<id>\d+)/$',  'videoblog.views.edit_video_desc', {}, 'edit_video_desc'),
    (r'movie/edit_tags/(?P<id>\d+)/$',  'videoblog.views.edit_video_tags', {}, 'edit_video_tags'),
    (r'archive/(?P<month>\d+)/$', 'videoblog.views.videolist', {}, 'video_list_archive'),

    (r'movie/vote_good/(?P<id>\d+)/$', 'videoblog.views.video_vote', {'res': 1}, 'video_vote_good'),
    (r'movie/vote_bad/(?P<id>\d+)/$', 'videoblog.views.video_vote', {'res': -1}, 'video_vote_bad'),

    (r'add_amazon_url/$', 'videoblog.views.Add_Video_Amazon_URL'),

    (r'tag/(?P<tag>[\w ^/]+)/$', 'videoblog.views.videolist', {}, 'tag_list'),

    (r'tags/$', 'videoblog.views.tagslist', {}, 'tags_list'),

    (r'archive/(?P<month>\d+)/(?P<cur_page>\d+)/$',  'videoblog.views.videolist', {'tag': None}, 'video_list_page'),
    (r'tag/(?P<tag>[\w ^/]+)/page-(?P<cur_page>\d+)/$', 'videoblog.views.videolist', {'month': None}, 'video_list_page'),
    (r'page/(?P<cur_page>\d+)/$', 'videoblog.views.videolist', {'tag': None, 'month': None}, 'video_list_page'),

    (r'feedback/$', 'videoblog.views.feedback', {}, 'feedback'),
    (r'feedback/ok/$', TemplateView.as_view(template_name="feedback_ok.html"), {}, 'feedback_ok'),
    (r'random/$', 'videoblog.views.random_video', {}, 'random'),
    
)
