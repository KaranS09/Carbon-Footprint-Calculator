from website import app
from flask import render_template,redirect, url_for, request
import requests
import json



# url = "https://beta3.api.climatiq.io/estimate"
# headers = {
#     "Authorization": "Bearer ZKNZQ2NHGW4F8QGEG19AVJ4Z1HXN",
#     "Content-Type": "application/json"
# }
# data = {
#     "emission_factor": {
#         "activity_id": "passenger_vehicle-vehicle_type_lower_medium_car-fuel_source_bev-engine_size_na-vehicle_age_na-vehicle_weight_na",
#         "source": "BEIS",
#         "region": "GB",
#         "year": "2021",
#         "lca_activity": "electricity_generation"
#     },
#     "parameters": {
#         "distance": 10,
#         "distance_unit": "km"
#     }
# }

# response = requests.post(url, headers=headers, json=data)

# print(response.json())



@app.route('/home')
def index_page():
 return render_template('home.html')

@app.route('/')
@app.route('/index', methods=['GET','POST'])
def home_page():
 distanceEV = 0
 co2e_totalEV = 0
 co2e_total = 0
 distance = 0
 co2EV = 0
 co2 = 0
 n2oEV = 0
 n2o = 0
 ch4 = 0
 ch4EV = 0
 moneyRT = 0
 money = 0
 moneywaste = 0
 energy = 0
 co2en = 0
 co2e_totalen = 0
 n2oen = 0
 ch4en = 0
 co2mw = 0
 co2e_totalmw = 0
 n2omw = 0
 ch4mw = 0
 co2e_totalRT = 0
 co2e_totalm = 0
 co2RT = 0
 co2m = 0
 n2oRT = 0
 n2om = 0
 ch4RT = 0
 ch4m = 0
 if request.method == "POST":
    if "submit1" in request.form:
        print(request.form)
        distanceEV = int(request.form.get('distanceEV'))
        distance = int(request.form.get('distance'))
    if "submit2" in request.form:
        print(request.form)
        moneyRT = int(request.form.get('moneyRT'))
        money = int(request.form.get('money'))
    if "submit3" in request.form:
        print(request.form)
        energy = int(request.form.get('energy'))
    if "submit4" in request.form:
        print(request.form)
        moneywaste = int(request.form.get('moneywaste'))
 if moneyRT != 0: 
  url = "https://beta3.api.climatiq.io/estimate"
  headers = {
    "Authorization": "Bearer ZKNZQ2NHGW4F8QGEG19AVJ4Z1HXN",
    "Content-Type": "application/json"
  }
  data = {
    "emission_factor": {
        "activity_id": "general_retail-type_retail_trade_except_of_motor_vehicles_motorcycles_repair_of_personal_household_goods_services",
        "source": "EXIOBASE",
        "region": "GB",
        "year": "2021",
        "lca_activity": "unknown"
    },
    "parameters": {
        "money": moneyRT,
        "money_unit": "usd"
    }
    }

  response = requests.post(url, headers=headers, json=data)
  response_json = json.loads(response.content)

  co2e_totalRT = response_json['constituent_gases']['co2e_total']
  co2RT = response_json['constituent_gases']['co2']
  ch4RT = response_json['constituent_gases']['ch4']
  n2oRT = response_json['constituent_gases']['n2o']

  print(f"co2e_total: {co2e_totalRT}")
  print(f"co2: {co2RT}")
  print(f"ch4: {ch4RT}")
  print(f"n2o: {n2oRT}")
 if money != 0: 
  url = "https://beta3.api.climatiq.io/estimate"
  headers = {
    "Authorization": "Bearer ZKNZQ2NHGW4F8QGEG19AVJ4Z1HXN",
    "Content-Type": "application/json"
  }
  data = {
   "emission_factor": {
        "activity_id": "consumer_goods-type_food_products_not_elsewhere_specified",
        "source": "EXIOBASE",
        "region": "AT",
        "year": "2021",
        "lca_activity": "unknown"
    },
    "parameters": {
        "money": money,
        "money_unit": "usd"
    }
    }
  response = requests.post(url, headers=headers, json=data)
  response_json = json.loads(response.content)

  co2e_totalm = response_json['constituent_gases']['co2e_total']
  co2m = response_json['constituent_gases']['co2']
  ch4m = response_json['constituent_gases']['ch4']
  n2om = response_json['constituent_gases']['n2o']

  print(f"co2e_total: {co2e_totalm}")
  print(f"co2: {co2m}")
  print(f"ch4: {ch4m}")
  print(f"n2o: {n2om}")
 if moneywaste != 0: 
  url = "https://beta3.api.climatiq.io/estimate"
  headers = {
    "Authorization": "Bearer ZKNZQ2NHGW4F8QGEG19AVJ4Z1HXN",
    "Content-Type": "application/json"
  }
  data = {
    "emission_factor": {
        "activity_id": "waste_management-type_food_waste_for_treatment_waste_water_treatment",
        "source": "EXIOBASE",
        "region": "IN",
        "year": "2021",
        "lca_activity": "unknown"
    },
    "parameters": {
        "money": moneywaste,
        "money_unit": "usd"
    }
    }
  response = requests.post(url, headers=headers, json=data)
  response_json = json.loads(response.content)

  co2e_totalmw = response_json['constituent_gases']['co2e_total']
  co2mw = response_json['constituent_gases']['co2']
  ch4mw = response_json['constituent_gases']['ch4']
  n2omw = response_json['constituent_gases']['n2o']

  print(f"co2e_total: {co2e_totalmw}")
  print(f"co2: {co2mw}")
  print(f"ch4: {ch4mw}")
  print(f"n2o: {n2omw}")
 if distanceEV != 0: 
  url = "https://beta3.api.climatiq.io/estimate"
  headers = {
    "Authorization": "Bearer ZKNZQ2NHGW4F8QGEG19AVJ4Z1HXN",
    "Content-Type": "application/json"
  }
  data = {
    "emission_factor": {
        "activity_id": "passenger_vehicle-vehicle_type_lower_medium_car-fuel_source_bev-engine_size_na-vehicle_age_na-vehicle_weight_na",
        "source": "BEIS",
        "region": "GB",
        "year": "2021",
        "lca_activity": "electricity_generation"
    },
    "parameters": {
        "distance": distanceEV,
        "distance_unit": "km"
    }
  }
  response = requests.post(url, headers=headers, json=data)
  response_json = json.loads(response.content)

  co2e_totalEV = response_json['constituent_gases']['co2e_total']
  co2EV = response_json['constituent_gases']['co2']
  ch4EV = response_json['constituent_gases']['ch4']
  n2oEV = response_json['constituent_gases']['n2o']

  print(f"co2e_total: {co2e_totalEV}")
  print(f"co2: {co2EV}")
  print(f"ch4: {ch4EV}")
  print(f"n2o: {n2oEV}")

 if energy != 0: 
    print("here")
    url = "https://beta3.api.climatiq.io/estimate"
    headers = {
    "Authorization": "Bearer ZKNZQ2NHGW4F8QGEG19AVJ4Z1HXN",
    "Content-Type": "application/json"
    }
    data = {
    "emission_factor": {
        "activity_id": "electricity-energy_source_grid_mix",
        "source": "ADEME",
        "region": "ZA",
        "year": "2021",
        "lca_activity": "electricity_generation"
    },
    "parameters": {
        "energy": energy,
        "energy_unit": "kWh"
    }
    }
    response = requests.post(url, headers=headers, json=data)
    response_json = json.loads(response.content)

    co2e_totalen = response_json['constituent_gases']['co2e_total']
    co2en = response_json['constituent_gases']['co2']
    ch4en = response_json['constituent_gases']['ch4']
    n2oen = response_json['constituent_gases']['n2o']

    print(f"co2e_total: {co2e_totalEV}")
    print(f"co2: {co2EV}")
    print(f"ch4: {ch4EV}")
    print(f"n2o: {n2oEV}")

 if distance != 0: 
   url = "https://beta3.api.climatiq.io/estimate"
   headers = {
    "Authorization": "Bearer ZKNZQ2NHGW4F8QGEG19AVJ4Z1HXN",
    "Content-Type": "application/json"
   }
   data = {
"emission_factor": {
"activity_id": "passenger_vehicle-vehicle_type_car-fuel_source_na-engine_size_na-vehicle_age_na-vehicle_weight_na",
"source": "BEIS",
"region": "GB",
"year": "2022",
"lca_activity": "fuel_combustion"
},
"parameters": {
"distance": 10,
"distance_unit": "km"
}
}




   response = requests.post(url, headers=headers, json=data)
   response_json = json.loads(response.content)
   print(response_json)
   co2e_total = response_json['constituent_gases']['co2e_total']
   co2 = response_json['constituent_gases']['co2']
   ch4 = response_json['constituent_gases']['ch4']
   n2o = response_json['constituent_gases']['n2o']

   print(f"co2e_total: {co2e_total}")
   print(f"co2: {co2}")
   print(f"ch4: {ch4}")
   print(f"n2o: {n2o}")


 return render_template('temp.html', co2e_totalEV = co2e_totalEV, co2e_total = co2e_total,co2EV = co2EV, n2oEV = n2oEV, ch4EV = ch4EV, co2 = co2, n2o = n2o, ch4 = ch4, co2e_totalen = co2e_totalen, co2en = co2en, n2oen = n2oen, ch4en = ch4en, co2mw = co2mw, co2e_totalmw = co2e_totalmw, ch4mw = ch4mw, n2omw = n2omw, co2e_totalRT = co2e_totalRT, co2RT = co2RT, ch4RT = ch4RT, n2oRT = n2oRT, co2e_totalm = co2e_totalm, co2m = co2m, n2om = n2om, ch4m = ch4m)