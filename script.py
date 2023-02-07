import requests

url = input("Enter the URL of the image: ")

response = requests.get(url)

# Get the file name from the URL entered
filename = url.split("/")[-1]

# Simply write to a file
with open(filename, "wb") as f:
    f.write(response.content)
