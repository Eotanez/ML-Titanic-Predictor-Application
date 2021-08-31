def logistic_model_1(age, gender, pclass, fare):
  
  """ 
  Arguments:
  Age == int 
  Gender == string (male or female)
  Class == int (1,2, or 3)
  Fare == int 

  Returns:
  Survival_code == int (1 survived; 0 died)
  """

  import pickle 
  import pandas as pd
  clf = pickle.load(open("model_ml.sav", 'rb'))

  # handle gender encoding
  male = 0
  female = 0
  if (gender == "male"):
    male = 1
  else:
    female = 1
  
  # handle class encoding
  pclass1 = 0
  pclass2 = 0
  pclass3 = 0
  if(pclass == 1):
    pclass1 = 1
  elif(pclass == 2):
    pclass2 = 1
  else:
    pclass3 = 1
  
  # handle fare encoding
  cheapest = 0
  cheap = 0
  medium = 0
  expensive = 0
  most_expensive = 0
  if(float(fare) < 8.05):
    cheapest = 1
  elif(float(fare) < 15.7417):
    cheap = 1
  elif(float(fare) < 33.375):
    medium = 1
  elif(float(fare) < 100):
    expensive = 1
  else:
    most_expensive = 1
  
  user_df = pd.DataFrame({
    "Age": age,
    "Sex_female": female,	
    "Sex_male": male,	
    "Pclass_1": pclass1,	
    "Pclass_2": pclass2,	
    "Pclass_3": pclass3,	
    "Fare cat._cheapest": cheapest,	
    "Fare cat._cheap": cheap,	
    "Fare cat._medium": medium,	
    "Fare cat._expensive": expensive,	
    "Fare cat._most expensive": most_expensive
  }, index=[0])

  return clf.predict(user_df)[0]
  
print(logistic_model_1(22,"male",1,200))