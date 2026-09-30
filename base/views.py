from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie,Show,Seat,Booking,BookingSeat
from .forms import MovieModelForm, ShowModelForm, SeatModelForm, BookingModelForm, BookingSeatModelForm
from django.contrib.auth.decorators import login_required


# Create your views here.
#Movie
@login_required(login_url='signin')
def create(request):
    form = MovieModelForm(request.POST, request.FILES)
    if form.is_valid():
        record = form.save(commit = False)
        record.user = request.user
        record.save()
        return redirect('read')
    return render(request, 'create.html',{'form':form})    


@login_required(login_url='signin')
def read(request):
    data = Movie.objects.all()
    return render(request, 'read.html',{'data':data})

# def update(request, did):
#     record = get_object_or_404(Movie, id = did)
#     form = MovieModelForm(request.POST, request.FILES, instance = record)
#     if form.is_valid():
#         form.save()
#         return redirect('read')
#     return render(request, 'update.html',{'form':form})
@login_required(login_url='signin')
def update(request, did):

    record = get_object_or_404(Movie, id=did)

    if request.method == 'POST':
        form = MovieModelForm(
            request.POST,
            request.FILES,
            instance=record
        )

        if form.is_valid():
            form.save()
            return redirect('read')

    else:
        form = MovieModelForm(instance=record)

    return render(request, 'update.html', {'form': form})


@login_required(login_url='signin')
def delete(request, did):
    record = get_object_or_404(Movie, id = did)
    if request.method == 'POST':
        record.delete()
        return redirect('read')
    return render(request, 'delete.html',{'data':record})

# Show
@login_required(login_url='signin')
def show_create(request):
    form = ShowModelForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('show_read')
    return render(request, 'show_create.html',{'form':form})    


@login_required(login_url='signin')
def show_read(request):
    data = Show.objects.all()
    return render(request, 'show_read.html',{'data':data})

@login_required(login_url='signin')
def show_update(request,sid):
    record = get_object_or_404(Show, id = sid)
    form = ShowModelForm(request.POST, request.FILES, instance = record)
    if form.is_valid():
        form.save()
        return redirect('show_read')
    return render(request, 'show_update.html',{'form':form})

 
@login_required(login_url='signin')   
def show_delete(request,sid):
    record = get_object_or_404(Show, id = sid)
    if request.method == 'POST':
        record.delete()
        return redirect('show_read')
    return render(request, 'show_delete.html',{'data':record})

# Seta
@login_required(login_url='signin')
def seat_create(request):
    form = SeatModelForm(request.POST, request.FILES)
    if form.is_valid():
        record = form.save(commit = False)
        record.user = request.user
        record.save()
        return redirect('seat_read')
    return render(request, 'seat_create.html',{'form':form}) 


@login_required(login_url='signin')
def seat_read(request):
    data = Seat.objects.all()
    return render(request,'seat_read.html',{'data':data})


@login_required(login_url='signin')
def seat_update(request,sis):
    record = get_object_or_404(Seat, id = sis)
    form = SeatModelForm(request.POST, request.FILES, instance = record)
    if form.is_valid():
        form.save()
        return redirect('read')
    return render(request, 'seat_update.html',{'form':form})

@login_required(login_url='signin')
def seat_delete(request,sis):
    record = get_object_or_404(Seat, id = sis)
    if request.method == 'POST':
        record.delete()
        return redirect('seat_read')
    return render(request, 'seat_delete.html',{'data':record})

#Booking
@login_required(login_url='signin')
def booking_create(request):
    form = BookingModelForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('booking_read')
    return render(request, 'booking_create.html',{'form':form})   
    
@login_required(login_url='signin')
def booking_read(request):
    data = Booking.objects.all()
    return render(request,'booking_read.html',{'data':data})


@login_required(login_url='signin')
def booking_update(request,bib):
    record = get_object_or_404(Booking, id = bib)
    form = BookingModelForm(request.POST, request.FILES, instance = record)
    if form.is_valid():
        form.save()
        return redirect('booking_read')
    return render(request, 'booking_update.html',{'form':form})


@login_required(login_url='signin')
def booking_delete(request,bib):
    record = get_object_or_404(Booking, id = bib)
    if request.method == 'POST':
        record.delete()
        return redirect('booking_read')
    return render(request, 'booking_delete.html',{'data':record})

#Bookingseat


@login_required(login_url='signin')
def bookseat_create(request):
    form = BookingSeatModelForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('show_read')
    return render(request, 'bookseat_create.html',{'form':form})  


@login_required(login_url='signin')
def bookseat_read(request):
    data = BookingSeat.objects.all()
    return render(request,'bookseat_read.html',{'data':data})
    


@login_required(login_url='signin')
def bookseat_update(request,bs):
    record = get_object_or_404(BookingSeat, id = bs)
    form = BookingSeatModelForm(request.POST, request.FILES, instance = record)
    if form.is_valid():
        form.save()
        return redirect('bookseat_read')
    return render(request, 'bookseat_update.html',{'form':form})
    


@login_required(login_url='signin')
def bookseat_delete(request,bs):
    record = get_object_or_404(BookingSeat, id = bs)
    if request.method == 'POST':
        record.delete()
        return redirect('bookseat_read')
    return render(request, 'bookseat_delete.html',{'data':record})

                


            



