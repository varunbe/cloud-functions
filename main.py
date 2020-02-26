from google.cloud import spanner

instance_id = 'test-instance'
database_id = 'trip-eta'

client = spanner.Client()
instance = client.instance(instance_id)
database = instance.database(database_id)


def spanner_read_data(request):
    query = 'SELECT TRP_ETA_SEQ, EVNT_GMT_TM, LAT_EVNT, LON_EVNT, OD_CTY, OD_ST, TOT_RMN_MIN, TOT_RMN_MLS FROM TRIP_DETAILS'

    outputs = []
    with database.snapshot() as snapshot:
        results = snapshot.execute_sql(query)

        for row in results:
            output = 'Trip ETA Sequence: {}, GPS Event time: {}, Latitude: {}, Longitude: {}, Current City: {}, Current State: {}, Total Remaining Time to reach the destination: {}, Total Remaining Miles to reach the destination: {}'.format(*row)
            outputs.append(output)

    return '\n'.join(outputs)
