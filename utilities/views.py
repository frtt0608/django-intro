from django.shortcuts import render, HttpResponse
import datetime, requests, os


# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')
    
def graduation(request):
    time = datetime.datetime.now()
    grad = datetime.datetime(2019,5,17)
    dt = grad - time
    return render(request, 'utilities/graduation.html', {'time':time, 'grad':grad, 'dt':dt})
 
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
    
def today(request):
    url = "https://api.openweathermap.org/data/2.5/weather?"
    q = 'Daejeon,kr'
    appid = 'ed959cca83201f4e7425e15ef3ff3bbe'
    urls = url+'q='+q+'&'+'appid='+appid
    response = requests.get(urls).json()
    weather = response["weather"][0]["main"]
    name = response["name"]
    nows = datetime.datetime.now()
    end_ssafy = datetime.datetime(2019,2,18,18)
    dt = end_ssafy-nows
    # https://api.openweathermap.org/data/2.5/weather?q=Daejeon,kr&appid=ed959cca83201f4e7425e15ef3ff3bbe
    return render(request, 'utilities/today.html', {'nows':nows, 'dt':dt,'weather':weather, 'name':name})
    
    
def ascii_new(request):
    words = ['short', 'utopia', 'rounded', 'acrobatic', 'alligator']
    return render(request, 'utilities/ascii_new.html', {'words':words})
    
def ascii_make(request):
    text = request.POST.get("text")
    font = request.POST.get("font")
    url = "http://artii.herokuapp.com/make?"
    urls = url + 'text=' + text + '&font=' + font
    response = requests.get(urls).text
    # http://artii.herokuapp.com/make?text=ASCII&font=shorts
    return render(request, 'utilities/ascii_make.html', {'response': response} )
    
def original(request):
    return render(request, 'utilities/original.html')
    
def translated(request):
    text = request.POST.get("text")
    
    naver_client_id = "Cl0gXEE3CjuQZ03qEVGj"
    naver_client_secret = "vkxWPOWgYh"
    
    papago_url = "https://openapi.naver.com/v1/papago/n2mt"

    headers = {
        "X-Naver-Client-Id": naver_client_id,
        "X-Naver-Client-Secret": naver_client_secret
    }
    
    data = {
        "source": "ko",
        "target": "en",
        "text": text
    }
    
    papago_response = requests.post(papago_url, headers=headers, data=data).json()
    
    reply_text = papago_response["message"]["result"]["translatedText"]
    
    return render(request, 'utilities/translated.html', {'text':text,'reply_text': reply_text})