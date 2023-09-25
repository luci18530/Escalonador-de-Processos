class FCFS:
    #First Come, First Served (FCFS)

    def run(self, processos, debug=False):

        tempo_retorno = tempo_resposta = tempo_espera = 0

        # Define o tempo inicial com base no primeiro processo.
        tempo_inicio = processos[0][0]
        soma_duracao = 0

        for n, processo in enumerate(processos):
            # Primeiro processo tem tempo de resposta/espera igual a zero
            if n != 0:
                delta_tempo = soma_duracao - (processo[0] - tempo_inicio)
                tempo_resposta += delta_tempo
                tempo_espera += delta_tempo

            # Atualiza a soma das durações e o tempo de retorno.
            soma_duracao += processo[1]
            tempo_retorno += soma_duracao - (processo[0] - tempo_inicio)

            if debug:
                print(f"FCFS: Executando processo {n+1} com chegada em {processo[0]} e duração de {processo[1]}")
                print(f"Tempo atual: {soma_duracao}")    
                print("-"*50) 

        n_processos = len(processos)
        tempo_retorno_medio = f"{tempo_retorno / n_processos:.1f}".replace('.', ',')
        tempo_resposta_medio = f"{tempo_resposta / n_processos:.1f}".replace('.', ',')
        tempo_espera_medio = f"{tempo_espera / n_processos:.1f}".replace('.', ',')

        return (tempo_retorno_medio, tempo_resposta_medio, tempo_espera_medio)