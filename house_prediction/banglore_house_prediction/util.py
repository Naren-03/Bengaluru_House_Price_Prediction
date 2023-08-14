import json,pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')


data = None
locations = None
model = None

def get_price(location,sqft,bhk,bath):
    try:
        loc_index = data.index(location.lower())
    except:
        loc_index = -1

    X = np.zeros(len(data))
    X[0] = sqft
    X[1] = bath
    X[2] = bhk
    if loc_index >=0:
        X[loc_index] = 1
    return abs(round((model.predict([X])[0]),2))

def getloc():
    return locations

def extract_data():
    global data
    global locations
    global model

    with open('D:\All Python Programs\ML Project\house_prediction\house_prediction\static\columns.json', 'r') as file:
        data = json.load(file)['data_columns']
        locations = data[3:]

    with open(r'D:\All Python Programs\ML Code\ML Project-1\server\artifacts\home_price_model.pickel','rb') as f:
        model = pickle.load(f)

    # print(data)
    # print(locations)

if __name__=="__main__":
    extract_data()
    print("\n",get_price("nagarbhavi",1000,2,3),"Lakh")
    print("\n",get_price("basaveshwara nagar",1000,2,3),"Lakh")
    print("\n",get_price("banjara",1000,2,3),"Lakh")
    print(getloc())