#!/bin/sh

(cd ~/Documents/image_segmentation/original/de && date '+%Y-%m-%d_%H.%M'_de.jpg | xargs wget http://217.24.238.168:82/record/current.jpg -O) & (cd ~/Documents/image_segmentation/original/no &&  date '+%Y-%m-%d_%H.%M'_no.jpg | xargs wget http://82.194.220.89:82/jpg/1/image.jpg -O)
