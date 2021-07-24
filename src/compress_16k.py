import soundfile as sf
from glob import glob

gtzan = glob("../dataset/gtzan16k/*/*")
"""for audio in gtzan:
    wav, sr = sf.read(audio)
    sf.write(audio.replace("gtzan", "gtzan16k"), wav, 16000)"""


f = open("../dataset/gtzan16k.tsv", "w")
for audio in gtzan:
    wav, sr = sf.read(audio)
    aux = audio.split("dataset/")[1]
    f.write(f"{aux}\t{len(wav)}\n")
