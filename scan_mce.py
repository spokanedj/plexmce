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

import logging
logging.basicConfig(filename='C:\Users\dale\AppData\Local\Plex Media Server\Scanners\Movies\Testlog.log',level=logging.DEBUG)

import win32com.client
sh=win32com.client.gencache.EnsureDispatch('Shell.Application',0)

# Build the Col # <-> Column Name
targetcols = ['Title', 'Genre', 'Rating', 'Length', 'Subtitle', 'Parental rating', 'Episode name', 'Broadcast date', 'Program description', 'Station call sign']
colnames = []
colnumbs = []

for colnum in range(0,1024):
    colname=ns.GetDetailsOf(None, colnum)
    if colname:
        for t in targetcols:
            if t == colname:
                colnames.append(colname)
                colnumbs.append(colnum)

# Scans through files, and add to the media list.
def Scan(path, files, mediaList, subdirs, language=None, root=None, **kwargs):
   
  logging.debug((logTime(), "Start scanning of files in folder: ", path))
  
  VideoFiles.Scan(path, files, mediaList, subdirs, root)

  # Add all the files
  for fullfilepath in files:
    file = os.path.basename(fullfilepath)
    (title, ext) = os.path.splitext(file)

   print(file)
    # video (Movie)
    # video.guid = "" move part identification
    # (name, year) = VideoFiles.CleanName(file)
    # video = Media.Movie(name, year)
    # tv_show = Media.Episode(name, season, ep, '', year)
    # video.source = VideoFiles.RetrieveSource(file)
    # video.parts.append(fullfilepath) # Join movie parts for continuous playback
        
        
    # video (Media Center)

##  C:\Users\Public\Recorded TV\A to Z_KHQDT_2014_10_09_21_30_03.wtv
##	 16 Genre : Comedy;Series
##	 19 Rating : Unrated
##	 21 Title : A to Z
##	 27 Length : 00:32:53
##	 204 Subtitle : B Is for Big Glory
##	 240 Parental rating : TV-PG
##	 267 Episode name : B Is for Big Glory
##	 271 Broadcast date : ‎10/‎9/‎2014 ‏‎12:00 AM
##	 272 Program description : Neithe...

    mce_name = ns.GetDetailsOf(file, 21)
    mce_episode = ns.GetDetailsOf(file, 267)
    mce_description = ns.GetDetailsOf(file, 272)
    mce_date = ns.GetDetailsOf(file, 271)

    mce_date2 = datetime.strptime(mce_date, "%m/%d/%Y %H:%M %p")

    print (mce_title)
    print (mce_episode)
    print (mce_description)
    print (mce_date)
    print (mce_date2)

##    (name, year) = VideoFiles.CleanName(path)    
##    logging.debug((logTime(), " CleanName: ", name, year))
##
##    match = re.search(episode_regex[-1], file, re.IGNORECASE)
##    if match:    
##      ep = int(match.group('ep')) 
##      logging.debug((logTime(), " Found ep in file: ", ep))
##    
##    match = re.search(year_regex[-1], file, re.IGNORECASE)
##    if match:    
##      year = int(match.group('year'))
##      logging.debug((logTime(), " Found year in file: ", year))

    video = Media.Episode(mce_title, '2014', mce_episode, path, Null)
    #tv_show = Media.Episode(name, season, ep, '', year)
    video.display_offset = mce_episode
    video.parts.append(fullfilepath)
    mediaList.append(video)

    tv_show = Media.Episode(mce_name, mce_date[0:9], 'ep1', mce_episode, mce_date[0:9])      
    tv_show.released_at = '%d-%02d-%02d' % (int(year), int(month), int(day))
    tv_show.parts.append(filepath)
    mediaList.append(tv_show)

        
def Update(path, files, mediaList, subdirs, language=None, root=None, **kwargs):
  logging.debug((logTime(), "Start update of files in folder: ", path))
    

def logTime ():
 return time.strftime("%H:%M:%S")
 
    
