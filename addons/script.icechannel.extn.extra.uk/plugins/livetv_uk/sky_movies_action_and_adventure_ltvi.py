'''
    Ice Channel
'''

from entertainment.plugnplay.interfaces import LiveTVIndexer
from entertainment.plugnplay import Plugin
from entertainment import common

class sky_movies_action_and_adventure(LiveTVIndexer):
    implements = [LiveTVIndexer]
    
    display_name = "Sky Movies Action & Adventure"
    
    name = "sky_movies_action_and_adventure"
    
    other_names = "sky_movies_action_and_adventure,Sky Movies Action & Adventure"
    
    import xbmcaddon
    import os
    addon_id = 'script.icechannel.extn.extra.uk'
    addon = xbmcaddon.Addon(addon_id)
    img = os.path.join( addon.getAddonInfo('path'), 'resources', 'images', name + '.png' )
    
    regions = [ 
            {
                'name':'United Kingdom', 
                'img':addon.getAddonInfo('icon'), 
                'fanart':addon.getAddonInfo('fanart')
                }, 
        ]
        
    languages = [ 
        {'name':'English', 'img':'', 'fanart':''}, 
        ]
        
    genres = [ 
        {'name':'Movies', 'img':'', 'fanart':''} 
        ]
    
    addon = None
    
