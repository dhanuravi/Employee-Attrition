# Attrition predictor
Attrition predictor is a end to end Flask application that predicts whether `a employee will move out of company or will stay`.

## URL
Run this App [HERE](https://attrition-predic.herokuapp.com/)

Created By
----------
Sri hari K V
https://bit.ly/34R7lrj

## Dataset
Thanks to Kaggle
You can find dataset [HERE](https://www.kaggle.com/pavansubhasht/ibm-hr-analytics-attrition-dataset)

## installation
one can install required packages for this application using 
```bash
pip install -r requirements
```
## Separate environment
Alwas create a separate `conda environment/any environment` so that you can avoid version errors between packages

## usage
After installing the required packages use the following command to start the flask app
```bash
python app.py
```

## folder structure
```bash
'
.
├── ada.pkl
├── xg.pkl
├── gb.pkln 
├── Procfile                                     #file for Heroku deployment
├── README.md
├── WA_Fn-UseC_-HR-Employee-Attrition.csv.csv     #dataset
├── data.py                                       #data from UI are decoded for model using this
├── attrition_classification.ipynb                #File which generated all pkl files
├── requirements.txt
├── test_list.py                                  #models got tested here
├── app.py                                        #web server gateway Interface
```

## Important Tools used
* python 3.7
* anaconda-jupyternotebook
* conda environment
* flask

## Steps for training models
* Drop EmployeeCount,StandardHours,Over18 - contains single unique values
* Check for `Null` values and remove them using `mean imputation`
* Encoding all the labels in data using `sklearn.preprocessing-LabelEncoder`
* Visualise `correlation` between each variable and target(attition)
* Check `Multicollinearity` using Variable Inflation Factors (VIF)
* split into `train and test` data - `0.8:0.2`
* `normalize` using StandardScaler
* should not use accuracy as metric since this is `imbalance data`, since this is attrition,`false negatives are more costly than false positives`, `Recall` will be better
* Tune hyperparameter (learning rate)
* Fitting models
* Ensembling the results using mode

## Models used
* gradient boosting
* XG boost
* ada boost



## Accuracy range
The overall accuracy range was between `85 to 87`
recall is above 90 for all 3 model, better results

## Input 
Fill the Information about customer required by model in web app's UI

## Output
It will say whether
    `this employee will stay`
                or
    `this employee will leave`

## Deployment
This Application is Deployed in Heroku Platform. 
To Run this App [CLICK HERE](https://attrition-predic.herokuapp.com/)
