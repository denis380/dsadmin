from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import Impressora, Busca_Rede, Busca_Coluna
from .models import Printer
from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
from django.contrib.auth.decorators import login_required



@login_required
def novaPrinter(request): # Cadastra uma nova impressora.
    form = Impressora(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('consultaPrinter')
    return render(request, 'nova_printer.html', {'form': form})# passando a form de com os dados das impressoras

@login_required
def consultaPrinter(request):#pega todos as impressoras listadas no banco de dados.
    printer = Printer.objects.all()
    return render(request, 'printer_list.html', {'printer': printer})

@login_required
def consultaRede(request): # Pega o ip passado pelo usuário.
    form = Busca_Rede(request.POST or None)
    form2 = Busca_Coluna(request.POST or None)
    return render(request, 'busca_rede.html', {'form2': form2 , 'form': form})

@login_required
def buscaPorIp(request):# Pega o IP e retorna o serial e o contador da impressora.
    if request.method == 'POST':
        form = Busca_Rede(request.POST)
        if form.is_valid():
            ip = form.cleaned_data['ip'] # Pega o IP preenchido na form pelo usuario

    try:  # Testa se a impressora está online.
        test = requests.get('http://'+ ip)

    except ConnectionError:
        erro = 'Não foi possível acessar a impressora!!'
        return render(request, 'erros.html', {'erro': erro})


    serial = buscaSerial(ip)
    cont = buscaCont(ip)
    dados = {'serial': serial, 'cont': cont}

    return render(request, 'info.html', dados)

@login_required
def atualizar(request, id): # Atualiza o equipamento no banco de dados.
    printer = get_object_or_404(Printer, pk=id)
    form = Impressora(request.POST or None, request.FILES or None, instance=printer)

    if form.is_valid():
        form.save()
        return redirect('consultaPrinter')

    return render(request, 'nova_printer.html', {'form': form})

@login_required
def impRetorno(request, ip):

    serial = buscaSerial(ip)
    contador = buscaCont(ip)

    return render(request, 'info.html', {'contador': contador}, {'serial': serial})

def buscaCont(ip):

    url = 'http://' + ip + '/cgi-bin/dynamic/printer/config/reports/deviceinfo.html'

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'lxml')

    b = soup.find_all('p')  # Diminuindo o conteúdo de busca

    stringSoup = str(b)  # Passando a busca para uma string

    listResult = stringSoup.split()  # Cria uma lista a partir da String

    indice = (listResult.index('pág.</p>,') + 3)  # Pega o indice correto do contador

    cont = listResult[indice]

    return cont

def buscaSerial(ip):

    url = 'http://' + ip + '/cgi-bin/dynamic/printer/config/reports/deviceinfo.html'

    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'lxml')

    b = soup.find_all('p')  # Diminuindo o conteúdo de busca

    stringSoup = str(b)  # Passando a busca para uma string

    listResult = stringSoup.split()  # Cria uma lista a partir da String

    indice = (listResult.index('série</p>,') + 3)  # Pega o indice do Serial correto

    serial = listResult[indice]

    return serial

@login_required
def deletar(request, id): # Deleta o equipamento no banco de dados.
    printer = get_object_or_404(Printer, pk=id)
    form = Impressora(request.POST or None, request.FILES or None, instance=printer)

    if request.method == 'POST':
        printer.delete()
        return redirect('consultaPrinter')
    return render(request, 'deletar_printer.html', {'form': form})

def inicio(request):
    return render(request, 'index.html')

def buscaPorColuna(request):# Busca a impressora pela coluna ou lista as colunas correspondentes.
    if request.method == 'POST':
        form = Busca_Coluna(request.POST or None)
        if form.is_valid():
            col = form.cleaned_data['coluna']# Pega a coluna preenchida na form pelo usuario
        else:
            return HttpResponse('Referência invlálida!')


    coluna = str(col).upper()


    try:
        printer = Printer.objects.filter(coluna=coluna).order_by('ip').first()
        ip = printer.ip
        return redirect('http://'+ ip)
    except AttributeError:
        printerList = Printer.objects.filter(coluna__contains=(coluna))

        if not printerList:
            erro = 'Coluna não encontrada no banco de dados.'
            return render(request, 'erros.html', {'erro': erro})
        else:

            return render(request, 'lista_colunas.html', {'printerList': printerList})












