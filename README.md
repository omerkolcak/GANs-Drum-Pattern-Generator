# Generative Adversarial Networks - Drum Pattern Generation
I love listening metal music, and especially black metal. In this project, I tried to generate similar drum patterns of my whole time favorite black metal drummer Maciej Kowalski aka Darkside from MGŁA and Kriegsmaschine. In order to achieve this, Generative Adversarial Networks(GANs) are used. This project covers the following steps:
* Data Collection
* Data Preprocessing
* Model Training
* Convert Images to Midi

You can listen couple of generated tracks by following this [link](https://soundcloud.com/oemer-faruk-kolcak/sets/ai-generated-darkside-drums).
## Data Collection
Based on my researches and similar projects made by others, midi files are the best option for this task. Midi files are symbolic music which means it is a collection of note events arrenged in different instruments over time. They are easy to work with and there are various python libraries to work on. Therefore, I searched through the internet to find midi files for MGŁA and Kriegsmaschine, but I could not find one single file since they are not that popular band. I had to find a different way, and one solution came to my mind. There is a website called [Ultimate-Guitar](https://www.ultimate-guitar.com/) where people transcript the songs and post guitar pro tabs. I downloaded the tabs of 14 different tracks from MGŁA and Kriegsmaschine, and converted them to midi files from Guitar Pro 7 application. There could be minor mistakes, since the tabs are not published by original composers. In overall, they seem to be very accurate. 
## Data Preprocessing
Now that we have the midi files, each midi file should be converted to image represantion of the track. This requires the quantization. By appling quantization, we simply make sure that every note gets mapped into the time grid. After quantization, images can be generated for every track. Below image is an example from the dataset. <br/>
![alt text for screen readers](readme-images/dataset_sample.png "Dataset Sample")
## Model Training
## Image to Midi
