class UndergroundSystem:
    # lc sol
    # tc O(1)
    # sc O(P + S^2) ???
    # -> the check_in_data hm: the maximum size this HashMap could be is the maximum possible number of passengers making a journey at the same time
    # -> This HashMap has one entry for each pair of stations that has had at least one passenger start and end a journey at those stations. Over time, we could reasonably expect every possible pair of the SS stations on the network to have an entry in this HashMap, which would be O(S^2)

    def __init__(self):
        self.check_in_data = {}
        self.journey_data = collections.defaultdict(lambda : [0, 0])
                
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = [stationName, t]

    def checkOut(self, id: int, end_station: str, t: int) -> None:
        # Access and remove the data for id. Note that removing it is actually
        # optional, but we'll discuss the benefits of it in the space complexity
        # analysis section.
        start_station, start_time = self.check_in_data.pop(id)
        self.journey_data[(start_station, end_station)][0] += (t - start_time)
        self.journey_data[(start_station, end_station)][1] += 1
            
    def getAverageTime(self, start_station: str, end_station: str) -> float:
        total_time, total_trips = self.journey_data[(start_station, end_station)]
        # The average is simply the total divided by the number of trips.
        return total_time / total_trips