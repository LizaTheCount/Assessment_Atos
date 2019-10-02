from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Upload


class UploadList(ListView):
    model = Upload


class UploadView(DetailView):
    model = Upload


class UploadCreate(CreateView):
    model = Upload
    fields = ['car', 'mpg', 'cyl', 'cyl_disp', 'horsep', 'weight', 'accel', 'model', 'origin']
    success_url = reverse_lazy('dataapp:upload_list')


class UploadUpdate(UpdateView):
    model = Upload
    fields = ['car', 'mpg', 'cyl', 'cyl_disp', 'horsep', 'weight', 'accel', 'model', 'origin']
    success_url = reverse_lazy('dataapp:upload_list')


class UploadDelete(DeleteView):
    model = Upload
    success_url = reverse_lazy('dataapp:upload_list')


def database_upload(request):
    # If we get a post request, send the HTML form
    if request.method == 'GET':
        return render(request, 'dataapp/database_upload.html', {})

    COUNTRIES = {'US': 0,
                 'Europe': 1,
                 'Japan': 2}

    # take item named FILES from request. Read and Decode (Decode becauce NO ASCII plz) said file.
    csv_data = (request.FILES['csv_file']).read().decode("utf-8")
    lines = csv_data.split("\r\n")

    # new entries is a buffer for new upload objects
    new_entries = []
    # loop through all the rows in the csv
    for line in lines:
        # split row into column values
        fields = line.split(";")
        # .append will throw a new object in the buffer
        # Upload will create the new object with said parameters
        new_entries.append(Upload(
            car=str(fields[0]),
            mpg = float(fields[1]),
            cyl = int(fields[2]),
            cyl_disp = float(fields[3]),
            horsep = float(fields[4]),
            weight = float(fields[5]),
            accel = float(fields[6]),
            model = int(fields[7]),
            origin = COUNTRIES[fields[8]],
        ))
    # bulk_create is a django function that fill throw everything in the database all at once.
    Upload.objects.bulk_create(new_entries)
    # HttpResponse will let the user know everything went oke and that no error has occured
    return HttpResponse('OK')

