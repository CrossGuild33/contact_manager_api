from sql_alchemy import banco

class ClienteModel(banco.Model):
    __tablename__ = 'clientes'

    cliente_id = banco.Column(banco.String, primary_key=True)
    nome = banco.Column(banco.String(80))
    endereco = banco.Column(banco.String(300))
    gostos = banco.Column(banco.String(80))

    def __init__(self, cliente_id, nome, endereco, gostos):
        self.cliente_id = cliente_id
        self.nome = nome
        self.endereco = endereco
        self.gostos = gostos

    # converte os dados para json
    def json(self):
        return {
            'cliente_id': self.cliente_id,
            'nome': self.nome,
            'endereco': self.endereco,
            'gostos': self.gostos
        }    

    @classmethod
    def find_cliente(cls, cliente_id):
        cliente = cls.query.filter_by(cliente_id=cliente_id).first()
        if cliente:
            return cliente
        return None;    

    @classmethod
    def delete_by_id(cls, cliente_id):
        # Faz a consulta do cliente pelo id
        cliente = cls.query.filter_by(cliente_id=cliente_id).first()

        if cliente:
            # Deleta o cliente no banco de dados
            banco.session.delete(cliente)
            banco.session.commit()
            return True
        
        return False     