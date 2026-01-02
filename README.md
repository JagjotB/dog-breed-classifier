Dog Breed Classifier – ImageNet CNN Evaluation

    This project implements an end-to-end image classification pipeline in Python that evaluates pretrained convolutional neural networks on pet images. The system determines whether an image contains a dog and, if so, whether the dog’s breed is correctly identified. The focus of the project is on data preprocessing, evaluation logic, and error analysis rather than model training.

    The project demonstrates how label quality and evaluation design directly affect model performance and highlights practical transfer learning workflows used in real-world machine learning systems.

Project Objectives

- Classify images as dog vs non-dog
- Identify the correct dog breed when applicable
- Compare multiple CNN architectures objectively
- Demonstrate the impact of ground-truth labeling on evaluation metrics
- Build a configurable and reproducible ML evaluation pipeline

Models Used

- ResNet (pretrained on ImageNet)
- AlexNet (pretrained on ImageNet)
- VGG (pretrained on ImageNet)

Project Structure

- check_images.py

  - Main execution script that orchestrates the pipeline

- classifier.py

  - Handles CNN inference using pretrained models

- get_input_args.py

  - Parses command-line arguments

- get_pet_labels.py

  - Extracts ground-truth labels from image filenames

- classify_images.py

  - Runs image classification and compares predicted labels to ground truth

- adjust_results4_isadog.py

  - Determines dog vs non-dog classification for both pet and classifier labels

- calculates_results_stats.py

  - Computes evaluation counts and percentage-based metrics

- print_results.py

  - Prints formatted result summaries and misclassifications

- pet_images/

  - Provided dataset of 40 labeled images

- uploaded_images/

  - User-provided images for custom testing

- dognames.txt

  - Canonical list of valid dog breed names

- run_models_batch.sh

  - Batch evaluation on the provided dataset

- run_models_batch_uploaded.sh

  - Batch evaluation on custom uploaded images


Environment Setup

- Create and activate a dedicated environment

  - conda create -n dogcls python=3.10 -y
  - conda activate dogcls

- Install dependencies

  - conda install pytorch torchvision -c pytorch -y

- Verify installation

  - python -c "import torch, torchvision; print(torch.**version**, torchvision.**version**)"

Running the Project

- Evaluate the provided dataset

  - sh run_models_batch.sh
  - Output files:

    - resnet_pet-images.txt
    - alexnet_pet-images.txt
    - vgg_pet-images.txt

- Evaluate custom uploaded images

  - sh run_models_batch_uploaded.sh
  - Output files:

    - resnet_uploaded-images.txt
    - alexnet_uploaded-images.txt
    - vgg_uploaded-images.txt

Custom Image Requirements

- Images must be in JPEG (.jpg) format
- Images should be approximately square
- Filenames must encode the true ground-truth label

Examples

- Doberman_pinscher_01.jpg
- Doberman_pinscher_02.jpg
- lion.jpg
- Steering_wheel.jpg

Important Notes

- The filename is treated as the ground-truth label
- Generic filenames (for example, Dog_01.jpg) prevent meaningful breed evaluation

Evaluation Metrics

- Number of images
- Number of dog images
- Number of non-dog images
- Percentage of correctly classified dog images
- Percentage of correctly classified non-dog images
- Percentage of correctly classified dog breeds
- Overall label match percentage

Key Skills Demonstrated

- Command-line interface design using argparse
- Data preprocessing and label normalization
- Transfer learning with pretrained convolutional neural networks
- Model evaluation and metric design
- Error analysis and debugging of ML pipelines
- Python data structures for experiment tracking
- Environment and dependency management
- Batch experimentation and reproducibility

Key Takeaway

- Strong machine learning systems depend as much on data handling and evaluation logic as on model architecture
- Proper labeling and reproducible experimentation are essential for meaningful results