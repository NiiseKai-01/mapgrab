import os, requests, time, json

url = "https://serpapi.com/search"
nav_url = "https://www.google.com/maps/place/?q=place_id:"

def process_data(places,results,index):
    for place in places:
            place_id = place.get("place_id")
            map_link = nav_url+place_id
            coords = place.get("gps_coordinates", {})
            results.append({
                "INDEX":index,
                "NAME":place.get("title"),
                "ADDRESS":place.get("address"),
                "PHONE_NUMBER":place.get("phone","-"),
                "RATING":place.get("rating","-"),
                "REVIEWS":place.get("reviews","-"),
                "PRICE":place.get("price","-"),
                "TYPE":place.get("type","-"),
                "OPERATING_HOURS":place.get("hours","-"),
                "GOOGLE_MAPS_LINK":map_link,
                "LATITUDE": coords.get("latitude"),
                "LONGITUDE": coords.get("longitude")
            })
            index += 1
            if index > 100:
                break
    return results,index

def jsfetcher(query):
    results = []
    index = 1

    #demo mode
    if query.lower() == "demoliveshowcase":
         with open("sample.json", "r") as file:
            data = json.load(file)
            places = data.get("local_results",[])
            results, index = process_data(places,results,index)
            return results
         
    #live mode
    for i in range(5):
        params = {
            "engine": "google_maps",
            "q": query,
            "start": i*20,
            "api_key":os.getenv("SERPAPI_KEY")
        }
        response = requests.get(url=url,params=params,timeout=10)
        if response.status_code != 200:
            break
        data = response.json()
        places = data.get("local_results",[])
        if not places:
            print("No more results, stopping...")
            break
        results, index = process_data(places, results, index)
        if index > 100:
            break        
        time.sleep(1)
    return results