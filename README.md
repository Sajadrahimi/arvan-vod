# arvan-client
A python SDK for ArvanCloud API


# VOD
```
  from vod.vod import VOD
  
  vod = VOD('MY API KEY')
  channels = vod.get_channels()
  channel = next(filter(lambda t: t.description == 'my channels', channels))
  video = vod.get_videos(channel, "video name, a key word, etc")
```

To add video from url:
```
  vod.add_video(channel, "video title", video_url = "URL TO VIDEO")
```

To add video from file:
```
  uploaded_file_id = vod.request_upload(channel, "PATH TO FILE")
  vod.add_video(channel, "video title", file_id=uploaded_file_id)
```
