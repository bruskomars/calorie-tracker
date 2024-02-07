from django.shortcuts import render, redirect
from .models import Food, Consume

# Create your views here.

def index(request):

    if request.method == "POST":
        food_consumed = request.POST.get('food_consumed')
        food = Food.objects.get(name=food_consumed)
        user = request.user

        add_food = Consume(food_consumed=food, user=user)
        add_food.save()

        return redirect('index')

    consume = Consume.objects.filter(user=request.user)
    foods = Food.objects.all()

    context = {
        'foods': foods,
        'consume': consume,
    }
    return render(request, 'myapp/index.html', context)

def delete(request, pk):
    item = Consume.objects.get(id=pk)

    if request.method == "POST":
        item.delete()

        return redirect('index')

    return render(request, 'myapp/delete.html')