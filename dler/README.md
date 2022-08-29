# DLer
_a simple download script using yt-dlp_

This script uses a list of urls to download multiple videos one by one. Just
create a simple text files containing the urls like:

```
https://www.youtube.com/watch?v=z7DgP8sgM1A
https://www.youtube.com/watch?v=sB7XIlN0kWU
```

Let's assume you saved that file with the filename _list_, you can now simply
issue:

```
@ dler -i list
```

If you want to download subtitles with the files:

```
@ dler -s -i list
```

If you want to download the files as audio only:

```
@ dler -a -i list
```

It's a simple script, as I told you.
