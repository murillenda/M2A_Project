from django.shortcuts import render


def login(request):
    return render(request, 'M2A_app/login.html')


def cadastro_usuario(request):
    return render(request, 'M2A_app/cadastro_usuario.html')


def cadastro_empresa(request):
    return render(request, 'M2A_app/cadastro_empresa.html')


def lista_diagnostico(request):
    return render(request, 'M2A_app/lista_diagnostico.html')


def lista_empresa(request):
    return render(request, 'M2A_app/lista_empresas.html')


def lista_grupo(request):
    return render(request, 'M2A_app/lista_grupo.html')


def lista_usuario(request):
    return render(request, 'M2A_app/lista_usuario.html')


def lista_respostas(request):
    return render(request, 'M2A_app/lista_respostas.html')


def dados_usuario(request):
    return render(request, 'M2A_app/dados_usuario.html')


def graficos(request):
    return render(request, 'M2A_app/graficos.html')


def registro_grupo(request):
    return render(request, 'M2A_app/registro_grupo.html')


def cadastro_diagnostico(request):
    return render(request, 'M2A_app/cadastro_diagnostico.html')


def cadastro_respostas(request):
    return render(request, 'M2A_app/cadastro_respostas.html')


def cadastro_perguntas(request):
    return render(request, 'M2A_app/cadastro_perguntas.html')


def cadastro_empresa_dois(request):
    return render(request, 'M2A_app/cadastro_empresa_dois.html')
