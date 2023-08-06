def calculador_de_livros(exemplares):
    preco_unitario_livros = 24.95
    
    custo_de_transporte_unidade = 3.00
    
    custo_de_transporte_adicional = 0.75

    custo_total_livros = exemplares * preco_unitario_livros

    custo_transporte_total =  (exemplares - 1) * custo_de_transporte_adicional + custo_de_transporte_unidade

    custo_final_do_pedido = custo_total_livros - (custo_total_livros * 40 / 100) + custo_transporte_total

    print(f'O custo total por seu pedido é de R$ {custo_final_do_pedido:.2f}')
     




calculador_de_livros(60)
