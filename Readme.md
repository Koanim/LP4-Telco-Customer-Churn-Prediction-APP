# Telco Customer Churn Prediction App 📲

Welcome to the **Customer Churn Prediction App Project** for embedding machine learning model to streamlit. The mission is to develop an app for predicting Customer churn rate using a previously trained Machine Learning model.

![Python Version](https://img.shields.io/badge/Python-3.11-blue)
![Data Analysis](https://img.shields.io/badge/Data-Analysis-yellow)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-blueviolet)
![MIT licensed](https://img.shields.io/badge/license-mit-blue?style=for-the-badge&logo=appveyor)
![Issues](https://img.shields.io/github/issues/PapiHack/wimlds-demo?style=for-the-badge&logo=appveyor)
![PR](https://img.shields.io/github/issues-pr/PapiHack/wimlds-demo?style=for-the-badge&logo=appveyor)

## Prerequisites 📈

Ensure that you install the following libraries in your Python environment or virtual environment:

* Streamlit
* Pandas
* CatBoost
* Xgboost
* Gradient Boost


<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python


### Setup ⚙️

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone https://github.com/bamzyyyy/Telco-Customer-Churn-Prediction.git
```

Change into the cloned repository

```sh
  cd Telco-Customer-Churn-Prediction
  
```

Create a virtual environment

```sh

  python -m venv venv

```

Activate the virtual environment

```sh
  venv/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```


The app will be launched in your default web browser and can then be used to make customer churn predictions based on the input fields.

## Preview 🔍
<img width="1390" alt="Screenshot 2024-06-26 at 3 09 04 AM" src="https://github.com/bamzyyyy/Telco-Customer-Churn-Prediction-APP/assets/160126707/a249db3a-be71-4b86-bda2-0a51f577dd84">

<img width="1315" alt="Screenshot 2024-06-26 at 3 09 16 AM" src="https://github.com/bamzyyyy/Telco-Customer-Churn-Prediction-APP/assets/160126707/0e52b2b7-482f-4ac5-970c-2983385b8356">


## Features ✅

**Sales Prediction**: The app allows users to input your details. It can then predict using the Xgboost, Gradient Boost and CatBoost model from the Machine Learning components.

**Interactive Interface**: Streamlit provides an interactive, easy-to-use, web-based interface.

## Usage Instructions 📋

- Input Fields: The app displays input fields for the Gender, Seniorcitizen, Partner, Dependent, Tenure, Phoneservice, MultipleLines, InternetService, Onlinesecurity, onlinebackup, DeviceProtection, Monthlycharges, Totalcharges, Contracttype, Paperlessbilling, PaymentMethod, TechSupport, DeviceProtection, StreamingTV and StreamingMovies.
  
- Results: The app will display the predicted Churn rate for the specified inputs.

## Author 👨‍💼

  | Name                                            | LinkedIn                                                                                                                                                                                                                                               | Medium Article |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Aminu Oluwarotimi Desmond | [Aminu Oluwarotimi Desmond](https://www.linkedin.com/in/aminudesmond/) |[BUILDING A USER-FRIENDLY CHURN PREDICTION APP USING STREAMLIT](https://medium.com/@aminuoluwarotimi/crafting-an-interactive-telco-churn-prediction-app-with-streamlit-b672b6738d80)|


## Model Training and Saving ⏳

The Xgboost, Catboost and Gradient boost model was trained using the Telecommunication Customer Churn as shown in this GitHub repository: [LP4-Telco-Customer-Churn-Prediction-APP
](https://github.com/Koanim/LP4-Telco-Customer-Churn-Prediction-APP/).
## Acknowledgments 🙏

I would like to express my gratitude to the [Azubi Africa Data Analyst Program](https://www.azubiafrica.org/data-analytics) for their support and for offering valuable projects as part of this program. Not forgeting my scrum masters on this project [Rachel Appiah-Kubi](https://www.linkedin.com/in/racheal-appiah-kubi/) & [Emmanuel Koupoh](https://github.com/eaedk)

## License 📜

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact 📧

For questions, feedback, and collaborations, please contact [Aminu Oluwarotimi Desmond](aminuoluwarotimi@gmail.com).

<a name="readme-top"></a>

<div align="center">
  <h1><b>Telco Churn Prediction App </b></h1>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents


- Overview
- [🛠 Built With ](#-built-with-)
- [Tech Stack ](#tech-stack-)
- Packages and Libraries
- Cleaning The Data
- Exploratory Data Analysis
- Visualizations
- Analysis
- Findings
- [Key Insights ](#key-insights-)
- [💻 Getting Started ](#-getting-started-)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Install](#install)
- [Usage](#usage)
- [👥 Authors ](#-authors-)
- [🔭 Future Features ](#-future-features-)
- [🤝 Contributing ](#-contributing-)
- [⭐️ Show your support ](#️-show-your-support-)
- [🙏 Acknowledgments ](#-acknowledgments-)
- [📝 License ](#-license-)

<!-- PROJECT DESCRIPTION -->

#  Buildin an App to Predict whether a customer will Churn in a Telecommunication Firm <a name="about-project"></a>

## Overview 

Machine learning is a vital tool for telecom companies to predict and mitigate customer churn. By analyzing data patterns, ML algorithms can anticipate customer behavior, identify dissatisfaction factors such as long wait times or rude service, and enhance self-service options. This proactive approach helps retain customers and maintain loyalty in an increasingly competitive and price-sensitive market.

## Data Sources 📊
- The dataset was provided in GitHub and SQL and was transformed to CSV format for transparency and reproductibility.
- Statistics on Telco Churn Rate.

## Topical Questions and Hypotheses
#### Questions 🤔:

ANALYTICAL QUESTIONS
The following analytical questions will help us gain insight and as well as confirm our hypothesis

1. How long Female and Male spent with Telco before Churning

2. What is the trend between Contract and churn

3. How long does it take each contract type before Churning

4. Which method of payment was prefered among the Senior Citizens and how much in total did both senior and non Senior citizens paid before churning

5. What is the churn trend for gender and dependents as well as their tenure

6. what is the trend between payment methods and gender and how it affect churning

7. What is the trend between tenure and paperlessBilling in relation to churn

8. What is the trend between tenure, Internet Service and senior citizen in relation to churn

9. What is the trend between StreamingMovies and senior citizen in relation to churn

10. How does internetService and OnlineSecurity affect churn

11. What is the trend between Contract and Payment Method in relation to churn

### Hypotheses 🔬:
#### A significance level (α) of 5% will used to perform all the hypothesis testing

The following hypothesis will be tested

1. The average number of churn for Female customers is greater than or equal to that of Male customers.

2. The average amount of TotalCharges for customers that churn is greater than or equal to those that did not churn.

3. The average number of tenure for customers that churn is less than or equal to those that did not churn

4. The average number of churn for customers that have Month_to_month contract is greater than or equal to those with 'One year' contract.

5. The average number of churn for customers that have Yes value for streamingTV is less than or equal to those with No values.

6. The average number of customers with dependents that will churn is greater than or equal to that of customers with no dependents.

7. The average number of churn for customers that have Yes values for seniorCitizen is greater than or equal to those with No values.

8. The PAYMENT METHOD does not influence customer churn

9. The average amount of TotalCharges for customers that churn is greater than or equal to those that did not churn
10. The average number of tenure for customers that churn is less than or equal to those that did not churn

11. The average number of churn for customers that have Month_to_Month contract is greater than or equal to those with 'One year' contract

12. Gender does not influence customer churn

13. The Internet service does not influence customer churn


###Data Dictionary
- customerID - Uniquely identify each customer
- gender - whether a customer is a Male or Female
- SeniorCitizen - whether customer is >60 years or not (Yes or No)
- Partner - Whether customer have a partner or not (Yes or No)
- Dependents - Whether customer have a dependents or not (Yes or No)
- tenure - How many months customer has been on the network
- PhoneService - Whether the customer is satisfied with the phone services
- MultipleLines - Whether the customer is satisfied with the multiple lines service
- InternetService - Whether the customer is satisfied with the internet service
- OnlineSecurity - whether the customer is satisfied with the online security service
- OnlineBackup - Whether the customer is satisfied with the onlince backup service
- DeviceProtection - Whether the customer is satisfied with the device protection service
- TechSupport - Whether the customer is satisfied with the tech support service
- StreamingTV - Whether the customer is satisfied with the streaming TV service
- StreamingMovies - Whether the customer is satisfied with the streaming Movies service
- Contract - Whether the customer opted for month-to-month, one-year and two-years contract with the Telco
- PaperlessBilling - Whether the customer is satisfied with the Paperless Billing service
- PaymentMethod - Whether the customer opted for electronic, mailed check, bank transfer and credit card payment methods
- MonthlyCharges - Monthly customer charges
- TotalCharges - Yearly customer charges
- Churn - Whether a customer will stop using the Telco's network or not (Yes and No)




## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>





<details>
<summary>Language</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
  </ul>
</details>


<details>
<summary>Database</summary>
  <ul>
    <li><a href="https://www.microsoft.com/en-us/sql-server">SQL</a></li>
  </ul>
</details>




## Packages and Libraries 📚
#### Collection of significant Python Libraries:
- Streamlit
- Pandas
- Numpy
- Seaborn
- Scipy
- Matplotlib
- Pyodbc
- Dotenv
- Sklearn
- Scikit
- Imblearn
- Custom Imputer
- XG Boost
- Pipeline


## Exploratory Data Analysis 🕵



- Univariate Analysis
  https://github.com/Koanim/LP2-Telco-churn-prediction/blob/main/box%20plot.JPG


  
- Bivariate Analysis
- https://github.com/Koanim/LP2-Telco-churn-prediction/blob/main/bivariate.JPG?raw=true





## Visualizations 👀

- Line Chart 📈
- Bar chart 📊
- Swarm Plot ◼▪◾

## Analysis 🔍
- Utilizing Python and data analysis libraries such as Pandas, Matplotlib, and Seaborn, we performed exploratory data analysis (EDA) to uncover trends and insights.
- We analyzed funding trends by year, sector-wise funding distribution, top investors, geographical distribution, and funding rounds.

## Machine Learning Models and Hyperparameter Tuning
-   Gradient_Boosting
-	Random_Forest	
-	XGBoost	
-   Naive_Bayes	
-   Logistic_Regression	
-   Support_Vector_Machine	
-   Decision_Tree	
-   K-Nearest_Neighbors	





## Findings 📈
- Total Charges and Tenure are highly positively correlated
- Customers that did not churn are more than those that churned.
- There are approximately 4000 non senior citizens among the telcos' customers compared to around 500 seniors

## Key Files 📂
- `LP2_telco_churn.ipynb`: Jupyter Notebook containing the code for data cleaning, EDA, and visualization.
- Raw data used for analysis.
>Telco_churn_git.csv
>Telco_churn_sql.csv
-`README.md`: This file providing an overview of the project.



<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- Features -->

## Key Insights <a name="key-features"></a>

- **Most non-senior Citizens are likely to churn compared to Senior citizens**
- **Customers using mailed or Electronic checks payment methods are more likely to churn**
- **Churning did not depend on gender**


<p align="right">(<a href="#readme-top">back to top</a>)</p>










<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>


To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project you need:

- Python


### Setup

Clone this repository to your desired folder:


```sh
  cd my-folder
  git clone hhttps://github.com/Koanim/Team-Lawrencium-Indian--startup-funding-Analysis-from-2018-to-2021
```

Change into the cloned repository

```sh
  cd Team-Lawrencium-Indian--startup-funding-Analysis-from-2018-to-2021
  
```

Create a virtual environment

```sh

python -m venv env

```

Activate the virtual environment

```sh
    env/Scripts/activate
```


### Install

Here, you need to recursively install the packages in the `requirements.txt` file using the command below 

```sh
   pip install -r requirements.txt
```



<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

- 🕵🏽‍♀️ **Victor Anim**                                [GitHub Profile](https://github.com/Koanim)   
- 🕵🏽‍♀️ **Aluko Oluwadamilola**                        [GitHub Profile](https://github.com/damzking?tab=repositories)
- 🕵🏽‍♀️ **Aminu Oluwarotimi Desmond**                  [GitHub Profile](https://github.com/bamzyyyy?tab=repositories)
- 🕵🏽‍♀️ **Nana Kwame Frimpong Baah**
- 🕵🏽‍♀️ **Leticia Blay**





<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>

We acknowledge the following persons for their coaching and support

- Racheal Appiah-Kubi
- Israel Anaba Ayamga

<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

