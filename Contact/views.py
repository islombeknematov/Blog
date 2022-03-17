from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView
from Contact.models import ContactModel

            # Class Based View
            
class ContactCreateView(CreateView):
    template_name = 'contact.html'
    model = ContactModel
    fields = ['name', 'email', 'subject', 'message']
    success_url = '/'



            # Function Based View
                    
# def contact_create(request):
#     if request.method == 'POST':
#         form = ContactModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#         else:
#             from = ContactModelForm()

#         context = {'form': form}

#         return render(request, 'contact.html', context)



