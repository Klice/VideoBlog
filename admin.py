# -*- coding: utf-8 -*-
# from django.db import models
from django.contrib import admin
from videoblog.models import Video, ViewStats, VideoTags
from tagging_autocomplete.widgets import TagAutocomplete
# from django.forms import TextInput


class ViewStatsAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'video_from', 'video_to', 'views')


class VideoAdmin(admin.ModelAdmin):
    formfield_overrides = {
        VideoTags: {'widget': TagAutocomplete}
    }
    date_hierarchy = 'date'
    list_filter = ('hoster',)
    search_fields = ['name', 'desc']
    list_display = ('name', 'hoster', 'tags')
    # list_editable = ('name', 'tags')
    # formfield_overrides = {
    #     models.CharField: {'widget': TextInput(attrs={'size': '60'})},
    # }


admin.site.register(Video, VideoAdmin)
admin.site.register(ViewStats, ViewStatsAdmin)
