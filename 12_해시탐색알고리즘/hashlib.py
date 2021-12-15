"""
hashlib: 파이썬에서는 hash 구현시 hashlib 모듈 사용 가능
"""
import hashlib
# result = hashlib.blake2b("kim".encode('utf-8'),digest_size=64)

result = hashlib.sha384("kim".encode('utf-8'))
print(result.digest())  # bytes 문자열 반환
print(result.hexdigest())  # 바이트 문자열을 16진수로 변환 반환