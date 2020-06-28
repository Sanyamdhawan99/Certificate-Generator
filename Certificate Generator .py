#!/usr/bin/env python
# coding: utf-8

# ### Import Libraries

# In[ ]:


""" Uncomment and run this cell if you donot have these libraries """

# !pip install cv2
# !pip install pandas
# !pip install numpy


# In[ ]:


import cv2
import pandas as pd
import numpy as np


# ### Read the Names/Content to be written on the certificate
# * The names should be in an excel or csv file for this code
# * If you have the data in any other file format, please use the required file reading syntax

# In[ ]:


""" Fill in the file path where you have the text to be written on the certificate """
text_file_path = ''
certificate_text = pd.read_excel(text_file_path)

""" Use this if you have csv file """
certificate_text = pd.read_csv(text_file_path)


# * Find the appropriate column in the certificate_text dataframe and read the data out of it
# 
# Here I present the examples of how to do that.
# 
# 1. If you have names in a single columns say Participants, then, <br>
#     names = np.array(certificate_text['Participants'].dropna()) <br>
#     
#     
# 2. If you have names that are spread over different columns, then, <br>
#     names_1 = np.array(certificate_text['Name'].dropna()).tolist() <br>
#     names_2 = np.array(certificate_text['Name1'].dropna()).tolist() <br>
#     names_3 = np.array(certificate_text['Name2'].dropna()).tolist() <br>
#     names = names_1 + names_2 + names_3 <br>
#     
#     
# * Do this same for every text column you need on the certificate

# In[ ]:


""" Change this according to the data you have """
names = np.array(certificate_text['Participants'].dropna())
len(names)


# In[ ]:


""" Convert all names to Uppercase """
names = [i.upper() for i in names]


# In[ ]:


""" certi_template -> the png or jpg certificate template """
certi_template = ''

""" certi_output_dir -> the directory where you want to have your certificates generated """
certi_output_dir = ''


# ### Main function to write text on the certificate

# In[ ]:


""" Set these parameters for your certificate template 
    Generate single certificate and try out these parameters accordingly
"""
font_size = 8
font_color = (0,0,0)  # RGB channel -> currently set to black
x_coordinate = 0
y_coordinate = 0


# In[ ]:


def make_certificate(names, certi_template, certi_output_dir):
    count = 0
    for name in names:
        count += 1
        certi = cv2.imread(certi_template)
        font = cv2.FONT_HERSHEY_PLAIN
        textsize = cv2.getTextSize(name, font, font_size, 2)[0]
        text_x = (certi.shape[1] - textsize[0]) / 2 + x_coordinate
        text_y = (certi.shape[0] + textsize[1]) / 2 - y_coordinate
        text_x = int(text_x)
        text_y = int(text_y)
        cv2.putText(certi, name, (text_x, text_y ), font, font_size, font_color, 6) # last for thickness
        certi_path = certi_output_dir + name + '.png'
        cv2.imwrite(certi_path,certi)
        print(count, end = ' ')
        print(' Writing certi for ' + name + ' to ' + certi_path)


# In[ ]:


""" Make the funtion call """
make_certificate(names, certi_template, certi_output_dir)

