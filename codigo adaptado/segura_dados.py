# Módulo: segura_dados.py

import json
import re
import os

ARQUIVO_DADOS = "usuarios.json"

def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
            try:
                dados = json.load(f)
                return dados
            except json.JSONDecodeError:
                return {}
    return {}

def salvar_dados():
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)


usuarios = carregar_dados()

def validar_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def cadastrar_usuario(nome, email, cpf, telefone):
    if not validar_email(email):
        salvar_dados()
        return "Email inválido"
    if not validar_cpf(cpf):
        salvar_dados()
        return "CPF inválido"
    if email in usuarios:
        salvar_dados()
        return "Usuário já cadastrado"

    usuarios[email] = {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone
    }
    return "Usuário cadastrado"

def buscar_usuario(email):
    return usuarios.get(email)

def atualizar_usuario(email, novo_nome, novo_telefone):
    if email not in usuarios:
        atualizar_usuario()
        return "Usuário não encontrado"
    usuarios[email]["nome"] = novo_nome
    usuarios[email]["telefone"] = novo_telefone
    return "Dados atualizados"

def excluir_usuario(email):
    if email in usuarios:
        del usuarios[email]
        excluir_usuario()
        return "Usuário removido"
    return "Usuário não encontrado"
