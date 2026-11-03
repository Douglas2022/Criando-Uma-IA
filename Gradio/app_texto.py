import gradio as gr
def reverter_texto(texto):
    return texto[::-1]

iface = gr.Interface(
    fn=reverter_texto,
    inputs="text",
    outputs="text",
    title="Reversor de Texto",
    description="Digite um texto e ele será revertido."
)
iface.launch()