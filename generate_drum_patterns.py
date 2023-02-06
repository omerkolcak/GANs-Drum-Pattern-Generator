import argparse
import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage, bpm2tempo
import numpy as np
import cv2 as cv
from tensorflow import keras

def generate_latent_points(latent_dim, n_samples):
    x_input = np.random.randn(latent_dim * n_samples)
    x_input = x_input.reshape(n_samples, latent_dim)
    return x_input

def image_to_midi(img,bpm=120,min_note=0):
    new_song = MidiFile()
    new_song.ticks_per_beat = 480
    meta_track = MidiTrack()
    new_song.tracks.append(meta_track)

    # Create meta_track, add neccessary settings.
    meta_track.append(MetaMessage(
        type='track_name', name='meta_track', time=0))
    meta_track.append(MetaMessage(type='time_signature', numerator=4, denominator=4,
                                  clocks_per_click=24, notated_32nd_notes_per_beat=8, time=0))
    meta_track.append(MetaMessage(type='set_tempo',
                                  tempo=bpm2tempo(bpm), time=0))
    
    print("tempo:",bpm2tempo(bpm))

    # drum_track
    drum_track = MidiTrack()
    new_song.tracks.append(drum_track)

    ticks_per_32note = 60 # ticks_per_beat / 8

    time_indices = []
    for i,col in enumerate(img.T):
        
        notes = (col==0).nonzero()[0]
        
        if len(notes) == 0:
            pass
        else:
            
            if len(time_indices) == 0:
                notes_from_last_message = 0
            else:
                notes_from_last_message = i - time_indices[-1]
            time_indices.append(i)
            
            for note_idx, n in enumerate(notes):
                time_passed = notes_from_last_message*ticks_per_32note if note_idx == 0 else 0
                drum_track.append(Message('note_on', channel=9, note=n+min_note, velocity=89,time=time_passed))
            
    return new_song

def generate_tracks(track_num,bpm,model_path):
    # define the notes used by darkside
    darkside_notes = [36, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 57, 59]
    # define the notes that should be deleted if the model fills these part
    delete_notes = [i-36 for i in range(36,61) if i not in darkside_notes]

    generator = keras.models.load_model(model_path)
    generator.compile()

    for idx in range(track_num):
        latent_points = generate_latent_points(50,1)
        # generate images
        X = generator.predict(latent_points)
        X = (X + 1) / 2.0 # unnormalize it
        
        img = np.array(X.reshape(25,256),dtype = np.uint8)
        img*= 255
        # delete the notes that are not used by Darkside
        img[delete_notes,:] = 255
        
        # save the generated image
        cv.imwrite(f"generated-tracks/track-{idx + 1}.png",img)
        
        # convert image to midi
        song = image_to_midi(img,bpm=bpm,min_note=36)
        # save the generated track
        song.save(f"generated-tracks/track-{idx + 1}.mid")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--track-nums', nargs='?', const=5, type=int)
    parser.add_argument('--bpm', nargs='?', const=100, type=int)
    parser.add_argument("--weights",nargs="?", const="models/model_5976.h5", type=str)

    args = parser.parse_args()

    number_of_tracks = args.track_nums
    bpm = args.bpm 
    model_path = args.weights

    generate_tracks(number_of_tracks,bpm,model_path)



