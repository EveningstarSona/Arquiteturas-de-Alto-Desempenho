'''
[1001537] Arquiteturas de Alto Desempenho

Atividade Prática 01 (Produto final com testes subsequentes)

Sona Eveningstar Jorge Candeu, 769802
Carlos André Costa Santana, 773370

06/06/2022
'''

from pratica01_asynchronous import main as asy_main
from pratica01_synchronous import main as sy_main

DOTS_LIST = [1000, 10000, 50000, 100000]
speedups = []
asy_errors = []
sy_errors = []

if __name__ == '__main__':
    for DOTS in DOTS_LIST:
        asy_time, asy_err = asy_main(DOTS)
        sy_time, sy_err = sy_main(DOTS)
        print('Speedup:', sy_time/asy_time, end='\n\n\n')
        speedups.append(sy_time/asy_time)
        asy_errors.append(asy_err)
        sy_errors.append(sy_err)
    for d, s, aerr, serr in zip(DOTS_LIST, speedups, asy_errors, sy_errors):
        print(f'{d} pontos, {s} speedup.\nErro assíncrono: {aerr}, erro síncrono: {serr}')