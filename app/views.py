from django.shortcuts import render, redirect, get_object_or_404
from .forms import DocumentForm, EditDescriptionForm
from .models import Document

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})

def upload_success(request):
    documents = Document.objects.all()
    return render(request, 'upload_success.html', {'documents': documents})

def delete_document(request, document_id):
    document = Document.objects.get(id=document_id)
    document.delete()
    return redirect('upload_success')

def edit_description(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == 'POST':
        form = EditDescriptionForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = EditDescriptionForm(instance=document)
    return render(request, 'edit_description.html', {'form': form})
