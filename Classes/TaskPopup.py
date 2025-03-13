import io
import pygame
import matplotlib.pyplot as plt
from mathml_to_latex.converter import MathMLToLaTeX

# from sdamgia import SdamGIA

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# tasks = SdamGIA()
# data = tasks.get_problem_by_id("math", "1001")["condition"]["text"]

# MathML код
mathml_code = """<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mstyle 
displaystyle=&quot;true&quot;><semantics><mrow><mfrac><mrow><msup><mn>9</mn><mrow><mi>sin</mi><mn>2</mn><mi>x</mi
></mrow></msup><mo>&#x2212;</mo><msup><mn>3</mn><mrow><mn>2</mn><msqrt><mn>2</mn></msqrt><mi>sin</mi><mi>x</mi></mrow
></msup></mrow><mrow><msqrt><mrow><mn>11</mn><mi>sin</mi><mi>x</mi></mrow></msqrt></mrow></mfrac><mo>=</mo><mn>0</mn
></mrow></semantics></mstyle></math>"""

mathml_code = """<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><semantics><mrow><mover 
accent=&quot;true&quot;><mi>a</mi><mo>&#x2192;</mo></mover><mrow><mo>( 
</mo><mrow><mn>25</mn><mo>;</mo><mtext>&#x2009;</mtext><mn>0</mn></mrow><mo>)</mo></mrow></mrow></semantics>
<semantics><mrow><mover 
accent=&quot;true&quot;><mi>b</mi><mo stretchy=&quot;true&quot;>&#x2192;</mo></mover><mrow><mo>(
</mo><mrow><mn>1</mn><mo>;</mo><mtext>&#x2009;</mtext><mo>&#x2212;</mo><mn>5</mn></mrow><mo>)</mo></mrow><mo>.</mo
></mrow></semantics></math>"""

# Преобразование MathML в LaTeX
latex_expression = f"${MathMLToLaTeX().convert(mathml_code)}$"
latex_expression = (r"$\varphi(a)=a\prod_{i=1}^{k} \left(1-\frac{1}{p_i}\right)=(p_{1}^{\alpha _1}-p_{1}^{\alpha "
                    r"_1-1})\ldots (p_{k}^{\alpha _k}-p_{k}^{\alpha _k-1}).$")
# Создание фигуры
plt.figure(figsize=(5, 2))

# Добавление текста с LaTeX
plt.text(0.5, 0.5, latex_expression, fontsize=12, ha='center', va='center')

# Отключение осей
plt.axis('off')

# Сохранение графика в объект BytesIO
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)  # Перемещение указателя в начало буфера

# Загрузка изображения в Pygame
image = pygame.image.load(buf)


# Функция для отображения всплывающего окна
def show_popup():
    popup_surface = pygame.Surface(image.get_size())
    popup_surface.fill(BLACK)
    # font = pygame.font.Font(None, 36)
    # text = font.render(data, True, WHITE)

    popup_surface.blit(image, (0, 0))

    return popup_surface
