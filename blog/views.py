from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required, permission_required

from blog.models import *
from blog.forms import *


def post_list(request):
    """
    Show all published posts. Latest posts go first.
    """
    posts = Post.objects.exclude(published_date__isnull=True).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """
    Show detailed view of a certain post.
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    """
    Create a new post.
    Only for authorized users.
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    """
    Edit certain post.
    Allowed only for authenticated and authorized users (administrator and post author only).
    """
    post = get_object_or_404(Post, pk=pk)

    if request.user.pk != post.author.pk and not request.user.has_perm('blog.post_change'):
        return redirect('no-rights')

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            #post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_draft_list(request):
    """
    Show all current user's posts not published yet.
    """
    print(request.user.username, request.user.pk)
    posts = Post.objects.\
        filter(published_date__isnull=True).\
        filter(author_id__exact=request.user.pk ).\
        order_by('-created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
@permission_required('blog.post_publish', login_url='no-rights')
def post_publish(request, pk):
    """
    Publish certain unpublished post.
    Only for administrators.
    """
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    """
    Remove certain post.
    Only for authors and administrators.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.user.pk != post.author.pk and not request.user.has_perm('blog.post_change'):
        return redirect('no-rights')
    else:
        post.delete()

    return redirect('post_list')


@login_required
def add_comment_to_post(request, pk):
    """
    Add comment to a post.
    For authenticated users.
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
@permission_required('blog.comment_approve', login_url='no-rights')
def comment_approve(request, pk):
    """
    Approve comment to be shown for all visitors.
    Allowed for administrators only.
    """
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    """
    Remove comment that has not been published yet.
    """
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


def no_rights(request):
    """
    Show page that says that a user has insufficient rights to do something.
    """
    return render(request, 'registration/no-rights.html')
