import requests

# Your server URL and API key
server_url = "https://r1.bearald.com"
api_key = "MTczNDkwMjk1MDg5ODY2YWNhZTdmLTRhZjktNDQ1Ny1hZDUzLTBhMThiYmMzZGIxNg=="

# Endpoint to get trending movies
trending_movies_endpoint = f"{server_url}/api/v1/discover/trending?page=1&language=en"

# Headers with API key
headers = {
    "X-Api-Key": api_key
}

# Make a request to the API
response = requests.get(trending_movies_endpoint, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    trending_movies = response.json()
    for movie in trending_movies.get("results", []):
        original_title = movie.get("originalTitle")
        poster_path = movie.get("posterPath")
        print(f"Title: {original_title}")
        print(f"Poster URL: {server_url}{poster_path}")
        print()
else:
    print(f"Failed to retrieve trending movies. Status code: {response.status_code}")
