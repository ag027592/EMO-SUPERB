# EMO-SUPERB: EMOtion Speech Universal PERformance Benchmark

[![Paper](https://img.shields.io/badge/IEEE%20SLT%202024-Open--Emotion-00629B?style=flat-square)](https://doi.org/10.1109/SLT61566.2024.10832296)
[![arXiv](https://img.shields.io/badge/arXiv-2402.13018-B31B1B?style=flat-square)](https://arxiv.org/abs/2402.13018)
[![Leaderboard](https://img.shields.io/badge/Leaderboard-emosuperb.github.io-1f6feb?style=flat-square)](https://emosuperb.github.io/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

# Overview
This repository provides the implementation of Open-Emotion: A Reproducible EMO-SUPERB for Speech Emotion Recognition Systems, published at the 2024 IEEE Spoken Language Technology Workshop (SLT).

Speech emotion recognition (SER) suffers from a reproducibility crisis: 80.77% of SER papers report results that cannot be reproduced, largely because datasets ship without standard train/dev/test splits. EMO-SUPERB addresses this with standardized, leakage-free partitions for six open-source SER datasets in English and Chinese, a codebase that evaluates 15 state-of-the-art speech self-supervised learning models, and a community-driven online leaderboard. We additionally prompt ChatGPT to interpret the 2.58% of annotations written as free-form typed descriptions, which classification models normally discard, yielding a 3.08% average relative gain.

📄 Paper: https://ieeexplore.ieee.org/abstract/document/10832296
📄 Arxiv: https://arxiv.org/pdf/2402.13018
🏆 Leaderboard and project website: https://emosuperb.github.io/

👥 Authors: Haibin Wu*, Huang-Cheng Chou*, Kai-Wei Chang, Lucas Goncalves, Jiawei Du, Jyh-Shing Roger Jang, Chi-Chun Lee, and Hung-yi Lee (*equal contribution)

 # Installation
 1. The EMO-SUPERB is developed based on [s3prl](https://github.com/s3prl/s3prl#installation) toolkit, please install it first.
    * Please follow the [instructions](https://s3prl.github.io/s3prl/tutorial/installation.html#editable-installation) to do an editable installation.
      ```
      git clone https://github.com/s3prl/s3prl.git
      cd s3prl
      pip install -e .
      ```
2. Move the ```emo-superb``` folder into the path ```s3prl/s3prl/downstream``` and rename the folder as the **"emotion_dev"**
3. Move the ```data``` folder into the path ```s3prl/s3prl/``` 
   * Download WAV files into the folder for each database (e.g., ```data/IEMOCAP/Audios```)by submitting the EULA form for the six databases.
   * [IEMOCAP](https://sail.usc.edu/iemocap/iemocap_release.htm)
   * [CREMA-D](https://github.com/CheyneyComputerScience/CREMA-D)
   * [IMPROV](https://lab-msp.com/MSP/publications/AcademicLicense-MSP-IMPROV.pdf)
   * [PODCAST](https://lab-msp.com/MSP/publications/Busso-FDPDTUA_V2.pdf)
   * [NNIME](https://nnime.ee.nthu.edu.tw/wp-content/uploads/2017/09/NNIME-Datebase-EULA_v2.pdf) (please apply via email: biiclab@ee.nthu.edu.tw) 
   * [BIIC-PODCAST](http://andc.ai/index.php) (please apply via email: cclee@ee.nthu.edu.tw)
# Train and Evaluation
## Trained Models
* All files can be downloaded by the [link](https://drive.google.com/file/d/15qjtVo46N944R5jRlFvKkIXBerwpjn3O/view?usp=sharing).
* Unzip the .zip file and move the folder into the path (s3prl/s3prl/result/)

## Training Models 

### Upstream name
| Index |        Model Name         |          Upstream Name          |
| ----- |:-------------------------:|:-------------------------------:|
| 01    |        WavLM        |           wavlm_large           |
| 02    |   W2V2 R    | wav2vec2_large_lv60_cv_swbd_fsh |
| 03    |     XLS-R-1B     |            xls_r_1b             |
| 04    | Data2Vec-A |      data2vec_large_ll60k       |
| 05    |       Hubert        |       hubert_large_ll60k        |
| 06    |    W2V2    |       wav2vec2_large_960        |
| 07    |        vq-wav2vec         |           vq_wav2vec            |
| 08    |    W2V     |          wav2vec_large          |
| 09    |       M CPC        |          modified_cpc           |
| 10    |        DeCoAR 2	         |             decoar2             |
| 11    |           TERA            |           tera_960hr            |
| 12    |        Mockingjay         |        mockingjay_960hr         |
| 13    |            NPC            |            npc_960hr            |
| 14    |          VQ-APC           |          vq_apc_960hr           |
| 15    |            APC            |            apc_960hr            |
| 16    |           FBANK           |              fbank              |

### Use the command line. We take the SAIL-IEMOCAP corpus as an example.
```
for upstream in fbank; do 
 for test_fold in fold1 fold2 fold3 fold4 fold5; do
  for corpus in IEMOCAP; do
  # The default config is "downstream/emotion/config.yaml"
  python3 run_downstream.py -n ${upstream}_${corpus}_$test_fold -m train -u ${upstream} -d emotion_dev -c downstream/emotion_dev/config_${corpus}.yaml -o "config.downstream_expert.datarc.test_fold='$test_fold'"
  python3 run_downstream.py -m evaluate -e result/downstream/${upstream}_${corpus}_$test_fold/dev-best.ckpt
  done;
 done;
done
```

### Run All Experiments
```
bash run_all_dataset_and_fold.sh
```

# Relabel by ChatGPT-4
The folder, named **```chatGPT```**, contains the promot (```Prompt.txt```) for ChatGPT and the input and output files.
* The input files (```input_dev.csv``` and ```input_train.csv```) include the file names, distributional primary emotions labels, and typed descriptions from annotators.
* The output files (```output_dev.csv``` and ```output_train.csv```) consist of the file names, adjusted distributional primary emotions labels, and reasons from ChatGPT.
We encourage everyone to contribute their prompt and results.

# Citation
If you find this work useful in your research, please cite:
```
@INPROCEEDINGS{Wu_2024_OpenEmotion,
  author={Wu, Haibin and Chou, Huang-Cheng and Chang, Kai-Wei and Goncalves, Lucas and Du, Jiawei and Jang, Jyh-Shing Roger and Lee, Chi-Chun and Lee, Hung-yi},
  booktitle={2024 IEEE Spoken Language Technology Workshop (SLT)},
  title={Open-Emotion: A Reproducible EMO-Superb For Speech Emotion Recognition Systems},
  year={2024},
  pages={510-517},
  doi={10.1109/SLT61566.2024.10832296}
}
```

# License
Released under the [MIT License](LICENSE).

