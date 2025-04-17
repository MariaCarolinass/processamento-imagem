import matplotlib
import gradio as gr
from transformations.translation import Translation
from transformations.rotation import Rotation
from transformations.scale import Scale
from operations.adjustment import Adjustment
from operations.conversion import Conversion
from corrections.control import Control

matplotlib.use('Agg')

def process_image(image, x, y, degree, scale, color, contrast, gamma):
    translation = Translation(x, y)
    image = translation.move_img(image)

    rotation = Rotation(degree)
    image = rotation.rotate_img(image)

    scale = Scale(scale)
    image = scale.change_scale(image)

    if color != "RGB":
        conversion = Conversion()
        if color == "Cinza":
            image = conversion.convert_rgb_to_gray(image)
        elif color == "HSV": 
            image = conversion.convert_rgb_to_hsv(image)
        else:
            image = conversion.convert_rgb_to_lab(image)

    adjustment = Adjustment(contrast)
    image = adjustment.adjust_contrast(image)

    control = Control(gamma)
    image = control.control_gammar(image)

    return image

demo = gr.Interface(
   fn=process_image,
   inputs=[
        gr.Image(label="Carregar Imagem"),
        gr.Number(label="Translação X", info="Deslocamento horizontal da imagem"),
        gr.Number(label="Translação Y", info="Deslocamento vertical da imagem"),
        gr.Slider(0, 360, value=0, label="Ângulo de Rotação", info="Rotacionamento da imagem"),
        gr.Slider(0.1, 10.0, value=1.0, label="Escala", info="Ampliação e redução da imagem"),
        gr.Dropdown(["RGB", "Cinza", "HSV", "LAB"], value="RGB", label="Conversão de espaços de cores", info="Cor da imagem"),
        gr.Slider(1, 100, value=1, label="Ajuste de Contraste", info="Controle de contraste da imagem"),
        gr.Slider(0.1, 3.0, value=1.0, label="Controle Gamma", info="Correção Gamma e clareamento"),
    ],
   outputs="image",
)

demo.launch()