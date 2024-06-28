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

For the full list, please refer to the requirements.txt file


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

### Home Page
<img width="1190" alt="Screenshot 2024-06-26 at 3 09 04 AM" src="resources/homepage1.webp">

<img width="1115" alt="Screenshot 2024-06-26 at 3 09 16 AM" src="resources\homepage2.webp">

### Data Page
<img width='800' alt='Data page preview' src='resources\datapage1.webp'> 
<img width='800' alt='Data page preview' src='resources\datapage2.webp'>

### Dashboard Page
<img width='800' alt='Dashboard page preview' src='resources\dashboard1.webp'> 
<img width='800' alt='Dashboard page preview' src='resources\dashboard2.webp'>
<img width='800' alt='Dashboard page preview' src='resources\dashboard3.webp'>
<img width='800' alt='Dashboard page preview' src='resources\dashboard4.webp'>
<img width='800' alt='Dashboard page preview' src='resources\dashboard5.webp'>

### Predict Page
<img width='800' alt='Predict page preview' src='resources\predictpage1.webp'>
<img width='800' alt='Predict page preview' src='resources\predictpage2.webp'>
<img width='800' alt='Predict page preview' src='resources\predictpage3.webp'>
<img width='800' alt='Predict page preview' src='resources\predictpage4.webp'>

### History Page
<img width='800' alt='History page preview' src='resources\history1.webp'>


## Features ✅

**Customer Churn Prediction**: The app allows users to select their response based on predefined set of questions relating to demographics, service provisions by Telco, contract type, payment methods and charges. The user also have the option to choose between Xgboost, Gradient Boost and CatBoost models to make their prediction.

**Interactive Interface**: Streamlit provides an interactive, easy-to-use, web-based interface.

## Usage Instructions 📋

- Input Fields: The app displays input fields for the Gender, Seniorcitizen, Partner, Dependent, Tenure, Phoneservice, MultipleLines, InternetService, Onlinesecurity, onlinebackup, DeviceProtection, Monthlycharges, Totalcharges, Contracttype, Paperlessbilling, PaymentMethod, TechSupport, DeviceProtection, StreamingTV and StreamingMovies.
  
- Results: The app will display the predicted Churn rate for the specified inputs.

## Author 👨‍💼

  | Name                                            | LinkedIn                                                                                                                                                                                                                                               | Medium Article |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Victor Nyarko Anim | [My LinkedIn](https://www.linkedin.com/in/victor-anim-83115818/) |[My First Machine Learning App 🎉 for Predicting Telco customer Churn! Using Streamlit.👏](https://medium.com/@victor.nyarko/my-first-machine-learning-app-for-predicting-telco-customer-churn-50bfdb2ecb30)|

[App Link](https://lp4-telco-customer-churn-prediction-app-2.onrender.com/)

## Model Training and Saving ⏳

The Xgboost, Catboost and Gradient boost model was trained using the Telecommunication Customer Churn as shown in this GitHub repository: [LP4-Telco-Customer-Churn-Prediction-APP
](https://github.com/Koanim/LP4-Telco-Customer-Churn-Prediction-APP/).
## Acknowledgments 🙏

I would like to express my gratitude to the [Azubi Africa Data Analyst Program](https://www.azubiafrica.org/data-analytics) for their support and for offering valuable projects as part of this program. Not forgeting my scrum masters on this project [Rachel Appiah-Kubi](https://www.linkedin.com/in/racheal-appiah-kubi/) & [Emmanuel Koupoh](https://github.com/eaedk)

## License 📜

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact 📧

For questions, feedback, and collaborations, please contact via [email](victor.nyarko@ymail.com).



<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- SUPPORT -->

## ⭐️ Show your support <a name="support"></a>

If you like this project kindly show some love, give it a 🌟 **STAR** 🌟

<p align="right">(<a href="#readme-top">back to top</a>)</p>


