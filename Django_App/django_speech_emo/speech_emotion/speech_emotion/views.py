import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from moviepy.editor import VideoFileClip,AudioFileClip
import numpy as np
import json
import librosa
from tensorflow.keras.models import load_model
inf_model = load_model('models/all_speech_recog.h5')
tr_mean = np.load('models/tr_mean.npy')
tr_std = np.load('models/tr_std.npy')

@csrf_exempt
def upload_video(request):
    if request.method =='POST' and request.FILES.get('video'):
        video = request.FILES['video']
        video_path = f'media/video.mp4'  #f'media/{video.name}'
        audio_path = f'media/audio.mp3'   #video_path.rsplit('.', 1)[0] + '.mp3'
        with open(video_path, 'wb+') as destination:
            for chunk in video.chunks():
                destination.write(chunk)
        extract_audio(video_path, audio_path)

        # Clean up the temporary video file
        #os.remove(video_path)

        emotion_data = prediction1(audio_path)
        return render(request, 'analytics.html', {
            'emotion_data': json.dumps(emotion_data),  # Pass the emotion data as JSON
        })
    
    else:
        return render(request, 'upload.html')
    

def extract_audio(video_path, audio_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()
    video_clip.close()

def resize_array(array):
    new_matrix = np.zeros((30,150))   
    for i in range(30):               
        for j in range(150):          
            try:                                
                new_matrix[i][j] = array[i][j]
            except IndexError:                  
                pass
    return new_matrix


def inf(audio_path):
    z, sz = librosa.load(audio_path, sr=16000)
    mfc=librosa.feature.mfcc(y=z, sr=sz, fmin=50, n_mfcc=30)
    rez_mfc=resize_array(mfc)
    rez_mfc=np.array(rez_mfc)
    mfcc_standardized = (rez_mfc - tr_mean) / tr_std
    mfcc_standardized = mfcc_standardized[..., np.newaxis]
    mfcc_standardized = mfcc_standardized[np.newaxis, ...]
    predictions = inf_model.predict(mfcc_standardized)
    predicted_emotion = np.argmax(predictions, axis=1)[0]
    emotion_map = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}
    predicted_emotion_label = emotion_map[predicted_emotion]
    return(predicted_emotion_label)

def prediction1(audio_path):
    audio = AudioFileClip(audio_path)
    audio_duration = audio.duration
    start_time = 0
    segment_duration = 3  
    output_dir = "./media"
    dict={}
    while start_time < audio_duration:
        end_time = min(start_time + segment_duration, audio_duration)
        segment = audio.subclip(start_time, end_time)
        segment_file = os.path.join(output_dir, f"segment.wav")
        segment.write_audiofile(segment_file, codec='pcm_s16le')
        prediction = inf(segment_file)
        print(f"{start_time}:{end_time} => {prediction}")
        dict[f"{start_time}:{end_time}"]=prediction
        start_time += segment_duration

    # Clean up: Close the audio file
    audio.close()
    return dict