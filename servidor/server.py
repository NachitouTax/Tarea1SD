import grpc
from concurrent import futures
import cache_pb2
import cache_pb2_grpc
import redis
import psycopg2

# Configurar la conexión a Redis
r = redis.Redis(host='redis', port=6379)

# Configurar la conexión a PostgreSQL
conn = psycopg2.connect(
    host="postgres",
    database="mydatabase",
    user="myuser",
    password="mypassword"
)
cursor = conn.cursor()

class CacheServicer(cache_pb2_grpc.CacheServicer):
    def Get(self, request, context):
        key = request.key

        # Intentar obtener el valor de Redis
        value = r.get(key)
        if value:
            return cache_pb2.GetResponse(value=value.decode('utf-8'))

        # Si el valor no está en Redis, obtenerlo de PostgreSQL
        cursor.execute("SELECT value FROM mytable WHERE key = %s", (key,))
        result = cursor.fetchone()
        if result:
            value = result[0]
            # Almacenar el valor en Redis
            r.set(key, value)
            return cache_pb2.GetResponse(value=value)
        else:
            return cache_pb2.GetResponse(value='')

    def Set(self, request, context):
        key = request.key
        value = request.value

        # Almacenar el valor en Redis y PostgreSQL
        r.set(key, value)
        cursor.execute("INSERT INTO mytable (key, value) VALUES (%s, %s)", (key, value))
        conn.commit()

        return cache_pb2.SetResponse(success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cache_pb2_grpc.add_CacheServicer_to_server(CacheServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()