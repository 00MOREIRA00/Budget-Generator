# Gerador de Orçamento
A ideia desse pequeno projeto é simples. Digamos que em um cenario onde ha um desenvolvedor que tenha uma grande demanda de produção de orçamentos para futuros projetos ele tenha o trabalho de abrir editor de texto para fazer toda alimentação de informações e gerar o PDF.

Com está aplicação o desenvolvedor somente ira preencher todo questionaro que seria:

    * Descrição do Projeto
    * Quantidades de horas estimadas de desenvolvimento
    * Valor cobrado por hora
    * Prazo de entrega 
    * Valor total cobrado


Após o preenchimento recebera um Pdf personalizado com toda informação.

------------------------------------------------------------
### Implementações 
1. Basicamente a aplicação recebe as informações através de inputs e os armazena em variaveis.
2. Fazemos download de um conjuntos de dados para utilização de PDFs através do 'fpdf'
    ```
        pip install fpdf
    ```
3. Utilizamos os códigos disponibilizados através do download desse anexo para gerar o PDF através de um layout disponibilizado e informado nos códigos. De modo que as informações são somente inseridas nesse layut e disponibilizado.







