from django.shortcuts import render, get_object_or_404, redirect
from .models import QueueL
from .forms import QueueForm


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
        form = QueueForm(request.POST, request.FILES)
        if form.is_valid():
            # queue = queue.objects.create(**form.cleaned_data)
            queue = form.save()
            return redirect(queue)
    else:
        form = QueueForm()
    return render(request, 'queue_l/add_queue.html', {'form': form})
