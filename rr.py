import copy

class RR:
    """Algoritmo de escalonamento Round Robin (RR)."""

    def run(self, processos, quantum, debug=False):
        """Executa o algoritmo RR com a duração do quantum especificada."""

        procs = list(map(list, copy.deepcopy(processos)))
        tempo_retorno_total = tempo_resposta_total = tempo_espera_total = 0
        tempo_inicio = processos[0][0]
        tempo_atual = tempo_inicio

        while procs:
            # Seleciona o próximo processo baseado no instante de chegada.
            while not (procs[0][0] <= tempo_atual or procs[0][0] == tempo_inicio):
                procs.append(procs.pop(0))

            # Marca primeira execução e acumula tempo de resposta.
            if -1 not in procs[0]:
                procs[0].append(-1)
                tempo_resposta_total += tempo_atual - procs[0][0]

            exec_time = min(quantum, procs[0][1])
            procs[0][1] -= exec_time
            tempo_atual += exec_time

             # Debug: Imprime a execução do processo.
            if debug:
                print(f"Executando processo {procs[0]} por {exec_time} unidades de tempo. Tempo atual: {tempo_atual}")

            # Atualiza o tempo de espera.
            for index, proc in enumerate(procs[1:], start=1):  # Começa do segundo processo
                if proc[0] < tempo_atual:
                    tempo_espera_total += exec_time

            if procs[0][1] == 0:  # Se o processo terminou
                tempo_retorno_total += tempo_atual - procs[0][0]
                procs.pop(0)
            else:
                procs.append(procs.pop(0))

        num_processos = len(processos)
        tempo_retorno_medio = f"{tempo_retorno_total / num_processos:.1f}".replace('.', ',')
        tempo_resposta_medio = f"{tempo_resposta_total / num_processos:.1f}".replace('.', ',')
        tempo_espera_medio = f"{tempo_espera_total / num_processos:.1f}".replace('.', ',')

        return (tempo_retorno_medio, tempo_resposta_medio, tempo_espera_medio)
