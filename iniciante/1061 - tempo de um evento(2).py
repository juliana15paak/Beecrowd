_, diainicial = input().split('Dia ')
diainicial = int(diainicial)
h_inicial, m_inicial, s_inicial = map(int, input().split(' : '))

_, diafinal = input().split('Dia ')
diafinal = int(diafinal)
h_final, m_final, s_final = map(int, input().split(' : '))

diainicial = diainicial * 24 * 60 * 60
h_inicial = h_inicial * 60 * 60
m_inicial = m_inicial * 60
tempoinicial = diainicial + h_inicial + m_inicial + s_inicial

diafinal = diafinal * 24 * 60 * 60
h_final = h_final * 60 * 60
m_final = m_final * 60
tempofinal = diafinal + h_final + m_final + s_final

tempo_decorrido = tempofinal - tempoinicial
qtd_dia = tempo_decorrido // (24 * 60 * 60)
tempo_decorrido = tempo_decorrido % (24 * 60 * 60)

qtd_hora = tempo_decorrido // (60 * 60)
tempo_decorrido = tempo_decorrido % (60 * 60)

qtd_minuto = tempo_decorrido // 60
tempo_decorrido = tempo_decorrido % 60

qtd_segundo = tempo_decorrido // 1


print(f'{qtd_dia} dia(s)')
print(f'{qtd_hora} hora(s)')
print(f'{qtd_minuto} minuto(s)')
print(f'{qtd_segundo} segundo(s)')
