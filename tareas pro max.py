import random
import sympy as sp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

# ----------------- Lógica de Tareas ------------------

def generar_tarea_matematica():
    tipo = random.choice([
        "ecuacion", "cuadratica", "limite", "fracciones", "trigonometria",
        "logaritmos", "matriz", "derivada", "integral", "sistema",
        "regla3", "porcentaje", "combinatoria", "probabilidad", "geometria", "estadistica"
    ])
    x, y = sp.symbols('x y')

    if tipo == "ecuacion":
        eq = sp.Eq(3*x - 7, 11)
        sol = sp.solve(eq, x)
        return f"🧮 Ecuación:\n{eq}\nSolución: x = {sol[0]}"

    elif tipo == "cuadratica":
        eq = sp.Eq(x**2 - 5*x + 6, 0)
        sol = sp.solve(eq, x)
        return f"🧮 Cuadrática:\n{eq}\nSoluciones: {sol}"

    elif tipo == "limite":
        f = (x**2 - 1)/(x - 1)
        l = sp.limit(f, x, 1)
        return f"🧮 Límite:\nlim x→1 ({f}) = {l}"

    elif tipo == "fracciones":
        expr = (1/(x + 1)) + (1/(x - 1))
        simpl = sp.simplify(expr)
        return f"🧮 Fracciones:\n{expr} = {simpl}"

    elif tipo == "trigonometria":
        expr = sp.sin(x)**2 + sp.cos(x)**2
        simpl = sp.simplify(expr)
        return f"🧮 Trigonometría:\n{expr} = {simpl}"

    elif tipo == "logaritmos":
        expr = sp.log(x**2)
        simpl = sp.simplify(expr)
        return f"🧮 Logaritmo:\nlog(x²) = {simpl}"

    elif tipo == "matriz":
        A = sp.Matrix([[random.randint(1, 5) for _ in range(2)] for _ in range(2)])
        B = sp.Matrix([[random.randint(1, 5) for _ in range(2)] for _ in range(2)])
        C = A * B
        return f"🧮 Matrices:\nA = {A}, B = {B}\nA·B = {C}"

    elif tipo == "derivada":
        f = x**2 * sp.sin(x)
        df = sp.diff(f, x)
        return f"🧮 Derivada:\n{f}\nDerivada: {df}"

    elif tipo == "integral":
        f = x**2 + 3*x + 2
        integ = sp.integrate(f, x)
        return f"🧮 Integral:\n∫({f}) dx = {integ} + C"

    elif tipo == "sistema":
        eq1 = sp.Eq(2*x + y, 5)
        eq2 = sp.Eq(x - y, 1)
        sol = sp.solve((eq1, eq2), (x, y))
        return f"🧮 Sistema de ecuaciones:\n{eq1}, {eq2}\nSolución: {sol}"

    elif tipo == "regla3":
        a, b, c = 3, 6, 9
        d = (b * c) / a
        return f"🧮 Regla de 3:\nSi {a} → {b}, entonces {c} → ?\nResultado: {d}"

    elif tipo == "porcentaje":
        total, porc = 200, 15
        res = (porc / 100) * total
        return f"🧮 Porcentaje:\n¿Cuánto es el {porc}% de {total}?\nRespuesta: {res}"

    elif tipo == "combinatoria":
        n, r = 5, 3
        res = sp.binomial(n, r)
        return f"🧮 Combinatoria:\nC({n},{r}) = {res}"

    elif tipo == "probabilidad":
        casos, total = 3, 8
        prob = casos / total
        return f"🧮 Probabilidad:\nP = {casos}/{total} = {prob:.2f}"

    elif tipo == "geometria":
        l = 5
        area = l ** 2
        perimetro = 4 * l
        return f"🧮 Geometría (cuadrado):\nLado = {l}, Área = {area}, Perímetro = {perimetro}"

    elif tipo == "estadistica":
        datos = [3, 5, 7, 5, 9]
        media = sum(datos)/len(datos)
        return f"🧮 Media de {datos} = {media}"

