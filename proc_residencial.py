import os
import pandas as pd
from dimensio import Dimensio
from indicador import Indicador

data_path = os.path.join('dades','residencials')

'''
    Netejar dades referents a l'any de creació dels edificis (antiguitat)
'''

def initAnt():
    path = os.path.join(data_path, 'antiguitat')

    nom_arxiu = 'Resi_municipi_2002_2011.csv'
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

    indicador = Indicador(data, range(2002,2011), 'municipi', 'unitats')

    return indicador


'''
    Netejar dades referents a la demanda de habitatges socials per anys (demanda)
'''

def initDem():
    path = os.path.join(data_path, 'demanda')

    nom_arxiu = 'Resi_comarca_2018_2012.csv'
    df = pd.read_csv(os.path.join(path,nom_arxiu), index_col=False, error_bad_lines=False, encoding='utf-8')
    #df = pd.read_csv('dades\\residencials\\demanda\\Resi_comarca_2018_2012.csv', index_col=False, error_bad_lines=False)
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

    return indicador

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

    return indicador

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

    return indicador


'''
    Netejar dades referents a la tinença (tinença)
'''

def initTin():
    path = os.path.join(data_path, 'tinenSa')
    
    nom_arxiu = 'Resi_municipi_2011.csv'
    df = pd.read_csv(os.path.join(path,nom_arxiu), index_col=False)
    df['Codi'] = df['Codi'].astype(str)

    #eliminem aquestes dues columnes pq no tenen gaire info.
    df = df.drop(['Cedit gratis o a baix preu', 'Altres formes'], axis = 1)
    
    data = df.copy()
    
    indicador = Indicador(data, '2011', 'municipi', 'unitats')

    return indicador


'''
    Netejar dades referent als tipus de residencia (tipus)
'''

def initTip():
    path = os.path.join(data_path, 'tipus') 

    nom_arxiu = 'Resi_2014_2020.csv'
    df = pd.read_csv(os.path.join(path,nom_arxiu))

    df_years = df[['Any']]
    df_years_ = pd.concat([df_years] * 9, ignore_index=True).reset_index() 

    df_values = df.drop(['Any'], axis = 1)

    all_values = []
    for column in df_values:
        this_column_values = df_values[column].tolist()
        all_values += this_column_values

    one_column_df = pd.DataFrame(all_values).reset_index().rename({0:'Values'}, axis = 1)

    data = df_years_.merge(one_column_df).drop(['index'], axis = 1)

    indicador = Indicador(data, range(2014,2020), 'altre', 'milers')

    return indicador

'''
    Netejar dades referent a la produccií inmobiliaria (producció)
'''

def initPro():
    path = os.path.join(data_path, 'antiguitat')

    nom_arxiu = 'Resi_municipi_2002_2011.csv'
    df = pd.read_csv(os.path.join(path,nom_arxiu), index_col=False, error_bad_lines=False)
    
    #calculamos los % de producció inmobiliaria per municipi
    y = ['2002', '2003', '2004', '2005', '2006', '2007','2008','2009', '2010', '2011']
    df_aux = pd.DataFrame()
    for pos in range(0,9):
        df_aux[y[pos+1]] =  round((((df[y[pos+1]] / df[y[pos]]) - 1) * 100),2)
    df_aux_T = df_aux.T

    all_values = []
    for column in df_aux_T:
        this_column_values = df_aux_T[column].tolist()
        all_values += this_column_values

    one_column_df = pd.DataFrame(all_values).reset_index().rename({0:'Values'}, axis = 1)

    years = pd.DataFrame(['2003', '2004', '2005', '2006', '2007','2008','2009', '2010', '2011'])
    df_city = df[['Codi', 'Literal']]
    df_city_ = pd.concat([df_city] * 9)
    df_city_sort = df_city_.sort_values(['Literal']).reset_index().reset_index().drop(['index'], axis = 1).rename({'level_0':'index','Literal':'Municipi'}, axis = 1)
    df_years = pd.concat([years] * len(df_city.T.columns)).reset_index().reset_index().drop(['index'], axis = 1).rename({'level_0':'index', 0:'Any'}, axis =1)
    
    df_city_years = df_city_sort.merge(df_years)

    data = df_city_years.merge(one_column_df).drop(['index'], axis = 1)

    indicador = Indicador(data, range(2003,2011), 'municipi', 'percentatge')

    return indicador



def initResidencial():

    dimensio = Dimensio()

#Antiguitat

    antiguitat = initAnt() 
    dimensio.afegirIndicador('Antiguitat Edificis', antiguitat)


#Demanda 
    demanda = initDem()
    dimensio.afegirIndicador('Demanda Social', demanda)

#Habitants per habitatge

    habitants = initHab()
    dimensio.afegirIndicador('Habitants per Habitatge', habitants)

#Habitantges principals

    principals = initPrin()
    dimensio.afegirIndicador('Habitatges Principals', principals)

#Tinença

    tinenSa_mun = initTin()
    dimensio.afegirIndicador('Tinença', tinenSa_mun)

#Tipus (milers)

    tipus = initTip()
    dimensio.afegirIndicador('Tipus Habitatges', tipus)

#Producció immobiliaria

    produccio = initPro()
    dimensio.afegirIndicador('Produccio Inmobiliaria', produccio)

    
    


