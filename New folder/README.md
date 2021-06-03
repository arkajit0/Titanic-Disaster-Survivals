# Titanic-Disaster-Survivals

Titanic Disaster survival prediction deployment URL: https://disaster-survival-prediction.herokuapp.com/

## Introduction
#### In this project we will build a classification model where according to different features we can tell if a person has survived or not in titanic disaster.
#### The dataset used has 12 columns that we will divide into 11 features and 1 target column
***The Columns are Given as:***

- PassengerId: This is the onboard passenger's Id Number
- Survived: Person survived or not(0: has not survived, 1: has survived)
- Pclass: Passenger Class  
- Name: Passenger Name
- Sex: Passenger Gender
- Age: Passenger Age
- SibSp: Number of Siblings/Spouses Aboard
- Parch: Number of Parents/Children Aboard
- Ticket: Ticket Number
- Fare: Passenger Fare (British pound)
- Cabin: Cabin Code
- Embarked: Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

### Instruction to run the file
***Step 1***
**Create and activate an environment**
- Using Conda <br>
conda create -n [your environment name] python=3.7 <br>
Then activate the environment by writing <br>
conda activate [your environment name] <br>

- Using default Environments <br>
python3 -m venv [your environment name] <br>
Then activate the environment by writing <br>
[your environment name]\Scripts\activate.bat [For windows users] <br>
source [your environment name]/bin/activate [For Mac/Ubuntu users] <br>

NOTE: you can give any python version and ignore brackets while giving environment name

***Step 2***
**Install Dependencies**
- For library installations  write <br>
pip install -r requirements.txt 

***Step 3***
**Run The File**
- To run the file write <br>
python app.py
