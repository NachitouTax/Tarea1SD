import grpc
import cache_pb2
import cache_pb2_grpc

def run():
    with grpc.insecure_channel('server:50051') as channel:
        stub = cache_pb2_grpc.CacheStub(channel)

        # Establecer un valor en la caché
        response = stub.Set(cache_pb2.SetRequest(key='key1', value='value1'))
        print(f'Set response: {response.success}')

        # Obtener un valor de la caché
        response = stub.Get(cache_pb2.GetRequest(key='key1'))
        print(f'Get response: {response.value}')

if __name__ == '__main__':
    run()
    