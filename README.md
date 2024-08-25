# Analyzing the effect of product type on the pereceived helpfulness of online reviews

This repository contains the code for my master thesis
"Unveiling the Influence of Product Type on Review Helpfulness: An Analysis between
Hedonic and Utilitarian Products using XGBoost"
    
This code covers the entire workflow from data selection to preparation, feature engineering, and model deployment for both hedonic and utilitarian data. It includes methods for detailed result analysis and general implementation practices. For a comprehensive overview of the code and methodology, please refer to the details below.

# Abstract
Online reviews have become a crucial factor in shaping consumer purchasing decisions, providing insights into product features and helping mitigate information asymmetry in digital marketplaces. This work explores the impact of online reviews on consumer behavior, with a focus on the distinction between utilitarian and hedonic products. A comprehensive framework is developed to assess how review helpfulness varies by product type. Advanced machine learning techniques, such as XGBoost and logistic regression, combined with SHAP value analysis, are employed to analyze the effectiveness of various review features in predicting helpfulness. The methodology is validated through practical examples and rigorous tests, revealing significant insights into feature importance and the varying impacts of review helpfulness on utilitarian versus hedonic products. These findings enhance the understanding of consumer behavior and provide actionable recommendations for optimizing review strategies on e-commerce platforms.
 
# Repository structure

| Folder | Description |
| ------ | ---------| 
| `1 Data Selection` | Includes the process of selecting review data for both hedonic and utilitarian products. |
| `2 Feature Preperation` | Details the evaluation of 15 features that describe review helpfulness. |
| `3 Data Analysis` |  Provides descriptive insights into the feature distribution and the helpfulnes s distribution. |
| `4 Model Building` | Encompasses the deployment of classification models for predicting helpfulness, along with code for SHAP value analysis. |


# Data

The dataset used in this analysis is the Amazon Reviews dataset collected by McAuley Lab in 2023, available at https://amazon-reviews-2023.github.io/.

This extensive dataset encompasses over 571.54 million online reviews, categorized into 16 main product categories. It includes:
- User Reviews: Detailed records with ratings, review text, helpfulness votes, and other relevant metrics.
- Item Metadata: Comprehensive information including product descriptions, prices, raw images, and additional descriptive features.
- Interaction Links: Graphs illustrating user-item interactions and "bought together" relationships.
Due to the large size of the files, only the final processed dataset is provided here.

# Reproducing results




# Methodology
The main contributions of this thesis are:
- Development of an estimation approach based on generative neural networks that allows for uncertainty quantification of parameters or model functionals
- Application to max-stable processes in order to analyze spatial extremes
- Extensive evaluation of the approach with regards to several novel metrics
- Application to extreme precipitation events across Western Germany

In the following are some of the important visualizations, for further details see the referenced publication.


## Proposed neural network architecture
The figure shows the proposed model architecture. The spatial field is fed through three blocks convolutional and max-pooling layers. Across the blocks, the output size decreases, while the channel size increases. In the second and third block, residual connections are added, marked by the arrows on top. After the convolutional layers the network is flattened and fed through some final linear layers, where Gaussian noise is multiplied on top to finally create $m$ output samples. For parameter prediction, samples of $\lambda, \nu$ are created, while for the direct estimation of the extremal coefficient function, sample points of the function are predicted as $\theta^i_j := \hat{\theta}_j(h_i)$.

![](4 Model Building/Pictures/Mean_ShapValues.png)

## Exemplary simulation results
The figure visualizes the different estimation methods for the max-stable models using a selected test sample $(\lambda, \nu) = (1.51, 1.37)$ for the Brown-Resnick model. In each figure the upper left panel shows the different location estimates, while the upper right panel shows the estimated extremal coefficient functions. The lower left panel shows the sample-based distribution estimates of the $\mathrm{ABC}$ and $\mathrm{EN}_{\lambda,\nu}$ method and the lower right panel shows the estimated pointwise confidence intervals ($\alpha = 0.05$) for the extremal coefficient function.

![](/Users/paulahofmann/Documents/Coding/Online-Review/3 Data Analysis/Helpful_Code_Product_Type.png)

The figure visualizes the different estimation methods for the Whittle-Matérn kernel (robustness scenario #2) using a selected test sample $(\lambda, \nu) = (4.00, 0.81)$. The plot division is the same as above.

![](imgs/whitmat_results.png)

## Analysis of precipitation extremes

Some results on the analysis of summer precipitation maxima across Western Germany.

### Visualization of precipiation fields
The figure shows the observed precipitation maxima in 2022 (top) and corresponding simulations from an estimated Schlather model with powered exponential correlation function (bottom ). The simulations have been transformed back to the original GEV surface.

![](imgs/2022_tp.png)

![](imgs/2022_tp_estimates.png)

### Estimation of spatial dependence

The figure shows the different estimates for the extremal coefficient function. The black dots are the binned F-madogram estimates and the lines correspond to the pointwise mean of the estimated extremal coefficient functions. The left panels shows F-madogram estimate with data from 2021-2023 and the right panel with data from 2011-2023.

![](imgs/madogram_estimate_powexp.png)
# Online-Review# Online-Review