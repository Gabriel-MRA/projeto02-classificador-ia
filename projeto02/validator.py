import json
import re

CATEGORIAS_PERMITIDAS = ["Suporte", "Vendas", "Financeiro", "Geral"]


def extrair_json_bruto(texto: str) -> str:
    match = re.search(r"\{.*?\}", texto, re.DOTALL)
    if not match:
        raise ValueError("Nenhum JSON encontrado na resposta.")
    return match.group()


def parse_json_resposta(resposta: str) -> dict:
    try:
        json_bruto = extrair_json_bruto(resposta)
        return json.loads(json_bruto)
    except json.JSONDecodeError:
        raise ValueError("JSON inválido.")


def validar_categoria(dados: dict) -> str:
    categoria = dados.get("categoria")

    if not categoria:
        raise ValueError("Campo 'categoria' ausente.")

    if categoria not in CATEGORIAS_PERMITIDAS:
        raise ValueError(f"Categoria inválida: {categoria}")

    return categoria


def fallback_seguro() -> dict:
    return {
        "categoria": "Geral",
        "erro": "Fallback acionado"
    }


def validar_resposta(resposta: str) -> dict:
    try:
        dados = parse_json_resposta(resposta)
        categoria = validar_categoria(dados)
        return {"categoria": categoria}
    except Exception as e:
        print(f"[ERRO VALIDAÇÃO] {e}")
        return fallback_seguro()