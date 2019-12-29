from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Board, Post

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})

def board_posts(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'posts.html', {'board': board})

def new_post(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if request.method == 'POST':
        description = request.POST.get('description')

        user = User.objects.first()  # TODO: get the currently logged in user

        post = Post.objects.create(
            description=description
        )

        return redirect('board_posts', pk=board.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_post.html', {'board': board})