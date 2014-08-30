# Basic Web Services Example

# import the client libraries
import gdata.youtube
import gdata.youtube.service

# YouTubeService() used to generate the object so that
# we can comunicate with the YouTube API
youtube_service = gdata.youtube.service.YouTubeService()

# prompt the user to enter the YouTube User ID
playlist = raw_input("Please enter the user ID: ")

# setup the actual API Call
url = "http://gdata.youtube.com/feeds/api/users/"
playlist_url = url + playlist + "/playlists"

# Retrieve YouTube playlist
video_feed = youtube_service.GetYouTubePlaylistVideoFeed(playlist_url)

print "\nPlaylists for " + str.format(playlist) + ":\n"

# display each playlist to screen
for p in video_feed.entry:
    print p.title.text

#print video_feed
