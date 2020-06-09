#!/bin/sh

(cd ~/Documents/image_segmentation/original/ny && date '+%Y-%m-%d_%H.%M'_no.jpg | xargs wget http://96.56.250.139:8200/jpg/1/image.jpg -O) & (cd ~/Documents/image_segmentation/original/no && date '+%Y-%m-%d_%H.%M'_no.jpg | xargs wget http://82.194.220.89:82/jpg/1/image.jpg -O)
