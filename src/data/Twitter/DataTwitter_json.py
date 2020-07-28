# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 17:15:19 2020

@author: gabrielbustamante
"""

import pandas as pd
import time
from itertools import cycle

class DataTwitter_json():
    def __init__(self):
        self.__stmt = dict()
        
    def downloading(created_at):
        print('\r{}'.format(created_at), sep='', end='', flush=True)
        '''
        for frame in [' .', ' . .', ' . . .', '          ']:
            print('\rdownloading', frame, sep='', end='', flush=True)
            time.sleep(0.025)
        '''
        
    def set_stmt(self, all_data):
        
        # tweet info
        self.__stmt['tweet_id'] = all_data.get('id')
        self.__stmt['tweet_created_at'] = str(pd.to_datetime(all_data.get('created_at')))
        self.__stmt['tweet_full_text'] = all_data.get('full_text')
        self.__stmt['tweet_favorite_count'] = all_data.get('favorite_count')
        self.__stmt['tweet_retweet_count'] = all_data.get('retweet_count')
        self.__stmt['tweet_in_reply_to_screen_name'] = all_data.get('in_reply_to_screen_name')
        self.__stmt['tweet_in_reply_to_status_id'] = all_data.get('in_reply_to_status_id')
        self.__stmt['tweet_in_reply_to_user_id'] = all_data.get('in_reply_to_user_id')
        
        
        # user info
        if all_data.get('user') != None:
            self.__stmt['user_id'] = all_data.get('user').get('id')
            self.__stmt['user_name'] = all_data.get('user').get('name')
            self.__stmt['user_screen_name'] = all_data.get('user').get('screen_name')
            self.__stmt['user_created_at'] = str(pd.to_datetime(all_data.get('user').get('created_at')))
            self.__stmt['user_followers_count'] = all_data.get('user').get('followers_count')
            self.__stmt['user_friends_count'] = all_data.get('user').get('friends_count')
            self.__stmt['user_listed_count'] = all_data.get('user').get('listed_count')
            self.__stmt['user_statuses_count'] = all_data.get('user').get('statuses_count')
            self.__stmt['user_favorites_count'] = all_data.get('user').get('favourites_count')
        
        # retweet info
        if all_data.get('retweeted_status') != None:
            self.__stmt['retweeted_id'] = all_data.get('retweeted_status').get('id')
            self.__stmt['retweeted_created_at'] = str(pd.to_datetime(all_data.get('retweeted_status').get('created_at')))
            self.__stmt['retweeted_full_text'] = all_data.get('retweeted_status').get('full_text')
            self.__stmt['retweeted_favorite_count'] = all_data.get('retweeted_status').get('favorite_count')
            self.__stmt['retweeted_retweet_count'] = all_data.get('retweeted_status').get('retweet_count')
            if all_data.get('retweeted_status').get('user') != None:
                self.__stmt['retweeted_user_id'] = all_data.get('retweeted_status').get('user').get('id')
                self.__stmt['retweeted_user_name'] = all_data.get('retweeted_status').get('user').get('name')
                self.__stmt['retweeted_user_screen_name'] = all_data.get('retweeted_status').get('user').get('screen_name')
                self.__stmt['retweeted_user_created_at'] = str(pd.to_datetime(all_data.get('retweeted_status').get('user').get('created_at')))
                self.__stmt['retweeted_user_favorites_count'] = all_data.get('retweeted_status').get('user').get('favourites_count')
                self.__stmt['retweeted_user_followers_count'] = all_data.get('retweeted_status').get('user').get('followers_count')
                self.__stmt['retweeted_user_friends_count'] = all_data.get('retweeted_status').get('user').get('friends_count')
                self.__stmt['retweeted_user_statuses_count'] = all_data.get('retweeted_status').get('user').get('statuses_count')
                
        
        elif all_data.get('quoted_status') != None:
            self.__stmt['retweeted_id'] = all_data.get('quoted_status').get('id')
            self.__stmt['retweeted_created_at'] = str(pd.to_datetime(all_data.get('quoted_status').get('created_at')))
            self.__stmt['retweeted_full_text'] = all_data.get('quoted_status').get('full_text')
            self.__stmt['retweeted_favorite_count'] = all_data.get('quoted_status').get('favorite_count')
            self.__stmt['retweeted_retweet_count'] = all_data.get('quoted_status').get('retweet_count')
            if all_data.get('quoted_status').get('user') != None:
                self.__stmt['retweeted_user_id'] = all_data.get('quoted_status').get('user').get('id')
                self.__stmt['retweeted_user_name'] = all_data.get('quoted_status').get('user').get('name')
                self.__stmt['retweeted_user_screen_name'] = all_data.get('quoted_status').get('user').get('screen_name')
                self.__stmt['retweeted_user_created_at'] = str(pd.to_datetime(all_data.get('quoted_status').get('user').get('created_at')))
                self.__stmt['retweeted_user_favorites_count'] = all_data.get('quoted_status').get('user').get('favourites_count')
                self.__stmt['retweeted_user_followers_count'] = all_data.get('quoted_status').get('user').get('followers_count')
                self.__stmt['retweeted_user_friends_count'] = all_data.get('quoted_status').get('user').get('friends_count')
                self.__stmt['retweeted_user_statuses_count'] = all_data.get('quoted_status').get('user').get('statuses_count')
                
        DataTwitter_json.downloading(created_at=self.__stmt['tweet_created_at'])
        return self.__stmt