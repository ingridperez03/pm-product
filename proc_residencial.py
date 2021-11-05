import os
import pandas as pd
from dimensio import Dimensio
from indicador import Indicador

data_path = os.path.join('dades','residencials')

'''
    Netejar dades referents a l'any de creació dels edificis (antiguitat)
'''

def initAnt(nivell):
    path = os.path.join(data_path, 'antiguitat')

    nom_arxiu = 'Resi_' + nivell + '_2002_2011.csv'
    df = pd.read_csv(os.path.join(path,nom_arxiu), index_col=False, error_bad_lines=False)
    years = pd.DataFrame(['2002', '2003', '2004', '2005', '2006', '2007','2008', '2009', '2010', '2011'])
    
    #Transposem els edificis amb antiguitat
    df_values = df.drop(['Codi', 'Literal', 'Total'], axis = 1)
    df_values_t = df_values.T
    
    #Modificacions per tenir els nivells i els anys
    df_aux = df[['Codi', 'Literal']]
    df_aux = pd.concat([df_aux] * 10).sort_values('Literal').reset_index()
    df_years = pd.concat([years] * len(df_values_t.columns)).reset_index().reset_index().drop(['index'], axis = 1).rename({'level_0':'ind', 0:'Any'}, axis =1)
    df_aux_year = df_aux.join(df_years).drop(['index'], axis = 1)
    
    #Passem totes les dades a la estructura [codi, any, nivell, edificis amb antiguitat]
    all_values = []
    for column in df_values_t:
        this_column_values = df_values_t[column].tolist()
        all_values += this_column_values

    one_column_df = pd.DataFrame(all_values).reset_index().rename({0:'Values', 'index':'ind'}, axis = 1)

    data = df_aux_year.merge(one_column_df).drop(['ind'], axis = 1)
    
    '''
    #por si el codigo tiene que tener 6 digitos
    if nivell == 'Municipis':
        data['Codi'] = data['Codi'].astype(str).str.zfill(6)   
    '''

    indicador = Indicador(data, range(2002,2011), nivell, 'unitats')


'''
    Netejar dades referents a la demanda de habitatges socials per anys (demanda)
'''

def initDem():
    path = os.path.join(data_path, 'demanda')

    nom_arxiu = 'Resi_comarca_2018_2012.csv'
    df = pd.read_csv(os.path.join(path,nom_arxiu), index_col=False, error_bad_lines=False)
    years = pd.DataFrame(['2012', '2013', '2014', '2015', '2016', '2017','2018'])

    #Separem els valors númerics eliminant les comarques
    df_values_t = df.drop(['Comarques'], axis = 1).T

    #Fem el dataframe de les comarques y anys. 
    df_aux = df[['Comarques']]
    df_aux = pd.concat([df_aux] * 7).sort_values('Comarques').reset_index().rename({'index':'codi', 'level_0':'ind'}, axis = 1)
    df_aux['codi'] = df_aux['codi'] + 1
    df_years = pd.concat([years] * len(df_values_t.columns)).reset_index().reset_index().drop(['index'], axis = 1).rename({'level_0':'ind', 0:'Any'}, axis =1)
    df_aux_year = df_aux.join(df_years)

    #Passem totes les dades a la estructura [codi, any, nivell, demanda]
    all_values = []
    for column in df_values_t:
        this_column_values = df_values_t[column].tolist()
        all_values += this_column_values

    one_column_df = pd.DataFrame(all_values).reset_index().rename({0:'Values', 'index':'ind'}, axis = 1)

    data = df_aux_year.merge(one_column_df).drop(['ind'], axis = 1)

    indicador = Indicador(data, range(2012,2018), 'comarca', 'unitats')


'''
    Netejar dades referents als habitants que viuen en un habitatge (habitants)
'''

def initHab():
    path = os.path.join(data_path, 'habitants')
    
    data = pd.DataFrame()
    for any_ in ['1996', '2001', '2011']:
        nom_arxiu = 'Resi_Comarques_' + any_ + '.csv'
        df = pd.read_csv(os.path.join(path,nom_arxiu))
        df['Any'] = any_

        #Any 2011 li falta una columna de 6 persones. Dupliquem la de >6. 
        if any_ == '2011':
            df_filtered = df.drop(['Unnamed: 8'], axis = 1)
            df_filtered['6'] =  df_filtered['>6']
            df_filtered = df_filtered[['Comarca', '1', '2', '3', '4', '5', '6', '>6', 'Total', 'Any']]
            df_filtered_cod = df_filtered.reset_index().rename({'index': 'Codi'}, axis = 1)
            df_filtered_cod['Codi'] = df_filtered_cod['Codi'] + 1
            data = data.append(df_filtered_cod)
        else:
            df_filtered = df.drop(['Unnamed: 9'], axis = 1)
            df_filtered_cod = df_filtered.reset_index().rename({'index': 'Codi'}, axis = 1)
            df_filtered_cod['Codi'] = df_filtered_cod['Codi'] + 1
            data = data.append(df_filtered_cod)
    
    indicador = Indicador(data, ['1996', '2001', '2011'], 'comarca', 'unitats')

'''
    Netejar dades referents als tipus d'habitatges (principals)
'''
def initPrin():
    path = os.path.join(data_path, 'habitants')

    nom_arxiu = 'Resi_Comarques_2011.csv'
    df = pd.read_csv(os.path.join(path,nom_arxiu))
    df['total_no_principals'] = df['total']
    df['any'] = '2011'
    df_ind = df.reset_index().rename({'index':'Codi'}, axis = 1)
    df_ind['Codi'] = df_ind['Codi'] + 1
    data = df_ind.drop(['total'], axis = 1)

    indicador = Indicador(data, '2011', 'comarca', 'unitats')

def initTin(nivell):
    path = os.path.join(data_path, 'tinenSa')
    
    nom_arxiu = 'Resi_' + nivell + '_2011.csv'
    df = pd.read_csv(os.path.join(path,nom_arxiu), index_col=False)
    df['Codi'] = df['Codi'].astype(str)

    #eliminem aquestes dues columnes pq no tenen gaire info.
    if nivell == 'municipi':
        df = df.drop(['Cedit gratis o a baix preu', 'Altres formes'], axis = 1)
    
    data = df.copy()
    
    indicador = Indicador(data, '2011', nivell, 'unitats')
    




def initResidencial():

    dimensio = Dimensio()

#Antiguitat

    antiguitat_com = initAnt('comarca') 
    dimensio.afegirIndicador('Antiguitat_Comarques', antiguitat_com)

    antiguitat_mun = initAnt('municipi') 
    dimensio.afegirIndicador('Antiguitat_Municipis', antiguitat_mun)

#Demanda 
    demanda = initDem()
    dimensio.afegirIndicador('Demanda', demanda)

#Habitants per habitatge

    habitants = initHab()
    dimensio.afegirIndicador('Habitants_Per_Habitatge', habitants)

#Habitantges principals

    principals = initPrin()
    dimensio.afegirIndicador('Habitatges_Principals', principals)

#Tinença

    tinenSa_com = initTin('comarca')
    dimensio.afegirIndicador('Tinença_Comarques', tinenSa_com)

    tinenSa_mun = initTin('municipi')
    dimensio.afegirIndicador('Tinença_Municipis', tinenSa_mun)
    


