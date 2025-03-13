import matplotlib.pyplot as plt
from lxml import etree

# Ваш MathML код
mathml_code = """
<m:math xmlns:m="http://www.w3.org/1998/Math/MathML">
    <m:mstyle displaystyle="true">
        <m:semantics>
            <m:mrow>
                <m:mfrac>
                    <m:mrow>
                        <m:msup>
                            <m:mn>9</m:mn>
                            <m:mrow>
                                <m:mi>sin</m:mi>
                                <m:mn>2</m:mn>
                                <m:mi>x</m:mi>
                            </m:mrow>
                        </m:msup>
                        <m:mo>−</m:mo>
                        <m:msup>
                            <m:mn>3</m:mn>
                            <m:mrow>
                                <m:mn>2</m:mn>
                                <m:msqrt>
                                    <m:mn>2</m:mn>
                                </m:msqrt>
                                <m:mi>sin</m:mi>
                                <m:mi>x</m:mi>
                            </m:mrow>
                        </m:msup>
                    </m:mrow>
                    <m:mrow>
                        <m:msqrt>
                            <m:mrow>
                                <m:mn>11</m:mn>
                                <m:mi>sin</m:mi>
                                <m:mi>x</m:mi>
                            </m:mrow>
                        </m:msqrt>
                    </m:mrow>
                </m:mfrac>
                <m:mo>=</m:mo>
                <m:mn>0</m:mn>
            </m:mrow>
        </m:semantics>
    </m:mstyle>
</m:math>
"""


# Функция для преобразования MathML в LaTeX
def mathml_to_latex(mathml):
    # Парсинг MathML
    tree = etree.fromstring(mathml)

    # Преобразование MathML в LaTeX
    latex = ""

    for elem in tree.iter():
        if elem.tag.endswith('mn'):
            latex += elem.text
        elif elem.tag.endswith('mi'):
            latex += elem.text
        elif elem.tag.endswith('mo'):
            latex += elem.text
        elif elem.tag.endswith('mfrac'):
            latex = f"\\frac{{{latex}}}{{"  # Начало дроби
        elif elem.tag.endswith('mrow'):
            latex += "{"  # Начало группы
        elif elem.tag.endswith('msup'):
            latex += f"{{{latex}}}^{{"  # Степень
        elif elem.tag.endswith('msqrt'):
            latex = f"\\sqrt{{{latex}}}"  # Квадратный корень
        elif elem.tag.endswith('mstyle'):
            continue  # Игнорируем стиль
        elif elem.tag.endswith('msemantics'):
            continue  # Игнорируем семантику

    # Закрытие всех открытых фигурных скобок
    latex += "}" * latex.count("{")

    return latex


# Преобразование MathML в LaTeX
latex_expression = mathml_to_latex(mathml_code)

# Рендеринг LaTeX с помощью Matplotlib
plt.figure(figsize=(8, 4))
plt.text(0.5, 0.5, f"${latex_expression} = 0$", fontsize=24, ha='center')
plt.axis('off')  # Отключаем оси
plt.savefig('math_expression.png', bbox_inches='tight', pad_inches=0.1)
plt.close()

# Выводим изображение
img = plt.imread('math_expression.png')
plt.imshow(img)
plt.axis('off')  # Отключаем оси
plt.show()
