# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    # This is for the single user, who can edit and process the blog i. e. superuser
    # This author belongs to the superuser
    title = models.CharField(max_length=200)
    text = models.TextField()    # The text field is empty because the blog text is undefined.
    create_date = models.DateField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)
    # inputs for published date is kept blank because I may not want to publish the blog and null because I may not
    # have publication date.

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        # The blog creation and publication dates may be different.

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    # Here among the comments the approved and not approved will separate and approved will appear with the blog.

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})   # After hitting the publication button the url should
        # take to post_detail page where primary key of that post is created.

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)  # default=Fault: Initially the comment is not approved.
    # The approved comment in Post.approved_comment return is same as the above approved_comment

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')     # After posting a comment the url redirects to post_list page.

    def __str__(self):
        return self.text




