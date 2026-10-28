# titulo
# input do chat
# a cada mensagem enviada:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # aparece na tela a resposta da IA

# pip install streamlit openai

import streamlit as st 
from openai import OpenAI 

modelo_ia = OpenAI(api_key="",
                   base_url="https://generativelanguage.googleapis.com/v1beta/openai")

st.write("# ChatBot Renata")

# criar o historico de mensagens
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")
# print(mensagem_usuario)

for mensagem in st.session_state["lista_mensagens"]: 
    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"]
    st.chat_message(quem_enviou).write(texto_mensagem)

if mensagem_usuario:
    # exibir a mensagem na tela
    # st.chat_message("quem ta mandando").write("mensagem do usuario")
    # "quem ta mandando" pode ser um:
        # user -> usuario
        # assistant -> chatbot
    st.chat_message("user").write(mensagem_usuario)
    mensagem1 = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem1)

    # pegar a resposta da IA
    resposta_modelo = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gemini-flash-lite-latest"
    )
    
    resposta_ia = resposta_modelo.choices[0].message.content

    # enviar a mensagem da IA no chat
    st.chat_message("assistant").write(resposta_ia)
    mensagem2 = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem2)

# manter o histórico (criar memória)

# tornar as respostas inteligentes
