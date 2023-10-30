from django.shortcuts import render, get_object_or_404, redirect
from .forms import AnnouncementForm, CommentForm
from django.shortcuts import render
from .models import Announcement


def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, './advertisements/announcement_list.html', {'announcements': announcements})


def announcement_create(request):
    if request.method == "POST":
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.save()
            return redirect('announcement_detail', pk=announcement.pk)
    else:
        form = AnnouncementForm()
    return render(request, './advertisements/announcement_create.html', {'form': form})


def announcement_detail(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.announcement = announcement
            comment.save()
            # здесь может быть перенаправление, или просто продолжайте рендерить тот же шаблон с новым комментарием
    return render(request, 'advertisements/announcement_detail.html', {'announcement': announcement, 'comment_form': form})


def add_comment_to_announcement(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.announcement = announcement
            comment.save()
            return redirect('announcement_detail', pk=announcement.pk)
    else:
        form = CommentForm()
    return render(request, './advertisements/add_comment_to_announcement.html', {'form': form})


def announcement_edit(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    if request.method == "POST":
        form = AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.save()
            return redirect('announcement_detail', pk=announcement.pk)
    else:
        form = AnnouncementForm(instance=announcement)
    return render(request, 'advertisements/announcement_create.html', {'form': form})


def announcement_delete(request, pk):
    announcement = get_object_or_404(Announcement, pk=pk)
    announcement.delete()
    return redirect('home')
