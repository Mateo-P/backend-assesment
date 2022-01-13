def parse_legs(legs, Leg, Airline):
    legs_to_create = []
    for leg in legs:
        try:
            id = leg['id']
            Leg.objects.get(api_id=id)
        except Leg.DoesNotExist:
            try:
                name = leg['airline_name']
                departure_airport = leg['departure_airport']
                departure_time = leg['departure_time']
                arrival_airport = leg['arrival_airport']
                arrival_time = leg['arrival_time']
                stops = int(leg['stops'])
                duration_mins = int(leg['duration_mins'])
                airline = Airline.objects.get(
                    api_id=id)
            except Airline.DoesNotExist:
                airline = Airline(
                    api_id=id,
                    name=name
                )
                airline.save()
            parsed_leg = Leg(
                api_id=id,
                departure_airport=departure_airport,
                departure_time=departure_time,
                arrival_airport=arrival_airport,                    arrival_time=arrival_time,
                stops=stops,
                duration_mins=duration_mins,
                airline=airline
            )
            legs_to_create.append(parsed_leg)
    Leg.objects.bulk_create(legs_to_create)