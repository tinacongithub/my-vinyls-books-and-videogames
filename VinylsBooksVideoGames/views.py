from django.shortcuts import render
from VinylsBooksVideoGames.models import Vinyls
from VinylsBooksVideoGames.models import Books
from VinylsBooksVideoGames.models import Videogames
from VinylsBooksVideoGames.forms import Search
from django.views import View
from django.views.generic import CreateView

def show_vinyls(request):
  vinyls_list = Vinyls.objects.all()
  return render(request, "VinylsBooksVideoGames/vinyls.html", {"vinyls_list": vinyls_list})

def show_books(request):
  books_list = Books.objects.all()
  return render(request, "VinylsBooksVideoGames/books.html", {"books_list": books_list})

def show_videogames(request):
  videogames_list = Videogames.objects.all()
  return render(request, "VinylsBooksVideoGames/videogames.html", {"videogames_list": videogames_list})

class SearchItem(View):
    form_class = Search
    template_name = 'VinylsBooksVideoGames/search.html'
    initial = {"title":""}
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            vinyls_list = Vinyls.objects.filter(title__icontains=title).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'vinyls_list':vinyls_list,
                                                        }
                                                        )
        return render(request, self.template_name, {"form": form})

class VinylAdd(CreateView):
  model = Vinyls
  success_url = "/vinyls"
  fields = ["title", "artist", "tracks"]

class BookAdd(CreateView):
  model = Books
  success_url = "/books"
  fields = ["title", "author", "year_published"]

class VideogameAdd(CreateView):
  model = Videogames
  success_url = "/videogames"
  fields = ["title", "genre", "year_released"]