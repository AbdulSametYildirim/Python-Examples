"""
Aşağıdaki Python kodu, yapay sinir ağları (YSA) kullanarak bir görüntü sınıflandırma (image classification) projesi örneği vermektedir.
Bu örnek projede, verilen bir görüntünün hangi sınıfa ait olduğunu tahmin etmeye çalışacağız.
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Giriş verilerini yükle
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Sınıf etiketlerini düzenle
class_names = ['köpek', 'kedi', 'güvercin', 'tavşan', 'ince kuyruklu köpek',
               'panda', 'gri geyik', 'ördek', 'köpekbalığı', 'araba']

# Görüntüleri normalize et
x_train = x_train / 255.0
x_test = x_test / 255.0

# YSA modelini oluştur
model = tf.keras.Sequential()
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(10))

# Modeli derle
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Modeli eğit
history = model.fit(x_train, y_train, epochs=10,
                    validation_data=(x_test, y_test))

# Modelin performansını değerlendir
test_loss, test_acc = model.evaluate(x_test,  y_test, verbose=2)
print('Test loss:', test_loss)
print('Test accuracy:', test_acc)