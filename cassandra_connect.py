from cassandra.cluster import Cluster

if __name__ == "__main__":
    cluster = Cluster(['0.0.0.0'],port=9042)
    session = cluster.connect('cityinfo',wait_for_all_pools=True)
    session.execute('USE cityinfo')
    rows = session.execute('SELECT * FROM users')
    for row in rows:
        print(row.age,row.name,row.username)
        