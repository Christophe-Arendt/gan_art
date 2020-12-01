##########################################################################
#     Environment Set-up
##########################################################################

import streamlit as st
import pandas as pd
from PIL import Image
import os
import IPython.display as display
import matplotlib.pyplot as plt
import numpy as np
from gan_art.utils import *
import io



#mpl.rcParams['figure.figsize'] = (12,12)
#mpl.rcParams['axes.grid'] = False
#os.environ['TFHUB_MODEL_LOAD_FORMAT'] = 'COMPRESSED'
#import tensorflow as tf
import tensorflow_hub as hub


##########################################################################
#     Layout
##########################################################################

st.set_page_config(
  page_title="Ex-stream-ly Cool App",
  page_icon="",
  layout="centered",
  initial_sidebar_state="expanded",
  )
##########################################################################
#     Style dictionnary
##########################################################################

style_dic = {'Choose' : 'Nothing',
            'Van Gogh': 'data/van_gogh_1.jpg',
            'Picasso': 'data/picasso_1.jpg',
            'Andy Warhol': 'data/warhol_1.jpg',
            }

##########################################################################
#     Design Top
##########################################################################

analysis = st.sidebar.selectbox("",['Every Human Is An Artist','AI-Gallery','About'])

##########################################################################
#     Upload Buffer
##########################################################################



if analysis == 'Every Human Is An Artist':
  # Overall title
  st.markdown("<h1 style='text-align: center; color: DarkBlue;'>Every Human Is An Artist</h1>", unsafe_allow_html=True)
  st.text("")
  st.markdown("<h3 style='text-align: center;'>Become your own Picasso and us Artificial Intelligence to transform your pictures into Art!</h3>", unsafe_allow_html=True)
  st.text("")
  st.text("")
  st.markdown("<h3 style='text-align: left; color: CornflowerBlue;'>STEP 1 : Upload your pitcture</h3>",unsafe_allow_html=True)
  st.text("")
  # Upload and display image
  uploaded_file = st.file_uploader("Choose a file" ,type=["jpg", "ipeg", "jpeg", "png"] )

  if uploaded_file is None:
    st.text("")
  else:
    g = io.BytesIO(uploaded_file.read())  # BytesIO Object
    temporary_location = "temp.jpg"
    with open(temporary_location, 'wb') as out:  # Open temporary file as bytes
      out.write(g.read())  # Read bytes into file
      # close file
      out.close()

    image = Image.open("temp.jpg").resize((800,500))
    st.image(image, caption='',use_column_width=False)


  ##########################################################################
  #     Choose Style
  ##########################################################################

  st.markdown("<h3 style='text-align: left; color: CornflowerBlue;'>STEP 2 : Choose your style </h3>",unsafe_allow_html=True)
  st.markdown("<h4 style='text-align: left'>Have a look at the AI-Gallery for more information about the different styles</h4>",unsafe_allow_html=True)

  st.text("")
  option = st.selectbox('Style Options',list(style_dic.keys()))
  selected = []
  if option == 'Choose':
    st.text('')

  if option == 'Van Gogh':
    selected.append(option)
  if option != None and option != 'Choose':
    image = Image.open(style_dic[option])
    #st.image(image, caption='Sunrise by the mountains',use_column_width=False)
    st.text('')


  ##########################################################################
  #     Style Transformer
  ##########################################################################

  st.markdown("<h3 style='text-align: left; color: CornflowerBlue;'>STEP 3 : Generate your piece of Art</h3>",unsafe_allow_html=True)
  if st.button('CLICK HERE TO SEE YOUR PIECE OF ART'):
    if option != None and option != 'Choose':
      style_path = style_dic[option]
      content_path = 'temp.jpg'
      style_image = load_img(style_path)
      content_image = load_img(content_path)

      # Create image
      hub_model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
      stylized_image = hub_model(tf.constant(content_image), tf.constant(style_image))[0]
      img = tensor_to_image(stylized_image).resize((800,500))
      st.image(img)

if analysis == 'AI-Gallery':
  st.markdown("<h1 style='text-align: center; color: DarkBlue;'>AI-Gallery</h1>", unsafe_allow_html=True)
  st.text("")
  st.markdown("<h3 style='text-align: center;'>Have a look at the different styles currently available!</h3>", unsafe_allow_html=True)
  st.text("")
  for key in style_dic:
    if key is not 'Choose':
      st.title(key)
      image = Image.open(style_dic[key])
      st.image(image, caption='', use_column_width=True)


if analysis == 'About':

  st.markdown("<h1 style='text-align: center; color: DarkBlue;'>Acknowledgments</h1>", unsafe_allow_html=True)
  st.text("")
  st.markdown("<h3 style='text-align: center;'>Special thanks to my father which who I share my passion with art and who made me disocover the beauty of it</h3>", unsafe_allow_html=True)
  image = Image.open('data/banner_galleria.jpg')
  st.image(image, caption='', use_column_width=True)
  st.markdown("<h1 style='text-align: center; color: DarkBlue;'>About</h1>", unsafe_allow_html=True)
  st.text("")

st.text("")
st.text("")
st.text("")
st.text("")
st.markdown("<h4 style='text-align: center; color: DarkBlue;'>[ Created by Christophe Arendt ]</h4>", unsafe_allow_html=True)
