# image_segmentation

This repository contains the toolbox for image segmentation, which is built primarily for the final project of the Computer Vision course at TU Delft. The project concerns the classification of parking space occupancy detection using a simplified AlexNet, or mAlexNet. Please refer to CV_Project for more details.

### Setting up
From a website called Inescam, we download snapshots of a surveillance camera in a parking lot in Trondheim, Norway using the shell script `get_img.sh`. The file can be added to `cron` to schedule the execution of the file. In this dataset, a time interval of 15 minutes was set to download the snapshot. The downloaded file is named after the following format: 2020-06-08_13.30_no.jpg, as in 8th June 2020 at 13:30, Norway. 


### Requirements
```
python3
matplotlib
opencv-python
pickle
```
