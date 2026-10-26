# ==========================================
# CALCULADORA SIMPLES EM PYTHON (TERMINAL)
# ==========================================
# Este programa pede dois números e uma operação,
# calcula o resultado e mostra na tela.
# Para rodar: python calculadora.py


def somar(a, b):
    '''Soma dois números.'''
    return a + b


def subtrair(a, b):
    '''Subtrai o segundo número do primeiro.'''
    return a - b


def multiplicar(a, b):
    '''Multiplica dois números.'''
    return a * b


def dividir(a, b):
    '''Divide o primeiro número pelo segundo.'''
    # Não existe divisão por zero, então avisamos o usuário.
    if b == 0:
        return 'Erro: não é possível dividir por zero!'
    return a / b


def ler_numero(mensagem):
    '''Pede um número ao usuário e repete até ele digitar um valor válido.'''
    while True:
        texto = input(mensagem)
        # Aceita vírgula como separador decimal (ex: 2,5)
        texto = texto.replace(',', '.')
        try:
            return float(texto)
        except ValueError:
            print('Valor inválido! Digite apenas números.')


def mostrar_menu():
    '''Mostra as opções disponíveis.'''
    print('\n===== CALCULADORA =====')
    print('1 - Somar (+)')
    print('2 - Subtrair (-)')
    print('3 - Multiplicar (*)')
    print('4 - Dividir (/)')
    print('0 - Sair')
    print('=======================')


def main():
    '''Função principal: controla o fluxo do programa.'''
    print('Bem-vindo à Calculadora!')

    # O while True repete o programa até o usuário escolher sair.
    while True:
        mostrar_menu()
        opcao = input('Escolha uma opção: ')

        if opcao == '0':
            print('Encerrando a calculadora. Até mais!')
            break

        if opcao not in ['1', '2', '3', '4']:
            print('Opção inválida! Escolha um número do menu.')
            continue

        # Pede os dois números
        numero1 = ler_numero('Digite o primeiro número: ')
        numero2 = ler_numero('Digite o segundo número: ')

        # Executa a operação escolhida
        if opcao == '1':
            resultado = somar(numero1, numero2)
        elif opcao == '2':
            resultado = subtrair(numero1, numero2)
        elif opcao == '3':
            resultado = multiplicar(numero1, numero2)
        else:
            resultado = dividir(numero1, numero2)

        print(f'\nResultado: {resultado}')


# Esta linha garante que o programa só roda quando
# executamos este arquivo diretamente.
if __name__ == '__main__':
    main()