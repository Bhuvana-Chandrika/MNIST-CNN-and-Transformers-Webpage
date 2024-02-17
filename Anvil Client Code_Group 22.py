
#login page client code on Anvil 

from ._anvil_designer import LoginTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Login(LoginTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    email=self.email.text
    password=self.password.text

    user_exists = anvil.server.call('authenticate_user',email,password)
    
    if user_exists:
      open_form('Upload')
    else:
      alert('Invalid Credentials')
    pass

# Upload page client code on Anvil 
  
from ._anvil_designer import UploadTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Upload(UploadTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    #TODO: put items in designer
    # self.topic_drop.items = ['pricing', 'tutors', 'classes', 'feedback', 'other']
    self.button_1.visible=False
  

  def file_loader_1_change(self, file, **event_args):
    if file.name.endswith('.csv'):
        self.file_loader_1.visible = False
        self.label_1.visible = True
        self.label_1.text = 'Working on it, please be patient...'
        result = anvil.server.call('validate_csv', file)
        if result == "Success":
            self.label_1.text = 'File uploaded successfully'
            self.image_1.source = anvil.server.call('img_show', file)
            cnn_pred = anvil.server.call('take_input_cnn', file)
            self.label_3.text = cnn_pred
            trans_pred = anvil.server.call('take_input_transformer', file)
            self.label_4.text = trans_pred
            self.file_loader_1.visible = True
            self.file_loader_1.text = 'Upload'
            self.label_1.visible=False
        else:
            self.label1.visible = True
            self.label_1.text = result
            self.button_1.visible = True
    else:
        self.label_1.visible=True
        self.label_1.text = 'Invalid file type. Only CSV file formats are allowed.'
        self.button_1.visible = True
    pass

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('CNN')
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Transformers')
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Upload')
    pass

#CNN page client code on Anvil
  
from ._anvil_designer import CNNTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class CNN(CNNTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Upload')
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Transformers')
    pass
  
#Transformer page client code on Anvil 
  
from ._anvil_designer import TransformersTemplate
from anvil import *
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Transformers(TransformersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('Upload')
    pass

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('CNN')
    pass