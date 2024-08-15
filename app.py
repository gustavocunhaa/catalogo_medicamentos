import json
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
def find_info(id: int):
    lista_atributos = ["produto", "principio_ativo", "tipo",
                       "fabricante", "especialidade", 
                       "classe_terapeutica", "categoria"]
    data = json.dumps({"lista_ids": [int(id)],
                       "atributos": lista_atributos
                       })
    url = f"{BASE_URL}/infocollect/"
    response = make_request(url, data)
    return response

# -------------------------
# Pages render

st.markdown("### Busque o produto")

id_medicamento = st.number_input(label="Id do medicamento", step=1, min_value=1)
info_produto_selecionado = json.loads(find_info(id_medicamento).text)
st.json(info_produto_selecionado)
