#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 08:47:43 2021

@author: gaddiel
"""

import pandas as pd
import numpy as np
import string

class CDIN:
    
    def dqr(data):
        # Lista de variables de la base de datos
        columns = pd.DataFrame(list(data.columns.values),columns=['Nombres'], 
                               index=list(data.columns.values))
        
        # Lista de tipos de datos
        data_types = pd.DataFrame(data.dtypes, columns=['Tipo_Dato'])
        
        #Lista de valores perdidos
        missing_values = pd.DataFrame(data.isnull().sum(), columns=['Datos_Faltantes'])
        
        # Lista de valores unicos
        unique_values = pd.DataFrame(columns=['valores_unicos'])
        for col in list(data.columns.values):
            unique_values.loc[col] = [data[col].nunique()]
        
        # Promedio de los valores numéricos
        mean_values = pd.DataFrame(columns=['promedio'])
        for col in list(data.columns.values):
            try:
                mean_values.loc[col] = [data[col].mean()]
            except: 
                pass
        
        # minimos de los valores numéricos
        min_values = pd.DataFrame(columns=['valor_minimo'])
        for col in list(data.columns.values):
            try:
                min_values.loc[col] = [data[col].min()]
            except: 
                pass
        
        # maximos de los valores numéricos
        max_values = pd.DataFrame(columns=['valor_máximo'])
        for col in list(data.columns.values):
            try:
                max_values.loc[col] = [data[col].max()]
            except: 
                pass
        
        # columna que se llame categórica (columna tipo booleana) cuando sea True, represente una variable categórica, 
        # false sea una variable numérica
        categorical = pd.DataFrame(columns=['categorica'])
        for col in list(data.columns.values):
            if data[col].dtype == 'object':
                categorical.loc[col] = True
            else:
                categorical.loc[col] = False
        
        
        return columns.join(data_types).join(missing_values).join(unique_values).join(mean_values).join(min_values).join(max_values).join(categorical)
    
    ## Métodos para limpieza de datos
    
    # Remover signos de puntuación
    def remover_punctuation(x):
        try:
            x=''.join(ch for ch in x if ch not in string.punctuation)
        except:
            pass
        return x
    
    def remove_digits(x):
        try:
            x=''.join(ch for ch in x if ch not in string.digits)
        except:
            pass
        return x
    # Remover los espacios en blanco
    def remove_whitespace(x):
        try:
            x=''.join(x.split())
        except:
            pass
        return x
    
    # reemplazar texto
    def replace_text(x, to_replace, replacement):
        try:
            x=x.replace(to_replace, replacement)
        except:
            pass
        return x
    
    # Convertir a minúsculas
    def lowercase_text(x):
        try:
            x=x.lower()
        except:
            pass
        return x
    
    #Convertir a mayúsculas
    def uppercase_text(x):
        try:
            x=x.upper()
        except:
            pass
        return x
    
    #Quita espacios en blando izquierda y derecha
    def remove_whitespace_lr(x):
        try:
    #         x=x.lstrip()
    #         x=x.rstrip()
            x=x.lstrip().rstrip()
        except:
            pass
        return x
    
    

    
    
    
    
    
    