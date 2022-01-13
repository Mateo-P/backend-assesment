def parse_itineraries(itineraries, Itinerary, Agent, Leg):
    for itinerary in itineraries:
        try:
            id = itinerary["id"]
            Itinerary.objects.get(api_id=id)
        except Itinerary.DoesNotExist:
            try:
                name = itinerary['agent']
                rating = itinerary["agent_rating"]
                id_legs = itinerary['legs']
                price = float(itinerary['price'][1:])
                agent = Agent.objects.get(name=name)
            except Agent.DoesNotExist:
                agent = Agent(name=name, rating=rating)
                agent.save()
            related_legs = Leg.objects.filter(api_id__in=id_legs)
            parsed_itinerary = Itinerary(
                api_id=id,
                price=price,
                agent=agent
            )
            parsed_itinerary.save()
            parsed_itinerary.legs.set(related_legs)
