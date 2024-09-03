# Giant Bomb API class

Write a python class with a method that will take a game title and return a link to the artwork for that game using the Giant Bomb API. 

Here is an example of a URL for the giant bomb API: https://www.giantbomb.com/api/games/?api_key={{API_KEY}}&format=json&filter=name:{GAME_TITLE}&field_list=name,image. 

The response will be a JSON object with a list of games. We want the game in the list that matches the value we pass to 'GAME_TITLE'. 

The response will have a key called "results" which will have a list of games. We want the game that has the same name as the game title we passed in. 

The response will have a key called "image" which will be a JSON object of artwork for the game. We want the value of the "original_url" key.

Remember, the method should accept a game title and return a link to the artwork for that game.

Please include error handling. If the API responds with an error, raise the error. If the API succeeds but there is no game with the given title, return None. 

Here is the documentation for the Giant Bomb API: https://www.giantbomb.com/api/documentation/#toc-0-22

Here is an example of the JSON response:

{
    "error": "OK",
    "limit": 100,
    "offset": 0,
    "number_of_page_results": 1,
    "number_of_total_results": 1,
    "status_code": 1,
    "results": [
        {
            "image": {
                "icon_url": "https://www.giantbomb.com/a/uploads/square_avatar/20/201266/3532465-2909474649-co4jn.jpg",
                "medium_url": "https://www.giantbomb.com/a/uploads/scale_medium/20/201266/3532465-2909474649-co4jn.jpg",
                "screen_url": "https://www.giantbomb.com/a/uploads/screen_medium/20/201266/3532465-2909474649-co4jn.jpg",
                "screen_large_url": "https://www.giantbomb.com/a/uploads/screen_kubrick/20/201266/3532465-2909474649-co4jn.jpg",
                "small_url": "https://www.giantbomb.com/a/uploads/scale_small/20/201266/3532465-2909474649-co4jn.jpg",
                "super_url": "https://www.giantbomb.com/a/uploads/scale_large/20/201266/3532465-2909474649-co4jn.jpg",
                "thumb_url": "https://www.giantbomb.com/a/uploads/scale_avatar/20/201266/3532465-2909474649-co4jn.jpg",
                "tiny_url": "https://www.giantbomb.com/a/uploads/square_mini/20/201266/3532465-2909474649-co4jn.jpg",
                "original_url": "https://www.giantbomb.com/a/uploads/original/20/201266/3532465-2909474649-co4jn.png",
                "image_tags": "All Images"
            },
            "name": "Elden Ring"
        }
    ],
    "version": "1.0"
}

The API key is stored in the .env file with key name GIANT_BOMB_API_KEY. 