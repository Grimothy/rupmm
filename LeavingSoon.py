import os
from datetime import datetime, timedelta
from arrapi import RadarrAPI

# Radarr API details
radarr_url = "https://radarr.bearald.com"
api_key = "a46bc0b141cb40308d02fb26aad7fb6b"

# Connect to Radarr API using arrapi
radarr = RadarrAPI(radarr_url, api_key)

# Define the time span (in days)
days_ago = 60
cutoff_date = datetime.now() - timedelta(days=days_ago)

# Get the list of movies from Radarr
movies = radarr.all_movies()

# Filter movies added 60 days ago or longer and have the file downloaded
filtered_movies = [movie for movie in movies if movie.added <= cutoff_date and movie.hasFile]

# Generate HTML content with CSS styles for the new layout
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Movie List</title>
<link href="https://fonts.googleapis.com/css2?family=Playwrite+DE+Grund&display=swap" rel="stylesheet">
<style>
body {
    font-family: 'Montserrat', sans-serif;
    background-image: url('background.jpg');
    background-attachment: fixed;
    background-size: cover;
    background-position: 50% 0%;
    margin: 0;
    padding: 20px;
    overflow-x: hidden;
}
body::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to bottom, rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.7) 25%, rgba(0, 0, 0, 0.7) 75%, rgba(0, 0, 0, 0.9));
    pointer-events: none; /* Allow clicks to pass through the overlay */
    z-index: 1; /* Place the overlay on top */
}
h1 {
    text-align: center;
    font-size: 3em;
    color: #333333;  /* Updated to dark gray */
    font-family: 'Playwrite DE Grund', cursive;
    background: linear-gradient(135deg, #f39c12, #8e44ad);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    transition: transform 0.3s ease-in-out;
    position: relative;
    z-index: 2; /* Ensure the title is above the overlay */
}
h1:hover {
    transform: scale(1.1);
}
.subheading {
    text-align: center;
    font-size: 1.2em;
    color: #FFFFFF; /* Light font color for better visibility */
    font-family: 'Playwrite DE Grund', cursive;
    margin-top: -10px; /* Adjust the margin as needed */
    position: relative;
    z-index: 2; /* Ensure the subheading is above the overlay */
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Added subtle drop shadow for better contrast */
}
.movie-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    padding: 0;
}
.movie-item {
    background-color: rgba(0, 0, 0, 0.7); /* Darker and more transparent */
    border-radius: 10px;
    margin: 20px;
    width: 300px;
    text-align: center;
    padding: 10px;
    transition: transform 0.5s, box-shadow 0.5s, filter 1.5s; /* Added filter transition */
    position: relative;
    z-index: 2; /* Ensure the movie items are above the overlay */
}
.movie-item:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.5); /* Darker shadow on hover */
}
.movie-item.blurred {
    filter: blur(1px); /* Reduced blur effect */
    transition: filter 1.5s; /* Slow down the blur effect */
}
.movie-title {
    font-size: 2em;
    color: #fff; /* Set to white for better contrast */
    margin: 10px 0;
    font-family: 'Montserrat', sans-serif;
}
.movie-img {
    border-radius: 10px;
    width: 100%;
    height: auto;
    margin-bottom: 10px;
}
.movie-details {
    font-size: 1.5em; /* Adjusted size to be 25% smaller than the title */
    color: #fff; /* Set to white for better contrast */
    font-family: 'Montserrat', sans-serif;
    font-weight: bold; /* Made the text bolder */
}
</style>
<script>
document.addEventListener("DOMContentLoaded", function() {
    const movieItems = document.querySelectorAll(".movie-item");
    
    movieItems.forEach(item => {
        item.addEventListener("mouseover", function() {
            movieItems.forEach(mi => {
                if (mi !== item) {
                    mi.classList.add("blurred");
                } else {
                    mi.classList.remove("blurred");
                }
            });
        });

        item.addEventListener("mouseout", function() {
            movieItems.forEach(mi => {
                mi.classList.remove("blurred");
            });
        });
    });
});
document.addEventListener("scroll", function() {
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    let docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    let scrollPercent = scrollTop / docHeight;
    let bgPosition = Math.round(scrollPercent * 100);
    document.body.style.backgroundPosition = `50% ${bgPosition}%`;
});
</script>
</head>
<body>
<h1>Leaving Soon</h1>
<p class="subheading">Let's keep this operation going! Please vote to keep the media that may be expiring but you want to watch later.</p>
<div class="movie-list">
"""

# Generate HTML content for filtered movies
for movie in filtered_movies:
    image_url = radarr_url.rstrip('/') + movie.images[0].url
    # Add movie details to HTML content with new date format
    formatted_date = movie.added.strftime("%B %d %Y")
    html_content += f"""
    <div class="movie-item">
        <h2 class="movie-title">{movie.title}</h2>
        <img class="movie-img" src="{image_url}" alt="{movie.title}">
        <div class="movie-details">Originally Added: {formatted_date}</div>
    </div>
    """

html_content += """
</div>
</body>
</html>
"""

# Save the HTML content to a file in the current directory
current_directory = os.getcwd()
html_file_path = os.path.join(current_directory, "movies_list.html")
with open(html_file_path, 'w') as html_file:
    html_file.write(html_content)

# Print the directory where the file was saved
saved_directory = os.path.abspath(html_file_path)
print(f"HTML file generated and saved at: {saved_directory}")