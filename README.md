# Generative Adversarial Networks - Drum Pattern Generation
I love listening metal music, and especially black metal. In this project, I tried to generate similar drum patterns of my whole time favorite black metal drummer Maciej Kowalski aka Darkside from MGŁA and Kriegsmaschine. In order to achieve this, Generative Adversarial Networks(GANs) are used. This project covers the following steps:
* Data Collection
* Data Preprocessing
* Model Training

You can listen couple of generated tracks by following this [link](https://soundcloud.com/oemer-faruk-kolcak/sets/ai-generated-darkside-drums).
## Data Collection
Based on my researches and similar projects made by others, midi files are the best option for this task. They are easy to work with and there are various python libraries to work on. Therefore, I searched through the internet to find midi files for MGŁA and Kriegsmaschine, but I could not find one single file since they are not that popular band. I had to find a different way, and one solution came to my mind. There is a website called [Ultimate-Guitar](https://www.ultimate-guitar.com/) where people transcript the songs and post guitar pro tabs. I downloaded the tabs of 14 different tracks from MGŁA and Kriegsmaschine, and converted to midi files from Guitar Pro 7 application. There could be minor mistakes, since the tabs are not published by original composers. In overall, they seem to be very accurate. 
## Data Preprocessing