def generar_tarea_fisica():
    tipo = random.choice([
        "mrua", "mru", "newton", "trabajo", "energia", "presion", "ohm", "optica",
        "dilatacion_lineal", "dilatacion_cubica", "calor", "hooke", "potencia", "latente", "parabolico", "momento", "densidad"
    ])

    if tipo == "densidad":
        m, v = 500, 0.25
        d = m / v
        return f"⚙️ Densidad:\nm = {m}g, V = {v}cm³ → d = {d}g/cm³"
    elif tipo == "momento":
        m, v = 10, 5
        p = m * v
        return f"⚙️ Momento lineal:\nP = m·v = {p} kg·m/s"
    elif tipo == "parabolico":
        v, ang = 20, 45
        g = 9.8
        h = (v**2 * (sp.sin(sp.rad(ang)))**2)/(2*g)
        return f"⚙️ Movimiento Parabólico:\nAltura máxima = {h:.2f} m"
    elif tipo == "latente":
        m, L = 0.2, 334000
        Q = m * L
        return f"⚙️ Calor Latente:\nQ = {Q} J"
    elif tipo == "potencia":
        W, t = 500, 10
        P = W / t
        return f"⚙️ Potencia eléctrica:\nP = {P} W"
    elif tipo == "hooke":
        k, x = 200, 0.1
        F = k * x
        return f"⚙️ Ley de Hooke:\nF = kx = {F} N"
    elif tipo == "mrua":
        vi, t, a = 10, 4, 2
        d = vi * t + 0.5 * a * t**2
        return f"⚙️ MRUA:\nvi = {vi}, t = {t}, a = {a} → d = {d} m"
    elif tipo == "mru":
        v, t = 12, 5
        d = v * t
        return f"⚙️ MRU:\nd = v·t = {d} m"
    elif tipo == "newton":
        m, a = 5, 2
        F = m * a
        return f"⚙️ Newton:\nF = m·a = {F} N"
    elif tipo == "trabajo":
        f, d = 20, 10
        w = f * d
        return f"⚙️ Trabajo:\nW = F·d = {w} J"
    elif tipo == "energia":
        m, v = 2, 10
        ec = 0.5 * m * v**2
        return f"⚙️ Energía Cinética:\nE = {ec} J"
    elif tipo == "presion":
        f, a = 100, 2
        p = f / a
        return f"⚙️ Presión:\nP = F/A = {p} Pa"
    elif tipo == "ohm":
        v, r = 12, 4
        i = v / r
        return f"⚙️ Ley de Ohm:\nI = V/R = {i} A"
    elif tipo == "optica":
        ang = 30
        n1, n2 = 1, 1.5
        r = sp.asin(n1 * sp.sin(sp.rad(ang)) / n2)
        return f"⚙️ Refracción:\nÁngulo incidente = {ang}° → Ángulo refractado ≈ {sp.deg(r):.2f}°"
    elif tipo == "dilatacion_lineal":
        L0, alpha, dT = 2, 1e-5, 50
        dL = L0 * alpha * dT
        return f"⚙️ Dilatación Lineal:\nΔL = {dL} m"
    elif tipo == "dilatacion_cubica":
        V0, beta, dT = 1.5, 3e-5, 80
        dV = V0 * beta * dT
        return f"⚙️ Dilatación Cúbica:\nΔV = {dV} m³"
    elif tipo == "calor":
        m, c, dT = 1, 4186, 30
        Q = m * c * dT
        return f"⚙️ Calor específico:\nQ = {Q} J"

# ------------------ Interfaz con Kivy ------------------

class TareaApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.input = TextInput(hint_text="Escribe tu propio problema aquí...", size_hint=(1, 0.15))
        self.output = Label(text="", size_hint_y=None, halign="left", valign="top")
        self.output.bind(texture_size=self.update_height)
        scroll = ScrollView(size_hint=(1, 0.5))
        scroll.add_widget(self.output)

        btn_mate = Button(text="Tarea de Matemáticas", size_hint=(1, 0.1))
        btn_fisica = Button(text="Tarea de Física", size_hint=(1, 0.1))
        btn_custom = Button(text="Agregar problema personalizado", size_hint=(1, 0.1))

        btn_mate.bind(on_press=lambda x: self.generar("mate"))
        btn_fisica.bind(on_press=lambda x: self.generar("fisica"))
        btn_custom.bind(on_press=self.agregar_personalizado)

        self.layout.add_widget(btn_mate)
        self.layout.add_widget(btn_fisica)
        self.layout.add_widget(self.input)
        self.layout.add_widget(btn_custom)
        self.layout.add_widget(scroll)

        return self.layout

    def update_height(self, instance, value):
        instance.height = value[1]
        instance.text_size = (self.layout.width - 40, None)

    def generar(self, tipo):
        if tipo == "mate":
            texto = generar_tarea_matematica()
        else:
            texto = generar_tarea_fisica()
        self.output.text += f"\n\n{texto}"

    def agregar_personalizado(self, instance):
        texto = self.input.text.strip()
        if texto:
            self.output.text += f"\n\n📝 Personalizado:\n{texto}"
            self.input.text = ""

if __name__ == '__main__':
    TareaApp().run()
