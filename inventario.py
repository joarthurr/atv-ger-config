class Inventario:
    def __init__(self, dinheiro = 0):
        self.equipamento = []
        self.consumivel = []
        self.dinheiro = dinheiro
        self.item_selecionado = None
  
    def pegar(self, item, tipo):
        if tipo == "equipamento":
            self.equipamento.append(item)
        elif tipo == "consumivel":
            self.consumiveis.append(item)
        print(f"[+] {item} adicionado ao inventário.")

    def selecionar(self, nome_item):
        if nome_item in self.equipamento or nome_item in self.consumivel:
            self.item_selecionado = nome_item
            print(f"[*] Item '{self.item_selecionado}' selecionado.")
        else:
            print(f"[!] Erro: {nome_item} não encontrado.")

    def guardar(self):
        if self.item_selecionado:
            print(f"[-] {self.item_selecionado} foi guardado.")
            self.item_selecionado = None
        else:
            print("[!] Você já está com as mãos vazias.")

    def dropar(self, nome_item):
        removido = False
        
        if nome_item in self.equipamento:
            self.equipamento.remove(nome_item)
            removido = True
        elif nome_item in self.consumiveis:
            self.consumiveis.remove(nome_item)
            removido = True

        if removido:
            if self.item_selecionado == nome_item:
                self.item_selecionado = None
            print(f"[x] {nome_item} foi removido do inventário.")
        else:
            print(f"[!] Você não possui {nome_item} para dropar.")