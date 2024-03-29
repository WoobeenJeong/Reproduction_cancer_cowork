# 원격 서버에서의 환경 설정

############################################
# remote explorer in vscode
# password on termius (0000xxxx[])

# Host 147.47.91.233
#   HostName 147.47.91.233
#   User wbjeong
#   Port 7777

###########################################
# settings:

# [Ubuntu 18.04]
# lsb_release -a

# [Ubuntu 8.7] 
cat /etc/os-release

# No LSB modules are available.
# Distributor ID: Ubuntu
# Description:    Ubuntu 20.04.6 LTS
# Release:        20.04
# Codename:       focal

# [NVIDIA GPU - Nvidia GeForce RTX 2080 Ti x 16, CUDA 11.0 and cuDNN 7.5]

lspci | grep -i VGA
# 03:00.0 VGA compatible controller: Matrox Electronics Systems Ltd. Integrated Matrox G200eW3 Graphics Controller (rev 04)

# [Python 3.7.7]
# [Python 3.10.9]
python --version

############################################

# conda create --name cancer
conda activate cancer

############################################

# [etc.]
conda install h5py=2.10.0 matplotlib=3.1.1 numpy=1.18.1 pandas=1.1.3 pillow=7.0.0 scikit-learn=0.22.1 scipy=1.4.1 tensorflow=1.13.1
conda install -c pytorch torchvision=0.7.0

### Errors ###
# conda install opencv-python==4.1.1 openslide-python==1.1.1 openslide==3.4.1 tensorboardX==1.9 captum==0.2.0 shap==0.35.0

conda install fastchan::opencv-python-headless    # 4.7.068
conda install conda-forge::openslide-python       # 1.3.1
conda install conda-forge::openslide              # 4.0.0
conda install conda-forge::tensorboardx           # 2.6.2
conda install conda-forge::shap                   # 0.45.0

############################################

# [WSI(.svs), molecular feature]
# GDC : https://portal.gdc.cancer.gov/

# [clinical metadata]
# cBio : https://www.cbioportal.org/

# WSI downloading :
# https://docs.gdc.cancer.gov/Data_Transfer_Tool/Users_Guide/Data_Download_and_Upload/

# CLAM downloading :
# https://github.com/mahmoodlab/CLAM/blob/master/docs/INSTALLATION.md

##########################################
# 이미지 분석 툴: CLAM
# (conda 이름 : clam)

# 위에 소개한 CLAM downloading의 해당 홈에서 다운로드
# clam.yaml 이라는 문서 다운로드

# 1. conda환경 구축에서 pytorch=1.3.1=py3.7_cuda10.1.243_cudnn7.6.3_0 이건 따로 넣어줘야 함 (인식 못함)
# 2. 이전버전 Numpy API 쓰기 때문에 해결 필요
# 3. imagecodecs/_aec.c 파일에서는 libaec.h 찾을 수 없음 (libxml/xmlversion.h 도)
# 4. GCC 컴파일러가 오류

conda env create -n clam -f cancer/env/clam.yaml

conda activate clam

conda install pytorch::pytorch
# conda install conda-forge::cudatoolkit  # 11.8.0 (already installed)
# conda install conda-forge::cudnn        # 8.9.7.29  
conda install conda-forge::libxml2      # 2.9.9
conda install conda-forge::libxslt      # 1.1.32
conda install conda-forge::libaec       # 1.0.4

python -c "import torch; print(torch.__version__)"                  # 1.3.1
python -c "import torch; print(torch.backends.cudnn.version())"

###########################################
# manifest를 다운로드
# GDC : https://portal.gdc.cancer.gov/ 방문
# Repository 클릭
# 가장 우측 상단에 TCGA-원하는암종으로 검색
# save cohort로 저장
# cohort builder로 이동
# 왼쪽 카탈로그 중 Available Data -> Data type 모든 항목 확장 -> slide image 선택
# 다시 Repository에서 Experimental Strategy -> Diagnostic Slide / Tissue Slide 선택 가능
# 목표는 Diagnostic image임

# 5,720 patients across 14 cancer types from TCGA
# 목록: (앞에 TCGA-를 붙일 것)
# [BLCA, BRCA, COADREAD, HNSC, KIRC, KIRP, LGG, LIHC, LUAD, LUSC, PAAD, SKCM, STAD, UCEC]

conda install -c bioconda gdc-client

gdc-client download -m ../wbjeong/cancer/WSI/gdc_manifest_LUAD_diagnostic_slide.txt -d /data/cancer/LUAD

ls -l | grep ^d | wc -l
ls -l | grep ^d | sort | wc -l

### 데이터 위치
cd /data/cancer/LUAD

### 용량
df -h

##########################################
