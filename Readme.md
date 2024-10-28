# Sobre:
O pintargrade.py é um programa de organização simples que eu criei apenas para revisar a linguagem python, porém, talvez ele possa ser útil em outros contextos.

Este programa foi feito com base na grade do curso de Engenharia da computação (porém pode ser alterado para fazer a mesma coisa em qualquer outro contexto), e serve para organizar quais são as matérias feitas, as que faltam fazer e as principais, marcando elas com bolinhas das cores verde, azul ou vermelha, ele basicamente edita a imagem base adicionando as marcações, porém sem perda de qualidade na imagem.

# Como usar:
- Para usar o programa, você deve ter em mente que as matérias são divididas em 3 listas, uma lista pra cada cor, qualquer matéria pode ter qualquer cor que o usuário quiser, basta apenas colocar ela na lista correspondente. 

### Usando a opção de salvar: 
Quando o usuário terminar de adicionar as matérias nas listas correspondentes, o programa irá perguntar se o usuário deseja salvar as alterações, se ele optar por salvar elas, as informações serão gravadas no HD, em um arquivo txt, caso ele não salve, ele irá conseguir gerar a imagem como pediu, porém depois de gerar a imagem, toda a informação será perdida, porém caso ele não tenha apertado em salvar e queira que as informações fiquem gravadas, ele pode usar a opção "salvar", no menu principal, Ao terminar de organizar tudo, digite "gerar" ou [6] para gerar a imagem, que irá aparecer no mesmo diretório, com o nome de: grade_pintada.jpg.

# Especificações técnicas:
obs: esse programa foi feito com o python3 e usa a biblioteca PIL e OS, e utiliza alguns comando s, caso queira usar no windows, altere a string ```'clear'``` passada como argumento para a biblioteca os.system para a string `'cls'`
