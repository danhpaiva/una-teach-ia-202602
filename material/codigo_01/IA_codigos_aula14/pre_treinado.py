import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
import numpy as np
import keras

url = ("https://storage.googleapis.com/download.tensorflow.org/"
       "example_images/YellowLabradorLooking_new.jpg")
caminho = keras.utils.get_file("labrador.jpg", url)
img = keras.utils.load_img(caminho, target_size=(224, 224))
x = keras.utils.img_to_array(img)[np.newaxis]
x = keras.applications.mobilenet_v2.preprocess_input(x)

modelo = keras.applications.MobileNetV2(weights="imagenet")
print("parametros do MobileNetV2:", modelo.count_params())
prob = modelo.predict(x, verbose=0)
for _, nome, p in keras.applications.mobilenet_v2.decode_predictions(prob, top=3)[0]:
    print(f"{nome:20s} {float(p):.3f}")
