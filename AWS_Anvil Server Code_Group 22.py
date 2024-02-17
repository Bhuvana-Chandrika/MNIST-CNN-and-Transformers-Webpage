import anvil.users
import anvil.email
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import bcrypt
import anvil.media
import pandas  as pd
import tensorflow as tf
from tensorflow import keras
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt
import anvil.mpl_util


model_cnn = keras.models.load_model('Cnn_model.h5')
anvil.server.connect("server_JKG6IABAE6HN7WQCWK4S37LV-6XFBKTEOZH3PBGVS")


@anvil.server.callable
def authenticate_user(email,password):
  user = app_tables.users.get(email=email)
  if (user is not None) and bcrypt.checkpw(password.encode('utf-8'),user['password_hash'].encode('utf-8')):
    return True
  else:
    return False

@anvil.server.callable
def validate_csv(file):
 with anvil.media.TempFile(file) as filename:   
   try:
     df = pd.read_csv(filename, header=None)  
     if df.shape != (28,28):
       return "Error: File must have 28 rows and 28 columns"     
     max_val = df.max().max()   
     if max_val <= 1 or max_val<=255:
       return "Success"   
     else:
       return "Error: Pixel values must be 0-255 or 0-1"   
   except pd.errors.ParserError:
     return "Error: Invalid CSV file"

@anvil.server.callable
def img_show(filename):
    with anvil.media.TempFile(filename) as file:  
      try:
        data = pd.read_csv(file, header=None) 
        image_matrix = np.array(data).reshape(28, 28)
        plt.figure()
        plt.imshow(image_matrix, cmap='gray')    
        return anvil.mpl_util.plot_image()
      except:
        return "Image not Formed"

@anvil.server.callable
def take_input_cnn(filename):
  with anvil.media.TempFile(filename) as file:  
    try:
        df = pd.read_csv(file, header=None) 
        numpy_array = df.values
        numpy_array = numpy_array.reshape(1, 28, 28, 1)   
        pred = model_cnn(numpy_array)
        new_array= pred.numpy()
        max_index_cnn = np.argmax(new_array)
        return max_index_cnn
    except:
        return 'Execution Failed'

# Define ClassToken layer for creating a class token
class ClassToken(tf.keras.layers.Layer):
    def _init_(self):
        super()._init_()

    def build(self, input_shape):
        w_init = tf.random_normal_initializer()
        self.w = tf.Variable(
            initial_value = w_init(shape=(1, 1, input_shape[-1]), dtype=tf.float32),
            trainable = True
        )

    def call(self, inputs):
        batch_size = tf.shape(inputs)[0]
        hidden_dim = self.w.shape[-1]

        cls = tf.broadcast_to(self.w, [batch_size, 1, hidden_dim])
        cls = tf.cast(cls, dtype=inputs.dtype)
        return cls

@anvil.server.callable
def take_input_transformer(filename):
  model_tf = keras.models.load_model('transformer_group22.h5', custom_objects={'ClassToken': ClassToken})
  with anvil.media.TempFile(filename) as file:  
    try:
        df = pd.read_csv(file, header=None) 
        print(df.head())
        numpy_array = df.values
        numpy_array= np.array(numpy_array) 
        if np.max(numpy_array) > 1:
            numpy_array = numpy_array / 255.0
        x = np.zeros((1,16,49))
        for img in range(1):
          ind = 0
          for row in range(4):
              for col in range(4):
                  x[img, ind, :] = numpy_array[(row * 7):((row + 1) * 7), (col * 7):((col + 1) * 7)].ravel()
                  ind += 1
        pos_feed = np.array([list(range(16))])
        predicted_output = model_tf.predict([x,pos_feed])
        max_index_transformer = np.argmax(predicted_output)
        return max_index_transformer
    except:
        return 'Execution Failed'
    
anvil.server.wait_forever()