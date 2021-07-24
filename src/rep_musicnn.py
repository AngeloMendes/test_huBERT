from glob import glob
from numpy import save
from musicnn.extractor import extractor

wavs = glob(pathname="../dataset/gtzan/*/*")
for wav in wavs:
    taggram = extractor(wav, model='MTT_musicnn')[0]
    f = wav.split("dataset/")[1]
    f = f.split(".wav")[0]
    save(f"../representations/{f}.npy", taggram)
