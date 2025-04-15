import gradio as gr

def process_image(image):
    translation = Translation(50, 100)
    translated_image = translation.move_img(image)
    return translated_image

interface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Image(type="numpy")
)

interface.launch()