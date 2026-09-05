# AHC Visual Intelligence Hackathon
## Real-Time Video Anomaly Detection

A real-time video anomaly detection system developed for the **AHC Visual Intelligence Hackathon 2026**.

The goal is to detect anomalous events from video footage as early and accurately as possible while maintaining low inference latency and minimizing false alarms.

---

## Project Overview

This project focuses on detecting abnormal events in video streams such as:

- Traffic accidents
- Traffic congestion
- Stalled or broken-down vehicles
- Vehicles blocking traffic
- Wrong-way driving
- Road spills or debris
- Waterlogging or flooding
- Fire
- Smoke
- Fighting or violence
- Loitering or suspicious presence

The system is designed with real-time inference and limited GPU resources in mind.

---

## Current Status

### Completed

- [x] Project structure created
- [x] Python virtual environment configured
- [x] Git repository initialized
- [x] GitHub repository connected
- [x] OpenCV installed and verified
- [x] NumPy installed and verified
- [x] PyTorch installed with CUDA support
- [x] NVIDIA RTX 3050 GPU detected
- [x] GPU computation successfully verified

### In Progress

- [ ] Video input pipeline
- [ ] Video frame extraction
- [ ] Frame sampling / temporal processing
- [ ] Anomaly detection model
- [ ] Event classification
- [ ] Temporal anomaly localization
- [ ] Real-time inference pipeline
- [ ] False-positive reduction
- [ ] Submission JSON generation
- [ ] Runtime and latency measurement
- [ ] Evaluation on public test data

---

## Hardware and Software

### Hardware

- NVIDIA GeForce RTX 3050 Laptop GPU
- 4 GB VRAM

### Software

- Python 3.11
- PyTorch
- TorchVision
- OpenCV
- NumPy
- CUDA-enabled PyTorch

---

## Project Structure

```text
AHC_Hackathon/
│
├── data/
│   └── # Dataset files (not uploaded to GitHub)
│
├── docs/
│   └── # Documentation and architecture notes
│
├── notebooks/
│   └── # Experiments and analysis
│
├── outputs/
│   └── # Generated outputs and results
│
├── src/
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt







Video Stream
     │
     ▼
Frame Capture
     │
     ▼
Frame Sampling
     │
     ▼
Lightweight Detection / Feature Extraction
     │
     ▼
Temporal Analysis
     │
     ▼
Anomaly Classification
     │
     ▼
Temporal Event Localization
     │
     ▼
False-Positive Filtering
     │
     ▼
Submission / Alert







Evaluation

The hackathon evaluates both anomaly detection and temporal localization.

For timestamped events, the predicted interval must overlap sufficiently with the ground-truth interval. Temporal Intersection over Union (IoU) is used for matching events.

The system will therefore optimize for:

Detection accuracy
Correct anomaly classification
Temporal localization accuracy
Low false-positive rate
Low inference latency






Development Goals

The main goals of this project are:

Build a reliable video-processing pipeline.
Develop a lightweight anomaly detection approach.
Support real-time or near-real-time inference.
Minimize false alarms.
Correctly classify different anomaly types.
Localize anomalies temporally when required.
Measure and optimize inference latency.
Produce valid hackathon submission files.