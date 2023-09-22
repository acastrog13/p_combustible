import pandas as pd
import warnings
import streamlit as st

url='http://ec.europa.eu/energy/observatory/reports/latest_prices_with_taxes.xlsx'

#DEFINICION DE LAS FUNCIONES


def num_form(value):
    value=(value).replace(',','')    
    value=float(value)/1000
    value=round(float(value) , 2)    
    return (value)


def doc(): #FUNCION QUE LEE TODO EL EXCEL
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        precios = pd.read_excel(url, 'En In EURO', header=10, usecols='B:D', 
                                names=['Paises','Gasolina','Diesel'], nrows=27, 
                                dtype={'Paises':str,'Gasolina':float,'Diesel':float},
                                engine="openpyxl",
                                converters={'Gasolina':num_form, 'Diesel':num_form},
                                thousands=None, decimal= '.')
    
    return(precios)


def pais (url,i):#FUNCION QUE NOS DEVUELVE EL NOMBRE DEL PAIS
    
    precios=doc()
    pais=precios['Paises']
    return(pais[i])


def com_gas ():#FUNCION QUE COMPARA LOS PRECIOS DE LA GASOLINA
    
    precios=doc()
    
    com=precios['Gasolina']
    
    max_gas=0.0
    min_gas=4.0
    nmin_pais=0
    nmax_pais=0
    
    for (i) in (range(27)):
                
        
        if (float(max_gas)<float(com[i])):
            max_gas=float(com[i])
            nmax_pais=i
            
        if (float(min_gas)>float(com[i])):
            min_gas=float(com[i])
            nmin_pais=i
    
    st.write(pais(url,nmin_pais), 'es el país con la gasolina más barata de la UE, ', min_gas, 'euro/L')
    st.write(pais(url,nmax_pais), 'es el país con la gasolina más cara de la UE, ', max_gas, 'euro/L')
 
def com_diesel ():#FUNCION QUE NOS COMPARA LOS PRECIOS DEL DIESEL
    precios=doc()
    
    com=precios['Diesel']
    
    max_diesel=0.0
    min_diesel=4.0
    nmin_pais=0
    nmax_pais=0
    
    for (i) in (range(27)):
                
        
        if (float(max_diesel)<float(com[i])):
            max_diesel=float(com[i])
            nmax_pais=i
            
        if (float(min_diesel)>float(com[i])):
            min_diesel=float(com[i])
            nmin_pais=i
    
    st.write(pais(url,nmin_pais), 'es el país con el diesel más barato de la UE, ', min_diesel, 'euro/L')
    st.write(pais(url,nmax_pais), 'es el país con el diesel más caro de la UE, ', max_diesel, 'euro/L')
 

#INICIO DEL PROGRAMA



st.title('COMPARADOR PRECIOS DE COMBUSTIBLE DE LA UE')
st.subheader('¿Qué quieres consultar?')
aux=st.radio(
    'Elige todas las veces que quieras',
    ['Todos los datos combustible en la UE',
     'Comparativa de los precios de gasolina',
     'Comparativa de los precios de diesel'],
    )

#st.button("Salir", type="primary")
if st.button('Aceptar'):
    
    if aux=='Todos los datos combustible en la UE':
        st.write(doc())
        
    elif aux=='Comparativa de los precios de gasolina':
        (com_gas())
        
    else:
        (com_diesel())
  
else:
    exit(1)


if st.button("Salir", type="primary"):
    exit(1)