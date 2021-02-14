import json
import urllib.request

CONVERSION_FACTIOR = 250

# Main function which will run loop until there are no new pages to read in API
def main():
    weights = []
    url_base = "http://wp8m3he1wt.s3-website-ap-southeast-2.amazonaws.com"
    url_api = "/api/products/1"

    while True:
        url = url_base + url_api
        data = get_data(url)
        append_cubic_weight(weights, data)

        if(data["next"] == None):
            break
        else:
            url_api = data["next"]

    average_weight(weights)

# Funtion to access data from API and convert it into JSON
def get_data(url):
    res = urllib.request.urlopen(url)
    return json.loads(res.read())


# Function to populate list with cubic weight for every Air Conditoner
def append_cubic_weight(weights, data):
    for objects in data["objects"]:
        if(objects["category"] == "Air Conditioners"):
            dimensions = get_dimensions(objects)
            weights.append(get_cubic_weight(dimensions))


# Function to retrieve dimension of Air Conditioner and converting every dimension into cm
def get_dimensions(i):
    w = i["size"]["width"] / 100
    l = i["size"]["length"] / 100
    h = i["size"]["height"] / 100
    return (w, l, h)


# Function to calculate cubic weight of 1 Air Conditioner
def get_cubic_weight(dimensions):
    return round(dimensions[0] * dimensions[1] * dimensions[2] * CONVERSION_FACTIOR, 3)


# Function to calculate average weight of all Air Conditoners
def average_weight(weight):
    total_weight = sum(weight)
    average = round(total_weight/len(weight), 3)
    print("\nAverage weight for {} Air Conditioners is {}kg\n".format(
        len(weight), average))


if __name__ == "__main__":
    main()
    
