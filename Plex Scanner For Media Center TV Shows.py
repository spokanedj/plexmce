import sys         #
import os          #
import os.path     #
import time        # 
import string      #
import re          # RegexPython
                   # result = re.findall(sourcestring, searcharray());
                   # result = re.match(sercharray(), sourcestring, re.IGNORECASE)
                   # result = re.sub(sourcestring, sercharray(), substringresulting)
                   # result = re.search(sercharray(), sourcestring, re.IGNORECASE)
          
import Media       # Master container for found Media.

#VIDEO
import VideoFiles  # Search for Video files.
                   # VideoFiles.Scan(path, files, mediaList, subdirs, root)
import Stack
import Utils

#PHOTO
import Filter
import PhotoFiles  # Search for Photo files.
                   # PhotoFiles.Scan(path, files, mediaList, subdirs, root)

#MUSIC
import AudioFiles  # Search for Audio files.
                   # AudioFiles.Scan(path, files, mediaList, subdirs, root)

import ID3, ID3v2
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
from mutagen.easyid3 import EasyID3
from mutagen.easymp4 import EasyMP4
from mutagen.asf import ASF

import logging
logging.basicConfig(filename='C:\Users\dale\AppData\Local\Plex Media Server\Scanners\Series\Plex Scanner For Media Center TV Shows.log',level=logging.DEBUG)

##try:
##    import win32com.client
##except Exception as e:
##    logging.exception(e)    

# Scans through files, and add to the media list.
def Scan(path, files, mediaList, subdirs, language=None, root=None, **kwargs):

  if (path != "TempRec"):
##    logging.debug((logTime(), "win32com loaded: "))
##
##    # Build the Col # <-> Column Name
##    targetcols = ['Title', 'Genre', 'Rating', 'Length', 'Subtitle', 'Parental rating', 'Episode name', 'Broadcast date', 'Program description', 'Station call sign']
##    colnames = []
##    colnumbs = []
##
##    logging.debug((logTime(), "columns built: "))
##
##    sh=win32com.client.gencache.EnsureDispatch('Shell.Application',0)
##    mypath = "c:\\users\\public\\recorded tv"
##    ns = sh.NameSpace(mypath)
##
##    for colnum in range(0,1024):
##        colname=ns.GetDetailsOf(None, colnum)
##        if colname:
##            for t in targetcols:
##                if t == colname:
##                    colnames.append(colname)
##                    colnumbs.append(colnum)
##
##    logging.debug((logTime(), "columns loaded: "))

    logging.debug((logTime(), "--------------------------------------- TV Start scanning of files in folder: ", path))
    
    # Filter out bad stuff and duplicates.
    VideoFiles.Scan(path, files, mediaList, subdirs, root)

    # Add all the videos to the list.
    for fullfilepath in files:
      if fullfilepath.endswith(".wtv"):
    
        file = os.path.basename(fullfilepath)
                   
        parts = file.split('_');
        title = parts[0];
        ep_title = parts[0] + ' ' + parts[3] + '/' + parts[4];
        channelsign = parts[1];
        year = int(parts[2]);
        month = int(parts[3]);
        day = int(parts[4]);

        ep = (year-2000)*(12*31)+(31*month)+(day);
        season = 1;
        
        logging.debug((logTime(), " Path: ", path))
        logging.debug((logTime(), " FullPath: ", fullfilepath))
        
        logging.debug((logTime(), " File: ", file))
        logging.debug((logTime(), " Tilte: ", title))
        logging.debug((logTime(), " Year: ", year))
        logging.debug((logTime(), " Season: ", season))
        logging.debug((logTime(), " Episode: ", ep))

        # video (Movie)
##        video = Media.Movie(title, year)
##        video.source = VideoFiles.RetrieveSource(fullfilepath) 
##        video.parts.append(fullfilepath) 
##        mediaList.append(video)

        tv_show = Media.Episode(title, 0, ep, ep_title, year)
        #tv_show.display_offset = (ep-episode)*100/(endEpisode-episode+1)
        #tv_show.source = VideoFiles.RetrieveSource(fullfilepath) 
        tv_show.parts.append(fullfilepath)
        tv_show.released_at = '%d-%02d-%02d' % (year, month, day)
        mediaList.append(tv_show)


        logging.debug((logTime(), "---------------------------------------"))
        logging.debug((logTime(), ""))
        
def Update(path, files, mediaList, subdirs, language=None, root=None, **kwargs):
  logging.debug((logTime(), "Start update of files in folder: ", path))
    
  
def logTime ():
 return time.strftime("%H:%M:%S")
 
    
