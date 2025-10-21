---
layout: post
title:  "Block-Term Tensor Regression"
picture: /assets/images/projects/publication.webp
duration: Jan. 2019 - Current
role: Lead Researcher
publish: True
---

# Introducing BTTR: Block-Term Tensor Regression

## Overview

Welcome to the introduction of **BTTR (Block-Term Tensor Regression)**, a cutting-edge method for tensor decomposition and regression. This tool is designed for high-performance computation and offers a robust solution for handling multi-dimensional data. Utilizing advanced algorithms and optimization techniques, BTTR is tailored for extracting maximally correlated representations from complex datasets.

## What is BTTR?

BTTR stands for Block-Term Tensor Regression, a deflation-based method that extracts maximally correlated representations of tensors. By leveraging ACE/ACCoS algorithms, BTTR ensures efficient and accurate tensor decomposition, making it a powerful tool for data scientists and researchers working with high-dimensional data.

## Key Features

### High-Performance Tensor Decomposition

BTTR employs advanced algorithms like ACE/ACCoS for optimal tensor decomposition. These algorithms are known for their efficiency and accuracy, ensuring that BTTR can handle large and complex datasets with ease.

### Flexible and Customizable

BTTR offers a range of customization options to fit various needs:
- **SNRs (Signal-to-Noise Ratios):** Adjustable range for fine-tuning.
- **Ratios:** Configurable to ensure precise control over decomposition.
- **Deflation Options:** Ability to enable or disable deflation based on specific requirements.
- **Rank Enforcement:** Option to enforce rank-1 decompositions for specific use cases.

### Integration with Popular Libraries

BTTR is built on top of popular scientific computing libraries like NumPy and SciPy, and integrates seamlessly with Tensorly for tensor operations. This ensures compatibility and ease of use for users familiar with these tools.

## Example Usage

Here's a quick overview of how to use BTTR in your projects:

```python
import numpy as np
from bttr import BTTR

# Initialize BTTR
bttr = BTTR()

# Generate sample data
X = np.random.randn(100, 10, 10)  # Example tensor data
Y = np.random.randn(100, 1)       # Example response variable

# Train the BTTR model
bttr.train(X, Y, nFactor=5, SNRs=range(30, 41), ratios=np.arange(95, 99.9, 1))

# Perform predictions or further analysis using the trained model
```

In this example, we initialize the BTTR model and train it using sample tensor data `X` and response variable `Y`. The `train` method offers various parameters to customize the training process, including the number of factors, SNRs, and ratios.

## Detailed Functionality

### Fixing Numpy Vectors

The `fix_numpy_vector` function is a utility to properly encode 1D arrays in Python, ensuring they are correctly interpreted by the tensor operations.

```python
def fix_numpy_vector(vector):
    return vector[None].T if len(vector.shape) == 1 else vector
```

### Training the Model

The `train` method is the core of the BTTR class, implementing the Block-Term Tensor Regression algorithm. It supports a range of parameters to control the training process and ensure optimal results.

```python
class BTTR:
    def train(self, X: np.ndarray, Y: np.ndarray, nFactor: int, SNRs=range(30, 41), ratios=np.arange(95, 99.9, 1), useACCoS=False, use_deflate=(True, True), enforce_rank_1=False, score_vector_matrix=False):
        # Training logic here
```

## Conclusion

BTTR is a versatile and powerful tool for tensor regression, offering high performance and flexibility. Whether you are working on complex scientific computations or data-driven research, BTTR provides the tools you need to efficiently manage and analyze high-dimensional data.

For more information and to access the code, visit the [BTTR GitHub repository](https://github.com/TheAxeC/Cardinal).

Happy coding!

---