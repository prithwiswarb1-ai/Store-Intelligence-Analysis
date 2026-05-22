#!/bin/bash

echo "Starting Detection Pipeline..."

python pipeline/detect.py

echo "Starting Event Simulator..."

python pipeline/simulator.py