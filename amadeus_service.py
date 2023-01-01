from amadeus import Client, ResponseError
def safety_rated_locations():
    amadeus = Client(
        client_id='REPLACE_BY_YOUR_API_KEY',
        client_secret='REPLACE_BY_YOUR_API_SECRET'
    )
    try:
        amadeus.safety.safety_rated_locations.by_square.get(
            north=40.742278,
            west=-74.105833,
            south=40.701278,
            east=-73.971973
        )
        print(response.data)
        return response.data
    except ResponseError as error:
        raise error
