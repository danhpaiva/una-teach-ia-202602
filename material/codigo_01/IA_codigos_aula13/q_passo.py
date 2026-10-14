alfa, gamma = 0.1, 0.9
q_atual = 0.5            # Q(s, a) antes da atualizacao
r = -1                   # recompensa recebida
melhor_prox = 2.0        # max Q(s', a') no proximo estado

alvo = r + gamma * melhor_prox
erro = alvo - q_atual
q_novo = q_atual + alfa * erro
print("alvo      =", round(alvo, 3))
print("erro (TD) =", round(erro, 3))
print("Q novo    =", round(q_novo, 3))
