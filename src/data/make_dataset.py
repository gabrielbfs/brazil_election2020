# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

import os
path = os.getcwd()
path = path[:path.find('brazil_election2022')]


presidentApproval_url = 'https://data.jota.info/aprovacao/dados/Popularidade.csv'

raw_filepath = path + 'brazil_election2022\\data\\raw\\'
processed_filepath = path + 'brazil_election2022\\data\\processed\\'


def presidentApproval_download(url=presidentApproval_url):
    """ Download data from url - save immutable .csv file
    """
    
    polls = pd.read_csv(url, parse_dates=['DATAFIM'])
    polls.to_csv(raw_filepath+'president_polls2020.csv', index=False)
    
    return polls


def presidentApproval_preprocessig(raw_filepath=raw_filepath, processed_filepath=processed_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    
    # download president_polls.csv dataset and save to raw folder (immutable data)
    polls = presidentApproval_download(url=presidentApproval_url)
    
    # filter 2020 cycle US President: Biden x Trump
    cols_astype = {'POSITIVA':float, 'REGULAR':float, 'NEGATIVA':float, 'NS.NR':float, 'ERRO':float, 'IC':float, 'N':float}
    cols = list(cols_astype.keys())
    polls[cols] = polls[cols].replace({' ':np.nan, '':np.nan})
    polls = polls.astype(cols_astype)
    polls.columns = polls.columns.str.lower()

    # only select polls with Trump and Biden as candidates
    polls = polls[~polls['empresa'].isna()]
    polls = polls[polls['tipo'] == 'Avaliação do governo federal']
    
    # edit data and create new features
    for presidente in polls['presidente'].unique():
        df = polls[polls['presidente'] == presidente]
        for empresa in df['empresa'].unique():
            mean_n = df[df['empresa'] == empresa]['n'].mean()
            if pd.isna(mean_n):
                mean_n = df['n'].mean()
            if pd.isna(mean_n):
                mean_n = polls['n'].mean()
            mean_n = int(mean_n)
            polls.loc[(polls['empresa'] == empresa) & 
                      (polls['presidente'] == presidente), 'n'] = polls.loc[(polls['empresa'] == empresa) & 
                                                                            (polls['presidente'] == presidente), 'n'].fillna(mean_n)

    polls['ufs'] = polls['ufs'].fillna(0).astype(str)
    polls['empresa_avaliaca'] = polls['empresa'].apply(lambda x: 2. if x in ['Ibope', 'Datafolha'] else 1.)
    polls['peso'] = polls['empresa_avaliaca']*polls['n']

    # save processed data to processed folder
    polls.to_csv(processed_filepath+'presidentApproval_processed.csv', index=False)
    
    

if __name__ == '__main__':
    
    general_election_polls2020_download(raw_filepath, processed_filepath)
    presidentApproval_preprocessig(raw_filepath=raw_filepath, processed_filepath=processed_filepath)
