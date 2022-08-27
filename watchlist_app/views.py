# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse

# # Create your views here.

# def movie_list(request):
#     movies = Movie.objects.all()
#     #all items will display as a list
#     data = {
#         'movies' : list(movies.values())
#         }
#     #values() is used to change items from listen to python dictonary
    
#     return JsonResponse(data) 
#     #Json will only return a python dictionary
#     #You tell if an item is json if True is treu , and there is no single quote
    
# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name' : movie.name,
#         'description' : movie.description,
#         'active' : movie.active
#     }
#     #The process of converting a complex data type into a python dictionary and rendering is known as SERIALIZATION
#     #DESERIALIZATION is collecting a jsonResponse from the user and converting it onto a complex data type
#     return JsonResponse(data)
