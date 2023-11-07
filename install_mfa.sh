#Make sure mfa is installed in the environment and run the following
# pip install git+https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner.git@v2.2.17
# pip install pgvector hdbscan
#conda install -c conda-forge pynini
# pip install --only-binary :all: pynini
mfa model download acoustic polish_mfa
mfa model download g2p polish_mfa
mfa model download dictionary polish_mfa