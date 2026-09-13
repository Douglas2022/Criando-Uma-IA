import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

# Carrega o .env
load_dotenv()

# Pega a chave da API
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("Chave da OpenAI não encontrada.")
    st.stop()

# Cliente OpenAI
client = OpenAI(api_key=api_key)

# Configuração
st.set_page_config(
    page_title="DougIA",
    page_icon="🤖"
)

st.title("🤖 DougIA")
st.write("Olá! Eu sou a DougIA. Como posso ajudar?")

# Histórico
if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {
            "role": "system",
            "content": "Você é a DougIA, uma assistente útil, amigável e objetiva."
        }
    ]

# Mostrar histórico
for mensagem in st.session_state.mensagens:
    if mensagem["role"] == "system":
        continue

    with st.chat_message(mensagem["role"]):
        st.write(mensagem["content"])

# CAMPO DE DIGITAÇÃO
prompt = st.chat_input("Digite sua mensagem aqui...")

# Quando o usuário enviar uma mensagem
if prompt:

    # Mostra mensagem do usuário
    with st.chat_message("user"):
        st.write(prompt)

    # Salva mensagem
    st.session_state.mensagens.append({
        "role": "user",
        "content": prompt
    })

    # Responde
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):

            resposta = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=st.session_state.mensagens
            )

            texto_resposta = resposta.choices[0].message.content

        st.write(texto_resposta)

    # Salva resposta
    st.session_state.mensagens.append({
        "role": "assistant",
        "content": texto_resposta
    })
