#!/bin/bash

timestamp=`date "+%d.%m.%Y_%H.%M.%S"`
output_dir='./logs/tweet_avg_non_chronological_bin_eval/'
config_file='./configs/tweet_avg_non_chronological_bin_eval.txt'

export CUDA_VISIBLE_DEVICES=0

mkdir -p $output_dir
#sudo touch ${output_dir}log.dev_${timestamp}.txt

echo ${config_file}
timestamp=`date "+%d.%m.%Y_%H.%M.%S"`
python3 -u main.py ${config_file} log.tweet_avg_non_chronological_bin_eval.txt 2>&1 | sudo tee ${output_dir}log.dev_${timestamp}.txt
