# 🔬 Analyzing the Effect of Product Type on the Perceived Helpfulness of Online Reviews

Welcome to the repository for my master's thesis:
>"Unveiling the Influence of Product Type on Review Helpfulness: An Analysis between Hedonic and Utilitarian Products using XGBoost"

This repository contains all the code, analyses, and methodologies used to evaluate how review helpfulness varies between hedonic (pleasure-oriented) and utilitarian (functionality-oriented) products.

# 📝 Abstract

Online reviews play a **crucial role** in shaping consumer purchasing decisions by offering insights into product features and reducing information gaps in digital marketplaces. This study examines how online reviews influence consumer behavior, focusing on utilitarian versus hedonic products. A framework is created to evaluate how review helpfulness varies with product type. Advanced machine learning techniques, including **XGBoost**, **Logistic Regression**, and **SHAP value analysis**, are used to assess the impact of review features on helpfulness. The methodology is validated with practical examples, providing key insights into feature importance and the differential effects on utilitarian and hedonic products. These findings improve understanding of consumer behavior and offer actionable recommendations for enhancing review strategies on e-commerce platforms.
 
# 🛠 Repository Structure

| Folder | Description |
| --- | ---------| 
| `1 Data Selection` | Includes the process of selecting review data for both hedonic and utilitarian products. |
| `2 Feature Preperation` | Details the evaluation of 15 features that describe review helpfulness. |
| `3 Data Analysis` |  Provides descriptive insights into the feature distribution and the helpfulness distribution. |
| `4 Model Building` | Encompasses the deployment of classification models for predicting helpfulness, along with code for SHAP value analysis. |


# 📊 Data

The dataset used in this analysis is the Amazon Reviews dataset collected by McAuley Lab in 2023, available at https://amazon-reviews-2023.github.io/.

This extensive dataset encompasses over 571.54 million online reviews, categorized into 16 main product categories. It includes:
- User Reviews: Detailed records with ratings, review text, helpfulness votes, and other relevant metrics.
- Item Metadata: Comprehensive information including product descriptions, prices, raw images, and additional descriptive features.
- Interaction Links: Graphs illustrating user-item interactions and "bought together" relationships.
Due to the large size of the files, only the final processed dataset is provided here.


# 🔬 Methodology

This thesis makes the following contributions:

Assessing the impact of product type on the helpfulness of reviews.
Investigating classification approaches for predicting review helpfulness, specifically using XGBoost and Logistic Regression.
Conducting SHAP value analysis to evaluate the importance of different features in products.

In the following are some of the important findings:


# 📈 Key Figures & Visualizations

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

## 2. Review Lengths (Word Count & Sentence Length)

This section focuses on the length of reviews, both in terms of word count and sentence length, comparing **helpful** and **unhelpful** reviews for both product types.

- **Key Insights**:
  - Helpful reviews for both product types (hedonic and utilitarian) tend to have higher word counts and feature longer sentences on average.
  - There is little difference in word count and sentence length between product types.

- **Implications**:
  - More detailed and longer reviews, both in terms of word count and sentence complexity, tend to be perceived as more helpful regardless of the product type.

![Review Lengths](./3%20Data%20Analysis/ViolinPlot.png)


# 📈 Model Building and Class Imbalance Handling

Given the imbalance between review types (hedonic vs. utilitarian), **SMOTE (Synthetic Minority Over-sampling Technique)** was applied to balance the dataset. After applying SMOTE, hyperparameter tuning was conducted to build an optimal model that yielded the best performance for both product types.

- **SMOTE**: This technique oversamples the minority class (utilitarian products) to mitigate the imbalance and improve model learning.
- **Hyperparameter Tuning**: The model parameters were fine-tuned using Bayesian Optimization to maximize the performance for both product types.

# Model Interpretation with SHAP Values

To interpret the model's predictions, **SHAP values** were employed. SHAP values provide insights into how different features influence the model's predictions for both hedonic and utilitarian products. 

The SHAP plot highlights how specific features (e.g., word count, sentiment, rating) contribute to the model’s predictions. This allows us to understand which aspects of the reviews (e.g., positive sentiment or longer reviews) have the most impact on predicting helpfulness for different product types. The SHAP plot is seen in the figure: 

![SHAP Values](./4%20Model%20Building/ShapValues.jpg)


---



# 🎯 Conclusion

In summary, this research highlights significant differences between hedonic and utilitarian product reviews, providing a nuanced understanding of what makes a review helpful.

Key Findings:
- **Hedonic Products Reviews**: More subjective, emotionally engaging, and benefit from low volume with rich content (images, emotional language).
- **Utilitarian Product Reviews**: Critical, rational, and focus on aiding decision-making with recent, factual reviews.

These insights can guide e-commerce platforms in refining their review filtering and recommendation algorithms, ultimately enhancing the consumer shopping experience. Further Research could investigate the interaction between features and how they jointly impact review helpfulness.


# 🔗 References

Meng et al. (2020): The impact of review features on helpfulness in e-commerce.
Mudambi and Schuff (2010): What makes a helpful online review?
