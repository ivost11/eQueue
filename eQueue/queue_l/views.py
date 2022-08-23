from django.shortcuts import render, get_object_or_404, redirect
from .models import QueueL
from .forms import AddQueueForm, DeleteQueueForm


def index(request):
    queues_cntx = QueueL.objects.all()
    context = {
        'queues': queues_cntx,
        'title': 'Список черг',
    }
    return render(request, 'queue_l/index.html', context)


def get_queue(request, queue_id):
    queue_item = get_object_or_404(QueueL, pk=queue_id)
    return render(request, 'queue_l/view_queue.html', {'item': queue_item})


def add_queue(request):
    if request.method == 'POST':
        print(request)
        form = AddQueueForm(request.POST, request.FILES)
        if form.is_valid():
            queue = form.save()
            return redirect(queue)
    else:
        form = AddQueueForm()
    return render(request, 'queue_l/add_queue.html', {'form': form})


def delete_queue(request):
    if request.method == 'POST':
        print(request)
        form = DeleteQueueForm(request.POST)
        if form.is_valid():
            QueueL.objects.filter(
                title=form.cleaned_data['title'], email=form.cleaned_data['email']).delete()
            return redirect('/')
    else:
        form = DeleteQueueForm()
    return render(request, 'queue_l/delete_queue.html', {'form': form})
