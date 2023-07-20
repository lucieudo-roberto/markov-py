## Cadeia de Markov Simples

A Cadeia de Markov Simples é um algoritmo implementado neste projeto que permite gerar palavras aleatórias com base em um conjunto de arquivos de texto fornecidos. Este README fornece uma visão geral do projeto, explica a estrutura dos diretórios e arquivos, bem como as etapas necessárias para executar o algoritmo.

## Visão Geral

A Cadeia de Markov é uma técnica estatística utilizada para modelar sequências de eventos, onde a probabilidade de um evento depende apenas do evento imediatamente anterior. Essa abordagem é comumente aplicada em processamento de linguagem natural para gerar texto com base nas probabilidades de transição entre palavras.

Este projeto implementa uma versão simples da Cadeia de Markov, que utiliza uma abordagem de ordem 1, ou seja, a probabilidade de uma palavra é determinada apenas pela palavra imediatamente anterior. O algoritmo utiliza arquivos de texto fornecidos no diretório `txt_inp` para treinar o modelo, e em seguida, permite que o usuário gere palavras aleatórias com o script `gener_word.py`.

## Estrutura do Diretório

Aqui está a estrutura do diretório deste projeto:

```
markov_1/
├── clean_files.py
├── gener_word.py
├── join_files.py
├── train_model.py
├── txt_inp/
└── txt_out/
```

- `clean_files.py`: Script responsável por limpar os arquivos de texto no diretório `txt_inp`, removendo caracteres especiais, pontuações e convertendo todas as palavras para letras minúsculas.
- `gener_word.py`: Script para gerar palavras aleatórias com base no modelo treinado.
- `join_files.py`: Script para juntar o conteúdo dos arquivos de texto em `txt_inp` em um único arquivo.
- `train_model.py`: Script para treinar o modelo de Cadeia de Markov com base nos arquivos de texto processados.
- `txt_inp/`: Diretório que contém os arquivos de texto de entrada para o treinamento do modelo.
- `txt_out/`: Diretório que conterá o arquivo gerado após a junção dos arquivos de texto.

## Instruções de Uso

Para utilizar o algoritmo de Cadeia de Markov Simples, siga os passos abaixo:

1. Coloque os arquivos de texto que deseja utilizar para o treinamento do modelo no diretório `txt_inp/`.

2. Execute o script `clean_files.py` para limpar os arquivos de texto. Isso garantirá que o modelo leve em consideração apenas o conteúdo relevante para a geração de palavras. Exemplo de uso:

   ```
   python clean_files.py
   ```

3. Em seguida, execute o script `join_files.py` para combinar o conteúdo dos arquivos de texto em um único arquivo. Isso permitirá que o modelo tenha uma visão mais abrangente das palavras presentes no conjunto de dados. Exemplo de uso:

   ```
   python join_files.py
   ```

4. Agora, o modelo está pronto para ser treinado. Execute o script `train_model.py` para construir o modelo de Cadeia de Markov com base nos dados processados. Exemplo de uso:

   ```
   python train_model.py
   ```

5. Após o treinamento do modelo, você pode gerar palavras aleatórias utilizando o script `gener_word.py`. Forneça uma palavra inicial e a quantidade de palavras que deseja gerar. Exemplo de uso:

   ```
   python gener_word.py 'word' quantidade randomic S/N
   ```

   - `'word'`: Palavra inicial para iniciar a geração.
   - `quantidade`: Número de palavras a serem geradas após a palavra inicial.
   - `randomic`: Opção para escolher se as palavras geradas serão aleatórias (S) ou seguirão a sequência mais provável (N).

6. Divirta-se explorando a geração de palavras com base no modelo de Cadeia de Markov Simples!

## Considerações Finais

Este projeto implementa uma versão básica da Cadeia de Markov e, portanto, pode apresentar algumas limitações em termos de precisão na geração de palavras. Sinta-se à vontade para aprimorar o código, adicionar mais funcionalidades ou utilizar uma ordem maior da Cadeia de Markov para obter resultados mais refinados.

Caso tenha alguma dúvida ou sugestão de melhoria, sinta-se à vontade para contribuir para o projeto ou entrar em contato.
