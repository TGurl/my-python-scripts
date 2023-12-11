#!/usr/bin/env bash

if [ $# -eq 0 ]
then
    echo 'No filename passed...'
    exit
fi

ffmpeg -y -hide_banner -loglevel error -stats \
    -video_size 1920x1080 -thread_queue_size 64 \
    -framerate 30 -f x11grab -draw_mouse 0 -i :0.0 \
    -f pulse -ac 2 -i default -crf 30 \
    -preset ultrafast -qp 0 -pix_fmt yuv444p \
    $1_`date '+%d%m%Y%H%M%S'`.mp4

