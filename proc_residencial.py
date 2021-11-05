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

def initResidencial():

    dimensio = Dimensio()

#Antiguitat
    antiguitat_Com = initAnt('comarca') 
    dimensio.afegirIndicador('Antiguitat_Comarques', antiguitat_Com)

    antiguitat_Mun = initAnt('municipi') 
    dimensio.afegirIndicador('Antiguitat_Municipis', antiguitat_Mun)

#Demanda 
    demanda_Com = initDem()
    dimensio.afegirIndicador('Demananda_Comarques', demanda_Com)



