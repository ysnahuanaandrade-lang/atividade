# Programa principal: menu e telas.
import banco
import utilidades

def mostrar_menu():
    print('\n===============================')
    print('SISTEMA DE NOTAS ESCOLAR')
    print('================================')
    print('1 - Cadastrar aluno')
    print('2 - Lista de aluno')
    print('3 -Buscar aluno por nome ')
    print('4 - Atualizar notas')
    print('5 - Remover aluno')
    print('6 - Relatório da turma')
    print('0 - Sair')
    return input ('Escolha uma opção: ')

def mostrar_aluno(aluno):
    '''Mostra uma linha com os dados de um aluno.'''
    id_aluno, nome, nota1, nota2 = aluno 
    media = utilidades.calcular_media(nota1, nota2) 
    situacao= utilidades.situacao(media)
    print(f'[{id_aluno:>3}] {nome:<22}'
    f'N1: {nota1:>4} N2:{nota2:>4.1f} '
    f'Média: {media:4.1f} {situacao}')
    
def cadastrar_aluno():
    print('\n--- Cadastrar aluno ---')
    nome = utilidades.ler_texto('Nome:')
    nota1 =utilidades.ler_nota('Nota 1 (0 a 10): ')
    nota2 =utilidades.ler_nota('Nota 2 (0 a 10): ')
    banco.inserir_aluno(nome, nota1, nota2)
    print('Aluno cadastrar com sucesso!')

def listar_alunos():
    print('\n--- lister alunos ---')
    alunos = banco.lister_alunos()
    if len(alunos) == 0:
        print('Nenhum aluno encontrado.')
    return
    for aluno in alunos:
        mostrar_aluno()

def buscar_aluno():
    print('\n--- Buscar Alunos ---')
    texto = utilidades.ler_texto('Digite parte do nome:')
    if len(alunos) == 0:
        print('Nenhum aluno encontrado')
    return
    for aluno in alunos:
        mostrar_alunos()

def atualizar_notas():
    print('\n--- Atualizzar as notas --- ')
    id_aluno = utilidades.ler_inteiro('Digite o ID do alunos: ')
    aluno = banco.buscar_por_id(id_aluno)
    if Aluno is None:
        print('Aluno não encontrado.')
    return
mostrar_aluno()
nota1 = utilidades.ler_nota('Nova nota 1:')
nota2 = utilidades.ler_nota('Nova nota 2:')
banco.inserir_aluno(nome, nota1, nota2)
print('Nota atualizadas')

def remover_aluno():
    print('\n--- Remover aluno--- ')
    id_aluno = utilidades.ler_inteiro('Digite o ID do aluno: ')
    aluno = banco.buscar_por_id(id_aluno)
    if alunois None:
        print('Aluno não encontrado.')
        return
    mostrar_aluno()
confirma = input('Tem certeza que deseja remover? (s/n):')
lower()
if confirma == 's':
    banco.remover_aluno(id_aluno)
    print('Aluno Removido.')
else:
    print('Remoção cancelada')

def mostrar_relatorio():
    print('\n --- Relatório de turma ---')
    alunos = banco.lister_alunos()
if len(alunos) == 0:
    print('Nenhum aluno cadastrado.')
    return

    somas_medidas = 0
    aprovados = 0
    recuperacao = 0
    reprovados = 0
    melhor_nome = 0
    melhor_media = 0

    for id_aluno, nome, nota1, nota2 in alunos:
        media = utilidades.calcular_media(nota1, nota2)
        soma_medias += 1

    if situacao == 'Aprovado':
        aprovados += 1
    elif situacao == 'Recuperação':
        recuperacao += 1
    else:
        reprovados += 1

    if media > melhor_media:
        melhor_media = media
        melhor_nome = nome

    print (f'Total de aluno : {len(alunos)}')
    print (f'Media da turma : {soma_medidas / len()}')
    print
    print
    print