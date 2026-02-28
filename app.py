# Arquivo Principal do Servidor. É nele que você escreve as regras de como o seu sistema web deve se comportar quando alguém tenta acessá-lo.

#  Importa a classe Flask (o motor do site) e a função jsonify (para converter listas/dicionários em JSON)
from flask import Flask, jsonify

# Cria a instância do aplicativo. O '__name__' ajuda o Flask a localizar arquivos de configuração.
app = Flask(__name__)

# Simulação de um banco de dados: uma lista de dicionários armazenada na memória RAM enquanto o servidor rodar.
estoque = [
    {"id": 1, "nome": "Piso Cerâmico 60x60", "quantidade": 50, "m2_por_caixa": 1.44},
    {"id": 2, "nome": "Argamassa ACIII", "quantidade": 100, "m2_por_caixa": 1.0}
]

# Define a rota principal (home). Quando você acessar http://127.0.0.1:5000/, essa função será executada.
@app.route('/')
def home():
    # Retorna um texto simples para o navegador confirmar que o servidor está "vivo".
    return "Sistema de Estoque Limeira - API Ativa!"

# Define a rota '/estoque'. O método 'GET' indica que estamos apenas buscando informações.
@app.route('/estoque', methods=['GET'])
def listar_estoque():
    # Pega a lista 'estoque' e a transforma em um formato JSON (padrão de comunicação de sistemas web).
    return jsonify(estoque)

# Verifica se este arquivo está sendo executado diretamente (e não importado por outro).
if __name__ == '__main__':
    # Inicia o servidor. O 'debug=True' faz o servidor reiniciar sozinho sempre que você salvar uma alteração.
    app.run(debug=True)