from personagem import Personagem, Guerreiro, Mago
from inventario import Inventario

class Main:
    def __init__(self):
        self.executar()
    
    def executar(self):
        """Método principal que demonstra o uso das classes"""
        
        print("=" * 60)
        print("DEMONSTRAÇÃO: PERSONAGENS E INVENTÁRIO")
        print("=" * 60)
        
        # Criando personagens
        print("\n[CRIANDO PERSONAGENS]")
        guerreiro = Guerreiro("Conan", 100, 25)
        mago = Mago("Merlin", 80, 50)
        
        print(f"✓ Guerreiro criado: {guerreiro.nome} (Vida: {guerreiro.vida}, Força: {guerreiro.forca})")
        print(f"✓ Mago criado: {mago.nome} (Vida: {mago.vida}, Mana: {mago.mana})")
        
        # Demonstrando ataques
        print("\n[ATAQUES DOS PERSONAGENS]")
        guerreiro.atacar()
        mago.atacar()
        mago.atacar()
        
        # Demonstrando recebimento de dano
        print("\n[RECEBIMENTO DE DANO]")
        guerreiro.receber_dano(15)
        mago.receber_dano(30)
        
        # Criando inventário
        print("\n[CRIANDO INVENTÁRIO]")
        inventario_conan = Inventario(dinheiro=100)
        print(f"✓ Inventário criado para {guerreiro.nome}")
        print(f"  Dinheiro inicial: {inventario_conan.dinheiro} ouro")
        
        # Demonstrando métodos do inventário
        print("\n[GERENCIANDO INVENTÁRIO]")
        
        # Pegando itens
        inventario_conan.pegar("Espada de Aço", "equipamento")
        inventario_conan.pegar("Escudo de Ouro", "equipamento")
        inventario_conan.pegar("Poção de Vida", "consumivel")
        
        # Selecionando item
        inventario_conan.selecionar("Espada de Aço")
        
        # Guardando item
        inventario_conan.guardar()
        
        # Dropando item
        inventario_conan.dropar("Poção de Vida")
        
        # Tentando selecionar item que não existe
        inventario_conan.selecionar("Mapa do Tesouro")
        
        # Resumo final
        print("\n" + "=" * 60)
        print("RESUMO FINAL")
        print("=" * 60)
        print(f"{guerreiro.nome} - Vida: {guerreiro.vida} | Força: {guerreiro.forca}")
        print(f"{mago.nome} - Vida: {mago.vida} | Mana: {mago.mana}")
        print(f"\nInventário de {guerreiro.nome}:")
        print(f"  Equipamentos: {inventario_conan.equipamento}")
        print(f"  Consumíveis: {inventario_conan.consumivel}")
        print(f"  Dinheiro: {inventario_conan.dinheiro} ouro")
        print("=" * 60)

# Executando a aplicação
if __name__ == "__main__":
    main = Main()