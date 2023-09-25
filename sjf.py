import copy

class SJF:
    """Algoritmo de escalonamento Shortest Job First (SJF)."""

    def run(self, processos, debug=False):
        """
        Executa o algoritmo SJF e retorna os tempos médios de retorno, resposta e espera.
        """

        # Cria uma cópia da lista de processos para não modificar a original.
        procs = copy.deepcopy(processos)

        # Inicialização das variáveis de tempos totais.
        tempo_retorno_total = tempo_resposta_total = tempo_espera_total = 0

        # Define o tempo inicial com base no primeiro processo.
        tempo_inicio = processos[0][0]
        tempo_atual = tempo_inicio
        soma_duracao = 0

        while procs:
            proximo = self._proximo_processo(procs, tempo_atual)

            # Se não houver processo disponível para execução no momento atual.
            if proximo == -1:
                tempo_atual = procs[0][0]
            else:
                if debug:
                    print(f"SJF: Executando processo {procs[proximo]} no tempo {tempo_atual}")
                # Calcula o delta do tempo para o cálculo dos tempos de resposta e espera.
                delta_tempo = soma_duracao - (procs[proximo][0] - tempo_inicio)
                tempo_resposta_total += delta_tempo
                tempo_espera_total += delta_tempo

                # Atualiza a soma das durações e o tempo de retorno total.
                soma_duracao += procs[proximo][1]
                tempo_retorno_total += soma_duracao - (procs[proximo][0] - tempo_inicio)

                # Atualiza o tempo atual com base no processo que está sendo executado.
                tempo_atual += procs[proximo][1]
                procs.pop(proximo)

        # Calcula os tempos médios.
        n_processos = len(processos)
        tempo_retorno_medio = f"{tempo_retorno_total / n_processos:.1f}".replace('.', ',')
        tempo_resposta_medio = f"{tempo_resposta_total / n_processos:.1f}".replace('.', ',')
        tempo_espera_medio = f"{tempo_espera_total / n_processos:.1f}".replace('.', ',')

        return (tempo_retorno_medio, tempo_resposta_medio, tempo_espera_medio)

    def _proximo_processo(self, procs, ta):
        """
        Retorna o índice do próximo processo a ser executado, considerando o tempo atual 'ta'.
        Se nenhum processo estiver disponível, retorna -1.
        """

        menor_duracao = None
        index_melhor = -1

        for index, p in enumerate(procs):
            if p[0] <= ta: 
                if menor_duracao is None or p[1] < menor_duracao or (p[1] == menor_duracao and p[0] < procs[index_melhor][0]):
                    menor_duracao = p[1]
                    index_melhor = index

        return index_melhor
