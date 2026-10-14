import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

servico = ctrl.Antecedent(np.arange(0, 10.1, 0.1), "servico")
comida = ctrl.Antecedent(np.arange(0, 10.1, 0.1), "comida")
gorjeta = ctrl.Consequent(np.arange(0, 25.1, 0.1), "gorjeta")

servico["ruim"] = fuzz.gaussmf(servico.universe, 0, 1.5)
servico["medio"] = fuzz.gaussmf(servico.universe, 5, 1.5)
servico["bom"] = fuzz.gaussmf(servico.universe, 10, 1.5)
comida["ruim"] = fuzz.trimf(comida.universe, [0, 0, 5])
comida["boa"] = fuzz.trimf(comida.universe, [5, 10, 10])
gorjeta["baixa"] = fuzz.trimf(gorjeta.universe, [0, 0, 13])
gorjeta["media"] = fuzz.trimf(gorjeta.universe, [0, 13, 25])
gorjeta["alta"] = fuzz.trimf(gorjeta.universe, [13, 25, 25])

regras = [
    ctrl.Rule(comida["ruim"] | servico["ruim"], gorjeta["baixa"]),
    ctrl.Rule(servico["medio"], gorjeta["media"]),
    ctrl.Rule(comida["boa"] | servico["bom"], gorjeta["alta"]),
]
sistema = ctrl.ControlSystemSimulation(ctrl.ControlSystem(regras))

for s, c in [(3, 2), (6.5, 9.0), (9.8, 9.5)]:
    sistema.input["servico"] = s
    sistema.input["comida"] = c
    sistema.compute()
    g = sistema.output["gorjeta"]
    print(f"servico={s} comida={c} -> {g:.2f}%")
