# ### porpoise 가져오기
# https://github.com/mahmoodlab/PORPOISE.git

# ### 돌릴 kernel 생성중
# Installed kernelspec cancer in /home/wbjeong/.local/share/jupyter/kernels/cancer

# cancer                *  /home/wbjeong/.conda/envs/cancer
# clam            hrjs         /home/wbjeong/.conda/envs/clam
# base                     /opt/ohpc/pub/anaconda3

import os
import shutil

def copy_svs_files(source_directory, destination_directory):
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith(".svs"):
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_directory, file)

                shutil.copy(source_file_path, destination_file_path)
                print(f"파일 복사: {source_file_path} -> {destination_file_path}")

source_directory = "/data/cancer"
destination_directory = "/data/CLAM/DATA_DERECTORY"
copy_svs_files(source_directory, destination_directory)