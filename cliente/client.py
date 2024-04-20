import grpc
import cache_pb2
import cache_pb2_grpc
import redis

# Configurar la conexión a Redis
r = redis.Redis(host='redis', port=6379)

def run():
    with grpc.insecure_channel('server:50051') as channel:
        stub = cache_pb2_grpc.CacheStub(channel)

        # Simular operaciones de lectura y escritura
        key = 'clave_ejemplo'
        value = 'valor_ejemplo'

        # Intentar obtener el valor de Redis
        cached_value = r.get(key)
        if cached_value:
            print(f'Valor obtenido desde Redis: {cached_value.decode("utf-8")}')
        else:
            # Solicitar el valor al servidor gRPC
            response = stub.Get(cache_pb2.GetRequest(key=key))
            value = response.value

            # Almacenar el valor en Redis
            r.set(key, value)
            print(f'Valor obtenido desde el servidor gRPC: {value}')

if __name__ == '__main__':
    run()