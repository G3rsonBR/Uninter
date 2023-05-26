def valida_int(pergunta, min, max):
    try:
        x = float(input(pergunta))
        while ((x < min) or (x > max)):
            x = float(input(pergunta))
        return x
    except ValueError:
        print('x')

def criaArquivo(nomeDoArquivo):
    try:
        a = open(nomeDoArquivo, 'wt+')
        a.close()
    except:
        print('Erro na Criação do Arquivo')
    else:
        print('Arquivo {} foi criado\n'.format(nomeDoArquivo))

def existeArquivo(nomeDoArquivo):
    try:
        a = open(nomeDoArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def cadastrarJogo(nomeArquivo, nomeJogo, plataformaJogo):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomeJogo, plataformaJogo))
    finally:
        a.close()

def listarArquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()

arquivo = 'games.txt'
if existeArquivo(arquivo):
    print('Localizado')
else:
    print('Inexistente')
    criaArquivo(arquivo)


while True:
    text = 'Escolha uma opção:\n1 - Cadastrar Novo Item\n2 - Listar Itens\n3 - Sair\n>>'
    escolher = valida_int(text, 1, 3)

    if escolher == 1:
        print('\nCadastrar Novo Item\n')
        nomeJogo = input('Digite o nome do Jogo: ')
        plataformaJogo = input('Digite a plataforma do Jogo:')
        cadastrarJogo(arquivo, nomeJogo, plataformaJogo)
    elif escolher == 2:
        print('\nListar Itens\n')
        listarArquivo(arquivo)
    elif escolher == 3:
        print('\nEncerrando programa....')
        break