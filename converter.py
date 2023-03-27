from os import path
from pydub import AudioSegment

# files                                                                         
src = "./human_voice/hi.mp3"
dst = "./human_voice/Hi.wav"

# convert wav to mp3                                                            
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")