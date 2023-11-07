#!/bin/sh
wget -O ../cml-tts.tar.bz2 https://www.openslr.org/resources/146/cml_tts_dataset_polish_v0.1.tar.bz
cd ../ && tar -xvjf cml-tts.tar.bz2 && mv cml_tts_dataset_polish_v0.1/ cml-tts/