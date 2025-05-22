# MVSNet & R-MVSNet: Depth Estimation for Multi-View Stereo

### Authors
- Naga Venkata Dheeraj Chilukuri  
- Meenakshisundram Ganapathi Subramanian  
- Soorya Boopal

## Overview

This repository contains the implementation and experimental results for a project focused on enhancing depth inference from unstructured multi-view images using deep learning models. We benchmarked the original MVSNet and proposed an optimized variant inspired by R-MVSNet using GRU-based regularization for improved scalability and performance.

## Project Structure

├── configs/ # Configuration files for training/inference
├── datasets/ # Scripts to preprocess the DTU dataset
├── models/ # MVSNet & GRU-enhanced R-MVSNet models
├── results/ # Output visualizations and metric logs
├── utils/ # Utility functions (metrics, warping, etc.)
├── train.py # Training script
├── test.py # Inference and evaluation script
├── requirements.txt # Dependencies
└── README.md # This file

pgsql
Copy
Edit

## Features

- Baseline MVSNet using 3D CNN cost volume regularization  
- Modified R-MVSNet using sequential GRU to reduce memory complexity  
- Evaluation on DTU dataset with repeatable benchmarks  
- Improved depth accuracy and F-score  
- Support for high-resolution reconstructions  

## Results Summary

| Model       | Accuracy ↓ | Completeness ↓ | F-Score ↑ | Inference Time ↓ |
|-------------|------------|----------------|-----------|------------------|
| MVSNet      | Baseline   | Baseline       | Baseline  | Moderate         |
| R-MVSNet    | Improved   | Improved       | Higher    | Significantly Faster |

Visual reconstructions and quantitative plots are available in the `results/` directory.

## Installation

```bash
git clone https://github.com/DheerajCNV/MVSNet-RMVSNet-Depth.git
cd MVSNet-RMVSNet-Depth
pip install -r requirements.txt
```
## Usage
# Training

```bash
python train.py --config configs/train_config.yaml
```
# Testing

```bash
python test.py --config configs/test_config.yaml
```
Dataset preparation instructions for DTU are included in datasets/README.md.

## Enhancements
GRU-based regularization (inspired by NRR-MVSNet)

Adaptive depth sampling for better hypothesis refinement

Improved memory efficiency: from O(H×W×D) → O(H×W + D)

## Citation & References
If you use this work, please cite relevant papers:

Yao et al., "MVSNet: Depth Inference for Unstructured Multi-view Stereo," ECCV 2018.

Xu et al., "NRR-MVSNet: Non-local Recurrent Regularization Networks for Multi-view Stereo," arXiv 2021.
