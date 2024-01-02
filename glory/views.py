from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Juice, Ingredients, Room

class HomeView(TemplateView):
    template_name = 'home.html'

class BartenderView(TemplateView):
    template_name = 'bartender.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        juice = Juice.objects.all()
        ingredient = Ingredients.objects.all()        
        context['juice'] = juice
        return context

class RoomView(TemplateView):
    template_name = 'room.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        juice_id = self.kwargs['pk']
        juice_obj = Juice.objects.get(id=juice_id)
        context['juice'] = juice_obj
        return context

class OrderView(TemplateView):
    template_name = 'ordercheck.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        juice_id = self.kwargs['pk']
        juice_obj = Juice.objects.get(id=juice_id)
        room_number = self.request.GET.get('message')
        check = Room.objects.filter(room_number=room_number)
        print(check)
        if check.exists():
            room_obj = Room.objects.get(room_number=room_number)
            context['room'] = room_obj.order_check
            print(room_number)
        else:
            room_obj = Room.objects.create(
                juice = juice_obj,
                room_number = room_number
            )
            room_obj.save()
            print(room_obj)
            context['room'] = room_obj.order_check
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

class DiningView(TemplateView):
    template_name = 'dining.html'

class SuiteView(TemplateView):
    template_name = 'suite.html'

class ActivitiesView(TemplateView):
    template_name = 'activities.html'

class WeddingView(TemplateView):
    template_name = 'weddings.html'

class MeetingView(TemplateView):
    template_name = 'meetings.html'

# class RoomView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         juice_id = self.kwargs['pk']
#         juice_obj = Juice.objects.get(id=juice_id)
#         room_number = self.request.GET.get('room')
#         print(juice_obj)
#         print(room_number)

#         context = {
#             'juice': juice_obj
#         }
#         return render(request, 'room.html', context)


        
    
