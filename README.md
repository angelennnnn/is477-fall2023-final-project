1. Environment Setup:

Operating System: Windows Version 11
Python Version: 3.9.6
Build Version: 22D68
# Overview

This document outlines the process of reproducing the results of Wolberg et al (2022) using the UCI Machine Learning Repository's Breast Cancer Wisconsin Diagnostic dataset. The document details the data availability, software license, data license, reproducibility, and analysis of the study. This document contains a reproducible work flow for data analysis on the project, and the structure can be used and recreated. 

## Data Availability

**Source:**  
UCI Machine Learning Repository - Breast Cancer Wisconsin Diagnostic dataset: [UCI Repository](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic)
This is the origin of where the data was fine from. It is the Wisconsin Breast Cancer Diagonstic dataset. The copyright and licensing of this under the UCI Adult dataset license is identified - CC By 4.0. This makes it so that you are able to share, adapt, and modify the dataset. You just need to make sure that you credit the original authors of the dataset. Attribution is required for the dataset usage. 

Becker,Barry and Kohavi,Ronny. (1996). Adult. UCI Machine Learning Repository. https://doi.org/10.24432/C5XW20.

**Copyright and Licensing:** Public domain (no copyright)

**Original Study Reference:**  
Wolberg, W. H., Street, W. N., & Mangasarian, O. L. (1995). Nuclear feature extraction for breast tumor diagnosis. In Biomedical Image Processing and Biomedical Visualization (Vol. 2359, pp. 2-11). International Society for Optics and Photonics.
**Zenodo Badge**
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10312729.svg)](https://doi.org/10.5281/zenodo.10312729)
## Software License

**MIT License**

- Permissive license allowing modification and usage
- Enables distribution, use, and modification of the work
- Simple for others to interact with the project
- Free license created by MIT
- Allows for distribution, making it usable for future classes

## Data License

Public domain (no copyright)

- Freely usable for any purpose
- No restrictions on distribution or modification

## Reproducing

Reproducing the results involves the following steps:

1. Download the dataset from the provided link.
2. Prepare the data for analysis, which may involve cleaning and preprocessing.
3. Implement the logistic regression model described in Ding et al (2022).
4. Evaluate the model's performance on the dataset.
5. Compare the results with those reported by Ding et al (2022).

**Note:** Due to limitations, alternative solutions might be necessary:

- Modify the provided code or develop your own implementation of the logistic regression model.
- Adjust data preprocessing steps based on the chosen model implementation.

## Analysis

The analysis will focus on the following aspects:

- **Overall accuracy:** Compare the model's overall accuracy with the reported results.
- **Performance by diagnosis:** Analyze whether the model performs differently for predicting malignant and benign tumors.
- **Comparison between men and women:** Investigate if the model's accuracy varies for different genders.
- **Comparison with Ding et al (2022):** Evaluate how the results compare with the original study and discuss potential reasons for discrepancies.

Following these steps and analyzing the results as described will allow you to reproduce the logistic regression study on the Breast Cancer Wisconsin Diagnostic dataset and assess its performance.

![Alt text](../data/imageworkflow.png)

Software License
MIT License Compatibility: This license is compatible with other open-source licenses, enabling seamless integration with other projects and promoting a vibrant open-source ecosystem. Limited Liability: The MIT License includes a liability disclaimer, providing legal protection to both the authors and contributors of the software. Preservation of Copyright Notice: Users are required to include the original copyright notice and license text in derivative works, ensuring proper attribution and clarity regarding licensing terms. Simplicity and Clarity: The MIT License is concise and written in straightforward language, making it accessible to developers and users alike. 

MIT License

Copyright (c) 2023 angelennnnn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
