from django.shortcuts import render, redirect
from .models import post, comment
from django.contrib.auth.decorators import login_required


@login_required(login_url="/admin")
def home(request):
    for i in post.objects.all():
        comments = i.comment_set.all()
        i.comments_number = len(comments)
        i.save()
    context = {
        'posts':post.objects.all()
    }

    return render(request, 'post/home.html', context)

def post_detail_view(request, id):
    post_x = post.objects.all().filter(id=id)[0]
    comments = post_x.comment_set.all()
    for comment in comments:
        replys = comment.reply_set.all()
        comment.replys.set(replys)
        comment.save()
    context = {
        'post':post_x,
        'comments':comments
    }
    return render(request, 'post/post_detail.html', context)

def like(request, id):
    post_x = post.objects.all().filter(id=id)[0]
    already_liked = False 
    for i in post_x.user_liked.all():
        if i == request.user:
            already_liked = True 
    
    if already_liked == False:
        post_x.user_liked.add(request.user)
    else:
        post_x.user_liked.remove(request.user)

    return redirect('home')

def like_detail(request, id):
    post_x = post.objects.all().filter(id=id)[0]
    already_liked = False 
    for i in post_x.user_liked.all():
        if i == request.user:
            already_liked = True 
    
    if already_liked == False:
        post_x.user_liked.add(request.user)
    else:
        post_x.user_liked.remove(request.user)

    return redirect('post-detail', id)
    
def comment_like(request, id, comment_id):
    comment_x = comment.objects.all().filter(id=comment_id)[0]
    already_liked = False 
    for i in comment_x.user_liked.all():
        if i == request.user:
            already_liked = True 
    
    if already_liked == False:
        comment_x.user_liked.add(request.user)
    else:
        comment_x.user_liked.remove(request.user)

    return redirect('post-detail', id) 