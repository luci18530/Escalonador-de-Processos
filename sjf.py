import copy

class SJF:
    """Algoritmo de escalonamento Smallest Job First (SJF)"""

    def run(self, processos):
        """
        Executa o algoritmo. Recebe como parametros a lista de processos a
        serem executados.
        """

        # Cria uma copia da lista de processos
        procs = copy.deepcopy(processos)
        tempo_retorno_total = tempo_resposta_total = tempo_espera_total = 0

        # Armazena o instante de chegada do primeiro processo
        tempo_inicio = processos[0][0]

        # Inicializa o tempo atual com o instante de chegada do primeiro processo
        tempo_atual = tempo_inicio

        # Armazena a soma das durações do processos
        soma_duracao = 0

        while procs:
            proximo = self._proximo_processo(procs, tempo_atual)

            if proximo == -1: # ocorrencia de vacuo. nao ha processo com tempo de chegada <= ao tempo atual
                tempo_atual = procs[0] # atualiza o tempo atual para o tempo de chegada do proximo processo na lista
            else:
                delta_tempo = soma_duracao - (procs[proximo][0] - tempo_inicio)
                tempo_resposta_total += delta_tempo
                tempo_espera_total += delta_tempo

                # Acumula a duracao de cada processo
                soma_duracao += procs[proximo][1]

                # Tempo total ate o fim do processo menos a diferenca entre o tempo de
                # chegado do processo atual e o tempo inicial
                tempo_retorno_total += soma_duracao - (procs[proximo][0] - tempo_inicio)

                # adiciona a duracao do processo escolhido, atualizando o tempo atual
                tempo_atual = tempo_atual + procs[proximo][1]
                procs.pop(proximo)

        n_processos = len(processos)
        tempo_retorno_medio = f"{tempo_retorno_total / n_processos:.1f}".replace('.', ',')
        tempo_resposta_medio = f"{tempo_resposta_total / n_processos:.1f}".replace('.', ',')
        tempo_espera_medio = f"{tempo_espera_total / n_processos:.1f}".replace('.', ',')

        return (tempo_retorno_medio, tempo_resposta_medio, tempo_espera_medio)


    # Metodo que busca o proximo processo a ser executado
    def _proximo_processo(self, procs, ta):
        """Retorna o índice do próximo processo a ser executado."""
        
        menor_duracao = None
        index_melhor = -1

        for index, p in enumerate(procs):
            if p[0] <= ta: 
                if menor_duracao is None or p[1] < menor_duracao or (p[1] == menor_duracao and p[0] < procs[index_melhor][0]):
                    menor_duracao = p[1]
                    index_melhor = index

        return index_melhor