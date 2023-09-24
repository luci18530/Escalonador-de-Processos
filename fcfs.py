class FCFS:
    #First Come, First Served (FCFS)

    def run(self, processos):

        tempo_retorno = 0
        tempo_resposta = 0
        tempo_espera = 0 
        # Armazena o instante de chegada do primeiro processo
        tempo_inicio = processos[0][0]
        # Soma das durações do processos
        soma_duracao = 0

        for n, processo in enumerate(processos):
            # Primeiro processo tem tempo de resposta/espera igual a zero
            if n != 0:
                delta_tempo = soma_duracao - (processo[0] - tempo_inicio)
                tempo_resposta += delta_tempo
                tempo_espera += delta_tempo

            # Soma a duração de cada processo
            soma_duracao += processo[1]

            # Tempo total ate o fim do processo menos a diferenca entre o tempo de
            # chegado do processo atual e o tempo inicial
            tempo_retorno += soma_duracao - (processo[0] - tempo_inicio)



        # converte para string, substitui ponto por virgula, com uma casa decimal
        n_processos = len(processos)
        tempo_retorno_medio = f"{tempo_retorno / n_processos:.1f}".replace('.', ',')
        tempo_resposta_medio = f"{tempo_resposta / n_processos:.1f}".replace('.', ',')
        tempo_espera_medio = f"{tempo_espera / n_processos:.1f}".replace('.', ',')

        # Retorna uma tupla contendo o tempo de retorno medio, o tempo de
        # resposta medio e o tempo de espera medio, respectivamente
        return (tempo_retorno_medio, tempo_resposta_medio, tempo_espera_medio)