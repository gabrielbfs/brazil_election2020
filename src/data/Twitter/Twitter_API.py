# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:07:21 2020

@author: gabrielbustamante
"""
import sys
sys.path.append('D:/Desktop/4.DataScience/0.courses/2.ND_DS/1.project Brazil_Election/brazil_election2022/src/data/Twitter')

import tweepy
from DataTwitter_json import DataTwitter_json

from sqlalchemy import create_engine, insert, Table, MetaData

import time

import pandas as pd


class Twitter_API(DataTwitter_json):
    
    def __init__(self, database, table, keys):
        print('-'*10)
        print('connected to mysql')
        
        self.path = 'mysql+pymysql://root:root@localhost:3306/' + database
        self.engine = create_engine(self.path)
        self.engine.connect()
        self.table = Table(table, MetaData(), autoload=True, autoload_with=self.engine)
        print('connected to api')
        self.auth = tweepy.OAuthHandler(keys['TWITTER_APP_KEY'], keys['TWITTER_APP_SECRET'])
        self.auth.set_access_token(keys['TWITTER_KEY'], keys['TWITTER_SECRET'])
        self.api = tweepy.API(self.auth, retry_count=50, retry_delay=300, timeout=180, wait_on_rate_limit=True)
        print('-'*10)
        
    
    '''
    def candidate_id(self, candidate):
        user = api.get_user(screen_name=candidate)
        return user.id
    
    def user_screen_name(self, user_id):
        user = api.get_user(id=user_id)
        return user.screen_name
    
    def candidate_total_followers(self, candidate):
        user = api.get_user(screen_name=candidate)  
        # user.friends_count
        return user.friends_count
    '''
    
    def limit_errors(cursor):
        while True:
            try:
                yield cursor.next()
            except tweepy.RateLimitError:
                print("\nRateLimitError")
                print("-"*10, end='')
                time.sleep(5*60)
                print("\n")
            
            except tweepy.TweepError:
                print("\nTweepError")
                print("-"*10, end='')
                time.sleep(3*60)
                print("\n")
            
            except StopIteration:
                return
                

    def cursor_search(self, screen_name, candidate, since, until):
        print("\n connected to cursor search")
        print("-"*10)
        for data in Twitter_API.limit_errors(tweepy.Cursor(self.api.search,  
                                  exclude_replies=False, 
                                  tweet_mode='extended', q=screen_name, 
                                  since=since, until=until).items()):
                     
            stmt = DataTwitter_json()
            stmt = stmt.set_stmt(data._json)
            
            stmt['candidate'] = candidate
            
            stmt = insert(self.table).values(stmt)
            try:
                self.engine.execute(stmt)
            except:
                pass
            time.sleep(0.5)
                
        
    """ # must adapt to Brazilian cities
    def cursor_search_geocode(self, screen_name, candidate, since, until):
        print("\n connected to cursor search geocode")
        print("-"*10)
        cities = pd.read_csv('C:/Users/gabri/Desktop/us elections/us_cities-889.csv', sep=';')
        
        for i in range(len(cities)):
            city = cities['city_ascii'].loc[i]
            state_id = cities['state_id'].loc[i]
            state_name = cities['state_name'].loc[i]
            
            lat = cities['lat'].loc[i]
            lng = cities['lng'].loc[i]
            geocode = str(lat) + ',' + str(lng) + ',10km'
            
            print('\r{}: {} - {}               \n'.format(i, state_id, city), end='')

            for data in Twitter_API.limit_errors(tweepy.Cursor(self.api.search,  
                                      exclude_replies=False, 
                                      tweet_mode='extended', q=screen_name, 
                                      since=since, until=until, 
                                      geocode=geocode).items()):
                         
                stmt = DataTwitter_json()
                stmt = stmt.set_stmt(data._json)
                
                stmt['candidate'] = candidate
                stmt['state_id'] = state_id
                stmt['state_name'] = state_name
                stmt['city'] = city
                
                stmt = insert(self.table).values(stmt)
                try:
                    self.engine.execute(stmt)
                except:
                    pass
                time.sleep(0.25)
     """                   
                                        

                
                
    
    def cursor_timeline(self, screen_name, candidate, since, until):
        print("\n connected to cursor timeline")
        print("-"*10)
        for data in Twitter_API.limit_errors(tweepy.Cursor(self.api.search,  
                                             exclude_replies=False, 
                                             tweet_mode='extended', q=screen_name, 
                                             since=since, until=until).items()):
                                 
            stmt = DataTwitter_json()
            stmt = stmt.set_stmt(data._json)
            
            stmt['candidate'] = candidate
            
            stmt = insert(self.table).values(stmt)
            try:
                self.engine.execute(stmt)
            except:
                pass
            time.sleep(1.05)
                                    
    
    
