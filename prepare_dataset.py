# !pip install librosa==0.9.2 unidecode==1.3.6 tgt==1.4.4 pyworld==0.2.10
import os
import yaml
from yaml import CLoader as Loader, CDumper as Dumper
import librosa
import numpy as np
from scipy.io import wavfile
from tqdm import tqdm
import pandas as pd
from preprocessor import Preprocessor
from tqdm.auto import tqdm
import shutil
from utils import get_yaml_path, get_yaml_contents, write_yaml
import subprocess
import sys

tqdm.pandas()


def create_data_df(transcript_path, data_path, speaker_id=None):
    data_df = pd.read_csv(transcript_path, sep="|")
    data_df["wav_filename"] = data_df["wav_filename"].apply(
        lambda x: os.path.join(data_path, x)
    )
    if speaker_id:
        return data_df[data_df["client_id"] == speaker_id].reset_index(drop=True)
    return data_df


def create_dataset(transcript_path, data_path, speaker_id, out_path):
    data_df = create_data_df(
        transcript_path=transcript_path, data_path=data_path, speaker_id=speaker_id
    )
    data_df = data_df[:100]
    if os.path.isdir(out_path):
        shutil.rmtree(out_path)
    dst = os.path.join(out_path)
    os.makedirs(dst)
    for idx, row in tqdm(data_df.iterrows()):
        audio_source = str(row["wav_filename"])
        audio_dst = os.path.join(dst, audio_source.split("/")[-1])
        shutil.copy(audio_source, audio_dst)
        transcript_dst = audio_dst.replace("wav", "lab")
        with open(transcript_dst, "w") as f:
            f.write(row["transcript"])


def prepare_align(config, data_path=None):
    sampling_rate = config["preprocessing"]["audio"]["sampling_rate"]
    max_wav_value = config["preprocessing"]["audio"]["max_wav_value"]
    if data_path is None:
        data_path = config["path"]["corpus_path"]
    for filename in tqdm(os.listdir(data_path)):
        if filename.split(".")[-1] == "wav":
            wav_path = os.path.join(data_path, filename)
            wav, sr = librosa.load(wav_path, sr=sampling_rate)
            wav = wav / max(abs(wav)) * max_wav_value
            wavfile.write(wav_path, sampling_rate, wav.astype(np.int16))


DATASET_NAME = "CML_Polish"
DATASET_ROOT = "../cml-tts/"
TRAIN_PATH = DATASET_ROOT
TRAIN_TRANSCRIPT = os.path.join(DATASET_ROOT, "train.csv")
SPEAKER_ID = 6892  ##10K+ samples for this ID, best to train TTS
CONFIG_DIR = os.path.join("./config", DATASET_NAME)
OUTPUT_PATH = "../output_dataset"

ACOUSTIC_MODEL = "polish_mfa"
DICTIONARY_MODEL = "polish_mfa"
SPEAKER_NAME = "universal"


PREPROCESSED_DATA_PATH = os.path.join(OUTPUT_PATH, "preprocessed_data", DATASET_NAME)
RAW_PATH = os.path.join(OUTPUT_PATH, "raw_data")
RAW_DATA_SPEAKER_PATH = os.path.join(RAW_PATH, SPEAKER_NAME)
CORPUS_PATH = RAW_DATA_SPEAKER_PATH
TEXTGRID_DIR = os.path.join(PREPROCESSED_DATA_PATH, "TextGrid", SPEAKER_NAME)
CONFIG = get_yaml_contents(CONFIG_DIR, "preprocess")
# Create directory structure
os.makedirs(OUTPUT_PATH, exist_ok=True)
os.makedirs(CORPUS_PATH, exist_ok=True)
os.makedirs(PREPROCESSED_DATA_PATH, exist_ok=True)
os.makedirs(RAW_DATA_SPEAKER_PATH, exist_ok=True)
os.makedirs(TEXTGRID_DIR, exist_ok=True)

#create dataset and apply wav preprocessing
create_dataset(TRAIN_TRANSCRIPT, TRAIN_PATH, SPEAKER_ID, RAW_DATA_SPEAKER_PATH)
prepare_align(CONFIG, data_path=RAW_DATA_SPEAKER_PATH)

# run alignment
align_cmd_opts = f"{CORPUS_PATH} {DICTIONARY_MODEL} {ACOUSTIC_MODEL} {TEXTGRID_DIR}"
command = f"mfa align --clean --single_speaker {align_cmd_opts}"
print(command)
with open("test.log", "wb") as f:
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    for c in iter(lambda: process.stdout.read(1), b""):
        sys.stdout.buffer.write(c)
        f.buffer.write(c)
os.remove("test.log")
# build dataset
preprocessor = Preprocessor(
    CONFIG, raw_path=RAW_PATH, preprocessed_path=PREPROCESSED_DATA_PATH
)
preprocessor.build_from_path()
