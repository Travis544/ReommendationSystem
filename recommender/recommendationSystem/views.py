from django.shortcuts import render
import requests


def getMovie(name):
    key="7d703b21"
    url = "http://www.omdbapi.com/?apikey="+key
    
    querystring = {"t":name,"r":"json","plot":"short"}
    # headers = {
    #     'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
    #     'x-rapidapi-key': "13a49c360fmsh78477b749e300d3p15db75jsncb92b421ad96"
    #     }

    response = requests.request("GET", url, params=querystring)
    
    print(response.text)
    return response

# Create your views here.
def home(request):
    if request.session.get("selectedGenres")!=None:
        request.session['selectedGenres'] =[]
    # getMovie("Titanic")
    # will eventually change this genre list to get form the movie dataset
    return render(request, "movie.html", {"genres": ["Comedy", "Action", "Romance"]})

def selectGenre(request):
    if request.session.get("selectedGenres")==None:
        request.session['selectedGenres'] =[]
    else:
       arr= request.session['selectedGenres']
       genre=request.POST['genre']
       if not genre in arr:
            arr.append(genre)
       request.session['selectedGenres']=arr
    print(request.session.get("genres"))
    return render(request, "movie.html", 
           {"genres": ["Comedy", "Action", "Romance"], "selectedGenre": request.session.get("selectedGenres")})

def recommendMovies(request):
    if request.method=="POST":
       # print(request.POST)
        genre=request.POST['genre']
        movieText=request.POST['movieLike']
        print(genre)
        print(movieText)
    return render(request, "recommendations.html")