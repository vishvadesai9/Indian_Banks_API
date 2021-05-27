""" A script to query the database.

This script queries the database to fetch data for autocomplete api and search api. It fetches database 
credentials using credentials module and establishes the connection to the database. Moreover, it queries 
the database for required data then returns appropriate response in the form of dictionary and then closes
the connection to the database.
"""
import json

import psycopg2
from psycopg2.extras import RealDictCursor


from credentials import credentials

def autocomplete(q,limit,offset):
    """Fetches branches which match the query.

    Retrieves possible matches based on the branch name ordered by
    IFSC code (ascending order) with limit and offset.

    Args:
        q: The branch to be retrieved.
        limit: The limit of query results.
        offset: The offset of query results.

    Returns: A list of dictionaries of branch data. 
        For Example: 
            {
            "branches": [{
                    "ifsc": "ABHY0065001",
                    "bank_id": 60,
                    "branch": "RTGS-HO",
                    "address": "ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
                    "city": "MUMBAI",
                    "district": "GREATER MUMBAI",
                    "state": "MAHARASHTRA"
                }, {
                    "ifsc": "ABNA0000001",
                    "bank_id": 110,
                    "branch": "RTGS-HO",
                    "address": "414 EMPIRE COMPLEX, SENAPATI BAPAT MARG LOWER PAREL WEST MUMBAI 400013",
                    "city": "MUMBAI",
                    "district": "GREATER BOMBAY",
                    "state": "MAHARASHTRA"
                }]
            }
    """
    conn = None
    try:
        # read the connection parameters
        params = credentials()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=RealDictCursor)
       
        query_sql = "SELECT * FROM branches WHERE branch LIKE '"+q+"%' ORDER BY ifsc ASC LIMIT " + str(limit) +" OFFSET " + str(offset)+" ;"  

        cur.execute(query_sql)
        results = cur.fetchall()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()

        if results:
            results = [dict(row) for row in results]
            response = {"branches": results}
            return response
        else:
            return {"response":"NO RESULTS FOUND"}

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return {"message":"Internal Server Error"}
        # return {"error": json.dumps(error)}
    finally:
        if conn is not None:
            conn.close()


def search(q,limit,offset):
    """Fetches branches which match the query.

    Retrieves possible matches across all columns and all rows, ordered by
    IFSC code (ascending order) with limit and offset. The term to be searched 
    and the columns have been converted to uppercase for the search to be case insensitive.

    Args:
        q: The term or word to be searched.
        limit: The limit of query results.
        offset: The offset of query results.

    Returns: A list of dictionaries of branch data. 
        For Example: 
            {
            "branches": [{
                    "ifsc": "ABNA0100318",
                    "bank_id": 110,
                    "branch": "BANGALORE",
                    "address": "PRESTIGE TOWERS', GROUND FLOOR, 99 & 100, RESIDENCY ROAD, BANGALORE 560
                    025.",
                    "city": "BANGALORE",
                    "district": "BANGALORE URBAN",
                    "state": "KARNATAKA"
                }, {
                    "ifsc": "ADCB0000002",
                    "bank_id": 143,
                    "branch": "BANGALORE",
                    "address": "CITI CENTRE, 28, CHURCH STREET, OFF M. G. ROAD BANGALORE 560001",
                    "city": "BANGALORE",
                    "district": "BANGALORE URBAN",
                    "state": "KARNATAKA"
                }]
            }

    """
    conn = None
    try:
        # read the connection parameters
        params = credentials()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        q = q.upper()

        query_sql =  "SELECT * FROM branches WHERE (UPPER(ifsc) LIKE '%"+q+"%') or \
                        (UPPER(branch) LIKE '%"+q+"%') or (UPPER(address) LIKE '%"+q+"%') or (UPPER(city) LIKE '%"+q+"%') or \
                        (UPPER(district) LIKE '%"+q+"%') or (UPPER(state) LIKE '%"+q+"%') ORDER BY ifsc ASC LIMIT "+ str(limit) + " OFFSET " \
                        + str(offset) + ";"

        cur.execute(query_sql)
        results = cur.fetchall()

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()

        if results:
            results = [dict(row) for row in results]
            response = {"branches": json.dumps(results)}
            return response
        else:
            return {"response":"NO RESULTS FOUND"}

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return {"message":"Internal Server Error"}
        # return {"error": str(error)}
    finally:
        if conn is not None:
            conn.close()

# if __name__ == '__main__':
#     search('RTGS',3,0)