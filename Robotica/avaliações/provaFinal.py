import requests
import sqlite3
import re

POKEMONS_ALVO = [
    "volcarona",
    "metagross",
    "garchomp",
    "amoonguss",
    "zoroark-hisui",
    "azumarill"
]

DATABASE_NAME = "projeto_rpa.db"

def validar_nome_pokemon(nome):
    padrao = r'^[a-z0-9\-]+$'
    return re.match(padrao, nome) is not None

def coletar_dados_pokemon(pokemon_names):
    todos_dados = []
    for nome in pokemon_names:
        if not validar_nome_pokemon(nome):
            print(f"Nome inválido ignorado: {nome}")
            continue
        url = f"https://pokeapi.co/api/v2/pokemon/{nome.lower()}/"
        try:
            resposta = requests.get(url)
            resposta.raise_for_status()
            dados = resposta.json()
            info = {
                "nome": dados["name"].capitalize(),
                "id": dados["id"],
                "tipos": ", ".join(t["type"]["name"].capitalize() for t in dados["types"]),
                "habilidades": ", ".join(a["ability"]["name"].replace("-", " ").title() for a in dados["abilities"]),
                "hp": next(s["base_stat"] for s in dados["stats"] if s["stat"]["name"] == "hp"),
                "ataque": next(s["base_stat"] for s in dados["stats"] if s["stat"]["name"] == "attack"),
                "defesa": next(s["base_stat"] for s in dados["stats"] if s["stat"]["name"] == "defense"),
                "sp_ataque": next(s["base_stat"] for s in dados["stats"] if s["stat"]["name"] == "special-attack"),
                "sp_defesa": next(s["base_stat"] for s in dados["stats"] if s["stat"]["name"] == "special-defense"),
                "velocidade": next(s["base_stat"] for s in dados["stats"] if s["stat"]["name"] == "speed"),
            }
            todos_dados.append(info)
            print(f"Dados de {info['nome']} coletados.")
        except Exception as e:
            print(f"Erro ao coletar {nome}: {e}")
    return todos_dados

def configurar_banco():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pokemons_coletados (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            pokeapi_id INTEGER,
            tipos TEXT,
            habilidades TEXT,
            hp INTEGER,
            ataque INTEGER,
            defesa INTEGER,
            sp_ataque INTEGER,
            sp_defesa INTEGER,
            velocidade INTEGER
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS dados_processados (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_pokemon TEXT NOT NULL,
            resumo_tipos_habilidades TEXT,
            status_geral TEXT
        )
    """)
    conn.commit()
    conn.close()

def inserir_dados_banco(pokemon_data):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    for p in pokemon_data:
        cursor.execute("""
            INSERT OR REPLACE INTO pokemons_coletados 
            (nome, pokeapi_id, tipos, habilidades, hp, ataque, defesa, sp_ataque, sp_defesa, velocidade)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (p["nome"], p["id"], p["tipos"], p["habilidades"], p["hp"], p["ataque"], p["defesa"], p["sp_ataque"], p["sp_defesa"], p["velocidade"]))
    conn.commit()
    conn.close()

def processar_dados():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dados_processados")
    cursor.execute("SELECT nome, tipos, habilidades, hp, ataque, defesa FROM pokemons_coletados")
    dados = cursor.fetchall()
    registros_processados = []
    for nome, tipos, habilidades, hp, ataque, defesa in dados:
        resumo = f"Tipos: {tipos}. Habilidades: {habilidades}."
        status = f"HP: {hp}, Atk: {ataque}, Def: {defesa}."
        registros_processados.append((nome, resumo, status))
    cursor.executemany("""
        INSERT INTO dados_processados (nome_pokemon, resumo_tipos_habilidades, status_geral)
        VALUES (?, ?, ?)
    """, registros_processados)
    conn.commit()
    conn.close()
    return registros_processados

def simular_envio_email(dados_processados):
    print("\nSimulação de envio de e-mail iniciada...")
    print(f"De: VictorAlexandre@gmail.com")
    print(f"Para: AlexandreVictor@example.com")
    print(f"Assunto: Relatório de Pokémon Coletados e Processados - Projeto RPA")
    print("\nCorpo do e-mail:")
    for nome, resumo, status in dados_processados:
        print(f"--- {nome} ---")
        print(resumo)
        print(status)
        print()
    print("E-mail simulado como enviado com sucesso.\n")

def imprimir_conteudo_banco():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemons_coletados")
    registros = cursor.fetchall()
    print("\nConteúdo da tabela pokemons_coletados:")
    for registro in registros:
        print(registro)
    conn.close()

def main():
    configurar_banco()
    dados_coletados = coletar_dados_pokemon(POKEMONS_ALVO)
    if not dados_coletados:
        print("Nenhum dado coletado. Finalizando.")
        return
    inserir_dados_banco(dados_coletados)
    dados_processados = processar_dados()
    simular_envio_email(dados_processados)
    imprimir_conteudo_banco()
    print("Processo concluído.")

if __name__ == "__main__":
    main()
