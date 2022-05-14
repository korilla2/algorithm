from __future__ import annotations
from typing import Any, Type
import hashlib


class Node:

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next


class ChainedHash:

    def __init__(self, capacity: int) -> None:
        # 해시 테이블 크기 지정
        self.capacity = capacity
        # 해시 테이블 선언 -> list
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        # key -> int
        if isinstance(key, int):
            return key % self.capacity

        # key -> not int
        return (int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                # 검색 성공
                return p.value
            # 뒤쪽 노드
            p = p.next
        # 검색 실패
        return None

    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                # 추가 실패
                return False
            # 뒤쪽 노드
            p = p.next

        temp = Node(key, value, self.table[hash])
        # 노드 추가
        self.table[hash] = temp
        # 추가 성공
        return True

    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        # 이전 노드
        pp = None

        while p is not None:
            if p.key == key:
                # 처음 찾은 경우
                if pp is None:
                    # 바로 적용
                    self.table[hash] = p.next
                # 처음이 아닌 경우
                else:
                    # 연결 바꿔줌
                    pp.next = p.next
                return True
            pp = p
            p = p.next

        # 삭제 실패
        return False

    # 출력
    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(p.key, p.value, end='')
                p = p.next
            print()
