# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 21:27:00 2020

@author: gabrielbustamante
"""

import sys
sys.path.append('D:/Desktop/4.DataScience/0.courses/2.ND_DS/1.project Brazil_Election/brazil_election2022/src/data/Twitter')

from Twitter_API import Twitter_API

from datetime import datetime, timedelta
import time

from private import keys_v01 as private

import winsound


start = str(datetime.today().date() - timedelta(days=7))
end = str(datetime.today().date())


keys = {'TWITTER_APP_KEY':private['TWITTER_APP_KEY'], 
        'TWITTER_APP_SECRET':private['TWITTER_APP_SECRET'], 
        'TWITTER_KEY':private['TWITTER_KEY'], 
        'TWITTER_SECRET':private['TWITTER_SECRET']}

table = 'tweets_from'


candidates = {'Jair Bolsonaro':'from:jairbolsonaro'}

for candidate in candidates.keys():
    screen_name = candidates[candidate]
    print('\n')
    print('#'*25)
    print(candidate)
    print('start: {}\nend: {}'.format(start, end))

    at_candidate = Twitter_API(database='brazil_election', table=table, keys=keys)
    at_candidate.cursor_timeline(screen_name=screen_name, candidate=candidate, since=start, until=end)
    winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)

print('\n')
print('-'*25)
print('done')
winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
print('#'*25)
