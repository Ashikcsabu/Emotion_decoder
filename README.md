<h1>Emotion Decoder</h1>
   <p>The "Speech Emotion Decoder." It’s an advanced tool that decodes emotions purely from audio. The backbone of this project is a custom-built deep learning model, which I trained using popular audio datasets like RAVDESS, TESS, and SAVEE. These datasets feature the voices of native English speakers, representing a wide range of emotions. </p>
   <p>I created a convolutional neural network that predicts emotional labels from audio input by breaking down the audio file into smaller chunks. We then generate a spectrogram using Fourier transform and extract something called MFCCs—Mel Frequency Cepstral Coefficients. These are a set of features that describe the shape of the audio signal’s spectral envelope and then predict the emotion label for each 3 sec audio chunks.</p>

   
https://github.com/user-attachments/assets/3f9d8887-5ac4-4b04-b3c9-256f32e2c78a

<h1>Website</h1>

**🌐  [Emotion Decoder Guides](https://ashikcsabu.github.io/Emotion_decoder_guide/)** — Visit the documentation website to understand the theoretical aspects of this project.

<h1>Dataset Links</h1>

➢ RAVDESS - **[Click Here](https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio)**

➢ SAVEE - **[Click Here](https://www.kaggle.com/datasets/barelydedicated/savee-database)**

➢ TESS - **[Click Here](https://www.kaggle.com/datasets/ejlok1/toronto-emotional-speech-set-tess)**

<h1>How to Implement Emotion decoder on your local</h1>

➢ **STEP 1 :** 

Download the repository zip file.

https://github.com/user-attachments/assets/edebf3b6-12c2-47b3-8de1-2c886e1cf9a1

<h3>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OR</h3>

clone the repository to your local.

```bash
 git clone https://github.com/Ashikcsabu/Emotion_decoder.git
```

➢ **STEP 2 :**

Switch to the app directory
```bash
cd Emotion_decoder-Emotion_decoder\Django_App\django_speech_emo
```

➢ **STEP 3 :**

Create a virtual environment in the app directory for that execute the following commands on terminal.
```bash
py -m venv .venv
```
After creating the virtual environment ACTIVATE the virtual environment .
```bash
cd .venv/Scripts
```
after switching to the Scripts type `activate.bat` and hit `ENTER`.

This will activate the virtual environment and you can see `(venv)` on your command line.

➢ **STEP 4 :**

Installing the requirements file to the virtual environment.

```bash
pip install -r requirements.txt
```

This will install all required libraries to the venv.

➢ **STEP 5 :**

After that switch to the main app `"speech_emotion"` directory. 
```bash
Emotion_decoder-Emotion_decoder/Django_App/django_speech_emo/speech_emotion
```

➢ **STEP 6 :**

Run the server using the following command.

```bash
py manage.py runserver
```

This will start the server on your local.

![image](https://github.com/user-attachments/assets/23478dfe-547a-4f7d-9709-c6fd285b450e)

`ctrl`+`click` on the localhost IP to start the website on your local machine!

