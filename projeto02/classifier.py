from llm_client import gerar_resposta
from validator import validar_resposta

CATEGORIAS = ["Suporte", "Vendas", "Financeiro", "Geral"]


def classificar_mensagem(mensagem, temperature=0.2):
    prompt = f"""
    Classifique a mensagem abaixo em uma das seguintes categorias: {', '.join(CATEGORIAS)}.
    Retorne apenas um JSON no formato:
    {{
        "categoria": "nome_categoria"
    }}

    Mensagem: "{mensagem}"
    """

    resposta = gerar_resposta(prompt, temperature)
    return validar_resposta(resposta)