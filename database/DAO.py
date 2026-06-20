from database.DB_connect import DBConnect
from model.circuit import Circuit
from model.results import Results


class DAO():
    @staticmethod
    def getAllCircuits():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                    from circuits"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row)

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllYears():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT distinct year
                    from seasons"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["year"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllCircuits():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                    from circuits"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Circuit(row["circuitId"], row["circuitRef"], row["name"], row["location"],
                               row["country"], row["lat"], row["lng"], row["alt"], row["url"], {}))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getYearofCircuit(circuitId, year1, year2):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct ra.year
                from circuits c, races ra, results re
                where c.circuitId = ra.circuitId 
                and ra.raceId = re.raceId
                and c.circuitId = %s
                and ra.year between %s and %s"""

        cursor.execute(query, (circuitId, year1, year2))

        res = []
        for row in cursor:
            res.append(row["year"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getDetails(circuitId, year1, year2):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select distinct ra.year, re.driverId, re.`position` 
                from circuits c, races ra, results re
                where c.circuitId = ra.circuitId 
                and ra.raceId = re.raceId
                and c.circuitId = %s
                and ra.year between %s and %s
                """

        cursor.execute(query, (circuitId, year1, year2))

        res = []
        for row in cursor:
            res.append((row["year"], Results(row["driverId"], row["position"])))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getPeso(circuitId, year1, year2):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """select count(re.driverId) as n
                from circuits c, races ra, results re
                where c.circuitId = ra.circuitId 
                and ra.raceId = re.raceId
                and c.circuitId = %s
                and re.`position` is not null
                and ra.year between %s and %s"""

        cursor.execute(query, (circuitId, year1, year2))

        res = []
        for row in cursor:
            res.append(row["n"])

        cursor.close()
        cnx.close()
        return res