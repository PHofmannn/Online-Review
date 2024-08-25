# Analyzing the effect of product type on the pereceived helpfulness of online reviews

This repository contains the code for my master thesis
"Unveiling the Influence of Product Type on Review Helpfulness: An Analysis between
Hedonic and Utilitarian Products using XGBoost"
    
This code covers the entire workflow from data selection to preparation, feature engineering, and model deployment for both hedonic and utilitarian data. It includes methods for detailed result analysis and general implementation practices. For a comprehensive overview of the code and methodology, please refer to the details below.

# Abstract
Online reviews have become a crucial factor in shaping consumer purchasing decisions, providing insights into product features and helping mitigate information asymmetry in digital marketplaces. This work explores the impact of online reviews on consumer behavior, with a focus on the distinction between utilitarian and hedonic products. A comprehensive framework is developed to assess how review helpfulness varies by product type. Advanced machine learning techniques, such as XGBoost and logistic regression, combined with SHAP value analysis, are employed to analyze the effectiveness of various review features in predicting helpfulness. The methodology is validated through practical examples and rigorous tests, revealing significant insights into feature importance and the varying impacts of review helpfulness on utilitarian versus hedonic products. These findings enhance the understanding of consumer behavior and provide actionable recommendations for optimizing review strategies on e-commerce platforms.
 
# Repository structure

| Folder | Description |
| --- | ---------| 
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


# Methodology

This thesis makes the following contributions:

Assessing the impact of product type on the helpfulness of reviews.
Investigating classification approaches for predicting review helpfulness, specifically using XGBoost and Logistic Regression.
Conducting SHAP value analysis to evaluate the importance of different features in products.

In the following are some of the important findings:


# Findings on Features in Relation to Product Type

This section presents an analysis of various features such as rating, sentiment, word count, and sentence length, in relation to two types of products: **hedonic** (pleasure-oriented) and **utilitarian** (functionality-oriented). 

## 1. Rating & Sentiment Distribution

- **Key Insights**:
  - Hedonic products are more likely to receive extreme ratings, particularly higher ratings (rating 5) and have a higher proportion of **positive sentiment** in reviews.
  - Utilitarian products tend to receive lower ratings (rating 1) and more **negative sentiment** compared with hedonic products

- **Implications**:
  - Consumers are more likely to provide highly positive feedback for hedonic products, whereas utilitarian products often receive more critical reviews.
  - This suggests that customers are more positive emotionally invested in hedonic products and may express dissatisfaction with functional products when they do not meet practical expectations.

![Rating Distribution](./3%20Data%20Analysis/Helpful_Rating.png)

---

### 2. Review Lengths (Word Count & Sentence Length)

This section focuses on the length of reviews, both in terms of word count and sentence length, comparing **helpful** and **unhelpful** reviews for both product types.

- **Key Insights**:
  - Helpful reviews for both product types (hedonic and utilitarian) tend to have higher word counts and feature longer sentences on average.
  - There is little difference in word count and sentence length between product types.

- **Implications**:
  - More detailed and longer reviews, both in terms of word count and sentence complexity, tend to be perceived as more helpful regardless of the product type.

![Review Lengths](./3%20Data%20Analysis/ViolinPlot.png)


# Model Building and Class Imbalance Handling

Given the imbalance between review types (hedonic vs. utilitarian), **SMOTE (Synthetic Minority Over-sampling Technique)** was applied to balance the dataset. After applying SMOTE, hyperparameter tuning was conducted to build an optimal model that yielded the best performance for both product types.

- **SMOTE**: This technique oversamples the minority class (utilitarian products) to mitigate the imbalance and improve model learning.
- **Hyperparameter Tuning**: The model parameters were fine-tuned using Bayesian Optimization to maximize the performance for both product types.

# Model Interpretation with SHAP Values

To interpret the model's predictions, **SHAP values** were employed. SHAP values provide insights into how different features influence the model's predictions for both hedonic and utilitarian products. 

The SHAP plot highlights how specific features (e.g., word count, sentiment, rating) contribute to the model’s predictions. This allows us to understand which aspects of the reviews (e.g., positive sentiment or longer reviews) have the most impact on predicting helpfulness for different product types. The SHAP plot is seen in the figure: 

![SHAP Values](./4%20Model%20Building/ShapValues.jpg)


---



## Conclusion

The findings highlight distinct patterns in how customers rate and review hedonic versus utilitarian products. However, both types of products are primarily influenced by review depth, age, and rating extremity. These findings align with previous studies indicating that only a few features significantly impact review helpfulness (Meng et al., 2020), emphasizing the importance of detailed reviews (Mudambi and Schuff, 2010). Other factors driving review helpfulness differ between the two product categories.

- **Hedonic Products**: Helpful reviews benefit when there is a low review volume, subjective and moderately older reviews, with accompanying images, short titles, and rich use of nouns to enhance emotional engagement.
  
- **Utilitarian Products**: Helpful reviews tend to have a larger volume, are more recent, and contain critical evaluations with a negatively emotional tone. This helps consumers make well-informed decisions.


___