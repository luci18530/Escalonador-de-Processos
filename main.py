from fcfs import FCFS
from sjf import SJF
from rr import RR

# Converte a entrada para uma lista de tuplas
def converte_entrada(entrada):
    return tuple(map(int, entrada.strip().split()))

def main():
    with open('entrada.txt', 'r') as file:
        processos = [converte_entrada(line) for line in file.readlines()] 
    
    fcfs = FCFS()
    sjf = SJF()
    rr = RR()

    fcfs_result = fcfs.run(processos, debug=True)
    sjf_result = sjf.run(processos, debug=True)
    rr_result = rr.run(processos, 2, debug=True)

    # Formata as saidas e imprime
    saida_fcfs = f"FCFS {fcfs_result[0]} {fcfs_result[1]} {fcfs_result[2]}"
    saida_sjf = f"SJF {sjf_result[0]} {sjf_result[1]} {sjf_result[2]}"
    saida_rr = f"RR {rr_result[0]} {rr_result[1]} {rr_result[2]}"
    saida = f"{saida_fcfs}\n{saida_sjf}\n{saida_rr}"
    print(saida)

if __name__ == '__main__':
    main()