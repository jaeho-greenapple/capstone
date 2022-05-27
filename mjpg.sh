export STREAMER_PATH=/home/pi/mjpg_jackson/mjpg-streamer/mjpg-streamer-experimental
export LD_LIBRARY_PATH=$STREAMER_PATH
$STREAMER_PATH/mjpg_streamer -i "input_uvc.so -d /dev/video2" -o "output_http.so -p 8080 -w $STREAMER_PATH/www"
