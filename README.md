# RPG ⚔️​

**Sistema simplificado de rpg que utiliza conceitos e abordagens da estrategia githubflow. As classes são organizadas em branchs para cada alteração especifica.**

📍​ Estrutura de Classes

👤​ **Classe Personagem** 

É o jogador no mundo. Ela armazena os dados e progresso de funcionamento

Dentro da classe personagem contem dois tipos:

🧙‍♂️ Mago 

🛡️​ Guerreiro 

Atributos Principais: Nome, Força, Vida Atual/Máxima e Mana

Métodos principais:

atacar(): Calcula o dano baseado em atributos.

receberDano(quantidade): Reduz a vida e verifica estado de morte.

 📦​ **Classe Inventário** 

A ponte entre o personagem e seus itens. Gerencia o espaço e a organização.

Atributos Principais: Equipamento, dinheiro, item_selecionado e consumivel

Métodos principais: 

Pegar (): Capaz de pegar um item do inventário
Selecionar (): Selecionar um item do inventário
Guardar (): Guardar um item dentro do inventário
Dropar (): Dropar itens do inventário

O item pode ser de vários tipos:

Equipamento

Dinheiro

Consumivel

