import json
import ast
import requests as r
import streamlit as st


# -------------------------
# Painel configs
st.set_page_config(layout= 'wide')

page_title = "🛒 Catálogo de produtos"
st.markdown(f"# {page_title}")

autor_html = """
<div style="display: inline_block"><br>
  <a href="https://github.com/gustavocunhaa">
    <img align="center" alt="github" height="30" width="30" src="https://static.macupdate.com/products/39062/l/github-desktop-logo.png">
  <a href="https://www.linkedin.com/in/gustavo-cunha-312a80157/">
    <img align="center" alt="linkedin" height="30" width="30" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg">
  </a>
</div>
"""
st.html(f"{autor_html}")

# -------------------------
# API Consume methods

BASE_URL = f"http://127.0.0.1:8000" # Local instance run

@st.cache_data
def make_request(url, input):
    headers = {"Content-Type": "application/json"}
    response = r.post(url=url, headers=headers, data=input)
    return response

@st.cache_data
def find_product(busca: str):
    data = json.dumps({"busca": busca})
    url = f"{BASE_URL}/product/find/"
    response = make_request(url, data).text
    return response
    

@st.cache_data
def create_vector(text: str):
    data = json.dumps({"texto": text})
    url = f"{BASE_URL}/makevector/"
    response = make_request(url, data).text
    return response


@st.cache_data
def distance_vector(vector_info: str):
    url = f"{BASE_URL}/recommendation/find/"
    data = json.dumps({"vetor": vector_info})
    response = make_request(url, data).text
    return response


@st.cache_data
def rule_find(id: int):
    url = f"{BASE_URL}/recommendation/rule/"
    data = json.dumps({"medicamento_id": id})
    response = make_request(url, data).text
    return response


@st.cache_data
def find_info(id: list):
    if type(id) == list:
       lista = id
    else:
       lista = ast.literal_eval(id)
    lista_atributos = ["produto", "principio_ativo", "tipo",
                       "fabricante", "especialidade", 
                       "classe_terapeutica", "categoria",
                       "codigo_barras", "tipo_receita"]
    data = json.dumps({"lista_ids": lista,
                       "atributos": lista_atributos
                       })
    url = f"{BASE_URL}/product/info/"
    response = make_request(url, data).text
    return response


# -------------------------
# Pages render

st.markdown("### Busque o produto")

busca = st.text_input(label="O que você precisa?")
if busca:
  produto = json.loads(find_product(busca))

  vectorRecommendation, ruleRecommendation, clusterRecommendation = st.columns([2,2,2])
  
  with vectorRecommendation:
    vetor_busca = json.loads(create_vector(produto['descricao']))
    lista_ids = distance_vector(vetor_busca)
    info_produto_selecionado = json.loads(find_info(lista_ids))
    st.write("Resultados da sua busca:")
    st.json(info_produto_selecionado)

  
  with ruleRecommendation:
    id_busca = int(produto['medicamento_id'])
    ids = json.loads(rule_find(id_busca))
    info_produto_selecionado = json.loads(find_info(ids))
    st.write("Você também pode optar por:")
    st.json(info_produto_selecionado)
  

  with clusterRecommendation:
    st.write("Produtos que você pode gostar:")