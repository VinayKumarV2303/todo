# board/views.py
from django.shortcuts import render

def board_view(request):
    return render(request, "board.html")  # this will look for templates/board.html
