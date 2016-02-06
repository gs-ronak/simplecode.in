#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from django import forms

from pagedown.widgets import AdminPagedownWidget


class BlogForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'size': 118}))
    content = forms.CharField(label='Content', widget=AdminPagedownWidget())
    snippet = forms.CharField(label='Summary',
                              widget=forms.Textarea(attrs={'cols': 85, 'rows': 7}),
                              required=False)

    def save(self, commit=True):
        instance = super(BlogForm, self).save(commit=False)
        if instance.status == 'p' and instance.publish_time is None:
            instance.publish_time = datetime.datetime.now()
        if commit:
            instance.save()
        return instance

