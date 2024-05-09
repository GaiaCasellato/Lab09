from database.DB_connect import DBConnect
from model.Areoporto import Areoporto
from model.Rotta import Rotta
from model.Volo import Volo


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllAreoporti():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ("""SELECT * 
                 FROM airports a""")
        cursor.execute(query)

        for row in cursor:
            result.append(Areoporto(row["ID"], row["IATA_CODE"], row["AIRPORT"], row["CITY"], row["STATE"],
                                    row["COUNTRY"], row["LATITUDE"],row["LONGITUDE"], row["TIMEZONE_OFFSET"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllVoli():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ("""SELECT * 
                    FROM flights f""")
        cursor.execute(query)

        for row in cursor:
            result.append(Volo(row["ID"], row["AIRLINE_ID"], row["FLIGHT_NUMBER"], row["TAIL_NUMBER"], row["ORIGIN_AIRPORT_ID"],
                               row["DESTINATION_AIRPORT_ID"], row["SCHEDULED_DEPARTURE_DATE"], row["DEPARTURE_DELAY"],
                               row["ELAPSED_TIME"], row["DISTANCE"], row["ARRIVAL_DATE"], row["ARRIVAL_DELAY"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getRotte():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = ("""SELECT ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID, AVG(DISTANCE) 
                    FROM flights f
                    GROUP BY ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID""")
        cursor.execute(query)

        for row in cursor:
            result.append(Rotta(row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"], row["AVG(DISTANCE)"]))
        cursor.close()
        conn.close()
        return result
