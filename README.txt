# Rede Neural sem Biblioteca Externa

Esse projeto é uma rede neural simples feita do zero em Python, sem uso de bibliotecas externas. A ideia veio de algo que vi na internet e achei interessante justamente por ser um desafio que mistura lógica, programação e inteligência artificial, mesmo começando praticamente sem saber nada sobre o assunto. Decidi fazer exatamente por isso, pra aprender na prática.

Com ajuda do ChatGPT para entender melhor os conceitos e organizar o raciocínio, fui construindo tudo passo a passo, mas sempre tentando entender o porquê de cada coisa e não só copiar código. A ideia do projeto é evoluir com o tempo conforme eu for aprendendo mais.

Até agora implementei três partes principais: o neurônio, a função sigmoid e o treinamento.

Primeiro criei uma função para simular um neurônio artificial. Nela eu uso inputs (que seriam as entradas), pesos (que representam a importância de cada entrada) e o bias (que funciona como um ajuste fino no resultado). Dentro da função eu percorro os inputs com um loop, multiplico cada um pelo seu peso e somo tudo, depois adiciono o bias. Esse valor final é passado pela função sigmoid.

A função sigmoid eu implementei manualmente pra entender como funciona. Ela pega qualquer número e transforma em um valor entre 0 e 1. Isso ajuda a interpretar a saída como um nível de confiança, por exemplo: 0.8 seria algo que o neurônio “acha que é sim”, enquanto 0.2 seria “acha que não”. Isso me ajudou bastante a entender como uma decisão pode ser representada numericamente.

Depois disso implementei o treinamento, que é a parte mais importante. Criei uma função que calcula o resultado do neurônio, compara com o valor esperado e calcula o erro. Com base nesse erro, o código ajusta os pesos. Esse ajuste leva em conta o erro, o input e uma taxa de aprendizado, que serve pra evitar mudanças muito bruscas. Assim, em vez de acertar de uma vez, o neurônio vai melhorando aos poucos a cada repetição.

Rodando esse processo várias vezes, dá pra ver claramente o resultado ficando cada vez mais próximo do esperado, o que foi uma das partes mais interessantes de ver funcionando na prática.

Com esse projeto eu aprendi na prática como funciona a base de uma rede neural, o papel de cada parte (inputs, pesos, bias), como a sigmoid influencia a saída e principalmente como o erro é usado para fazer o modelo “aprender”. Além disso, melhorei bastante minha lógica de programação e minha forma de pensar na construção de código.

Como próximos passos, pretendo expandir isso criando mais neurônios, trabalhar com múltiplos exemplos (dataset) e melhorar a estrutura do código conforme eu for evoluindo.

Esse projeto não tem como objetivo ser algo pronto pra produção, e sim entender de verdade o que acontece por trás das bibliotecas.