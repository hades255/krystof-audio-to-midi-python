import os
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from pydub import AudioSegment
from audio_to_midi import audio_to_midi

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'wav'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Convert audio file to WAV if needed
            if file.filename.lower().endswith('.wav'):
                wav_filename = filename
            else:
                wav_filename = f"{os.path.splitext(filename)[0]}.wav"
                audio = AudioSegment.from_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                audio.export(os.path.join(app.config['UPLOAD_FOLDER'], wav_filename), format='wav')
            # Convert WAV file to MIDI
            midi_filename = f"{os.path.splitext(wav_filename)[0]}.midi"
            audio_to_midi(os.path.join(app.config['UPLOAD_FOLDER'], wav_filename), os.path.join(app.config['UPLOAD_FOLDER'], midi_filename))
            return midi_filename
    return '''
    <!doctype html>
    <title>Upload WAV File</title>
    <h1>Upload WAV File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''

@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run()
