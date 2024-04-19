import grpc
from concurrent import futures
import cache_pb2
import cache_pb2_grpc
import redis

# Configuración de Redis
r = redis.Redis(host='redis', port=6379)

class CacheServicer(cache_pb2_grpc.CacheServicer):
    def Get(self, request, context):
        value = r.get(request.key)
        return cache_pb2.GetResponse(value=value.decode('utf-8') if value else '')

    def Set(self, request, context):
        r.set(request.key, request.value)
        return cache_pb2.SetResponse(success=True)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    cache_pb2_grpc.add_CacheServicer_to_server(CacheServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()