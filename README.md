# Polish TTS on EfficientSpeech

1. run `download_data.sh` to download the Polish dataset and extract it.

2. Create a conda environment and install Montreal Forced Aligner from source [here](https://github.com/montrealcorpustools/montreal-forced-aligner/) .
3. run `install_mfa.sh` to download the required models.
4. check `preprocess.yaml` and see if `corpus_path` to the correct path for the dataset.
5. run `prepare_dataset.py` and wait till the process finishes, This can take a while as there are 10K+ audio files
6. Finally starting training with
   
```python 
python train.py --preprocess-config ./config/CML_Polish/preprocess.yaml --precision 16-mixed --num_workers 4 --batch-size 128 --max_epochs 1000 --warmup_epochs 50 --lr 0.001 --out-folder ../train_outputs --verbose --wav-path ../train_outputs
```
