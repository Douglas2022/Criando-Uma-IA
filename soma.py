import gradio as gr

def soma(a, b):
    return a + b

print(soma(3, 2)) 

iface = gr.Interface(
fn=soma, inputs=["number", "number"], outputs="number",
title = "Calculadora de soma",
description = "Esta é uma calculadora simples que soma dois números.",
theme = "default"
)
iface.launch()