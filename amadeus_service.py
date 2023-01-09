from amadeus import Client, ResponseError
def safety_rated_locations():
    amadeus = Client(
        client_id=YOUR_CLIENT_ID,
        client_secret=YOUR_CLIENT_SECRET
    )
    try:
        response = amadeus.safety.safety_rated_locations.by_square.get(
            north=40.742278,
            west=-74.105833,
            south=40.701278,
            east=-73.971973
        )
        
        return response.data
    except ResponseError as error:
        raise error