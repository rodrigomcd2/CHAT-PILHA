class BatePapo:
    def __init__(self):
        self.mensagens = []  # Pilha de mensagens
        self.mensagens_apagadas = []  # Pilha de mensagens apagadas
    
    def enviar_mensagem(self, mensagem):
        """Envia uma mensagem, empilhando-a no histórico."""
        self.mensagens.append(mensagem)
        print(f"Mensagem enviada: {mensagem}")
    
    def apagar_mensagem(self):
        """Apaga a última mensagem enviada (desempilhando) e mostra as mensagens com a informação de apagamento."""
        if self.mensagens:
            apagada = self.mensagens.pop()
            self.mensagens_apagadas.append(apagada)
            print("\nMensagens no chat:")
            for i, msg in enumerate(self.mensagens, 1):
                print(f"{i}: {msg}")
            print("\nMensagem apagada")
        else:
            print("Não há mensagens para apagar.")
    
    def desfazer_apagar(self):
        """Desfaz a exclusão da última mensagem apagada, restaurando-a."""
        if self.mensagens_apagadas:
            restaurada = self.mensagens_apagadas.pop()
            self.mensagens.append(restaurada)
            print(f"Mensagem restaurada: {restaurada}")
        else:
            print("Não há mensagens apagadas para restaurar.")
    
    def mostrar_mensagens(self):
        """Mostra todas as mensagens atuais no chat."""
        print("\nMensagens no chat:")
        if self.mensagens:
            for i, msg in enumerate(self.mensagens, 1):
                print(f"{i}: {msg}")
        else:
            print("Sem mensagens no chat.")

# Simulando o bate-papo
chat = BatePapo()

# Enviando mensagens
chat.enviar_mensagem("Oi, tudo bem?")
chat.enviar_mensagem("Como você está?")
chat.enviar_mensagem("Hoje está um ótimo dia!")

# Mostrando as mensagens enviadas
chat.mostrar_mensagens()

# Apagando a última mensagem
chat.apagar_mensagem()

# Mostrando as mensagens após apagar uma
chat.mostrar_mensagens()

# Desfazendo o apagar (restaurando a última mensagem apagada)
chat.desfazer_apagar()

# Mostrando as mensagens após desfazer o apagar
chat.mostrar_mensagens()
