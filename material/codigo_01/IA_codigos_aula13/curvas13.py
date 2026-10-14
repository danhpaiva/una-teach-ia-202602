import json
import numpy as np
from qlearning_grid import treinar
from cartpole_q import treinar as treinar_cp

def blocos(v, n):
    v = np.array(v, dtype=float)
    return [round(float(v[i:i + n].mean()), 1) for i in range(0, len(v), n)]

_, ret = treinar()
Q, ret_cp = treinar_cp()
json.dump({"grid": blocos(ret, 25), "cartpole": blocos(ret_cp, 250)},
          open("curvas13.json", "w"))
print("grid:", blocos(ret, 25))
print("cartpole:", blocos(ret_cp, 250))
