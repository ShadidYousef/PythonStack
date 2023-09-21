from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def result(request):
    user_name = request.POST['username']
    dojo_location = request.POST['dojo_location']
    favorite_language = request.POST['favorite_language']
    comment = request.POST['comment']
    submit_dic = {
        "username": user_name,
        "dojo_location": dojo_location,
        "favorite_language": favorite_language,
        "comment": comment
    }
    return render(request, 'submit.html', submit_dic)
