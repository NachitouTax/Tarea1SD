import grpc
from concurrent import futures
import cache_pb2
import cache_pb2_grpc
import redis

# Configurar instancia de Redis maestro y replicas
master = redis.Redis(host='redis-master', port=6379)
replicas = [
    redis.Redis(host='redis-replica-1', port=6379),
    redis.Redis(host='redis-replica-2', port=6379),
    # Agrega más replicas según sea necesario
]

class ReplicatedCacheServicer(cache_pb2_grpc.CacheServicer):
    def Get(self, request, context):
        key = request.key
        # Leer desde una replica aleatoria
        replica = replicas[hash(key) % len(replicas)]
        value = replica.get(key)
        return cache_pb2.GetResponse(value=value.decode('utf-8') if value else '')

    def Set(self, request, context):
        key = request.key
        value = request.value
        # Escribir en el maestro
        master.set(key, value)
        return cache_pb2.SetResponse(success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cache_pb2_grpc.add_CacheServicer_to_server(ReplicatedCacheServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()