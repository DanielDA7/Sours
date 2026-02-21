# ============================================================================
# ОЧЕНЬ СЛОЖНЫЙ КОД НА PYTHON - Продвинутые концепции
# ============================================================================

from typing import TypeVar, Generic, Callable, Any, List, Dict, Tuple, Generator
from functools import wraps, lru_cache
from abc import ABC, abstractmethod
from collections import defaultdict, deque
from dataclasses import dataclass, field
import heapq
import threading
from queue import Queue
from enum import Enum
import json

# ============================================================================
# 1. МЕТАПРОГРАММИРОВАНИЕ И ДЕКОРАТОРЫ
# ============================================================================

class Singleton(type):
    """Метакласс для создания синглтона"""
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DatabaseConnection(metaclass=Singleton):
    """Синглтон класс для работы с БД"""
    def __init__(self):
        self.connection_id = id(self)
        print(f"БД соединение создано: {self.connection_id}")


def memoize_with_ttl(timeout: int):
    """Декоратор с кэшированием и временем жизни"""
    def decorator(func: Callable) -> Callable:
        cache = {}
        timestamps = {}
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            import time
            key = (args, tuple(sorted(kwargs.items())))
            current_time = time.time()
            
            if key in cache and (current_time - timestamps[key] < timeout):
                return cache[key]
            
            result = func(*args, **kwargs)
            cache[key] = result
            timestamps[key] = current_time
            return result
        
        return wrapper
    return decorator


@memoize_with_ttl(timeout=10)
def expensive_computation(n: int) -> int:
    """Дорогостоящее вычисление с кэшем"""
    print(f"Вычисляю для {n}...")
    return sum(i ** 2 for i in range(n))


# ============================================================================
# 2. ГЕНЕРИКИ И ТИПИЗАЦИЯ
# ============================================================================

T = TypeVar('T')

class Stack(Generic[T]):
    """Обобщенный стек с типизацией"""
    def __init__(self):
        self._items: List[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T:
        return self._items.pop()
    
    def is_empty(self) -> bool:
        return len(self._items) == 0


# ============================================================================
# 3. СЛОЖНЫЕ АЛГОРИТМЫ - ДИНАМИЧЕСКОЕ ПРОГРАММИРОВАНИЕ
# ============================================================================

class DynamicProgramming:
    """Примеры сложных алгоритмов ДП"""
    
    @staticmethod
    def longest_common_subsequence(s1: str, s2: str) -> str:
        """Самая длинная общая подпоследовательность (O(n*m))"""
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Восстановление результата
        result = []
        i, j = m, n
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                result.append(s1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        
        return ''.join(reversed(result))
    
    @staticmethod
    def min_edit_distance(word1: str, word2: str) -> int:
        """Расстояние редактирования (Левенштейн)"""
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        
        return dp[m][n]


# ============================================================================
# 4. ГРАФОВЫЕ АЛГОРИТМЫ
# ============================================================================

class Graph:
    """Сложный граф с различными алгоритмами"""
    
    def __init__(self, vertices: int):
        self.V = vertices
        self.graph = defaultdict(list)
        self.visited = set()
    
    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        self.graph[u].append((v, weight))
    
    def dijkstra(self, start: int) -> Dict[int, float]:
        """Алгоритм Дейкстры для кратчайшего пути"""
        distances = {i: float('inf') for i in range(self.V)}
        distances[start] = 0
        pq = [(0, start)]
        
        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current_dist > distances[current]:
                continue
            
            for neighbor, weight in self.graph[current]:
                distance = current_dist + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances
    
    def dfs(self, vertex: int, visited: set = None) -> List[int]:
        """DFS с посещением вершин"""
        if visited is None:
            visited = set()
        
        visited.add(vertex)
        result = [vertex]
        
        for neighbor, _ in self.graph[vertex]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        
        return result


# ============================================================================
# 5. ГЕНЕРАТОРЫ И ИТЕРАТОРЫ
# ============================================================================

class FibonacciGenerator:
    """Генератор чисел Фибоначчи с состоянием"""
    
    def __init__(self, limit: int):
        self.limit = limit
        self.a, self.b = 0, 1
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self) -> int:
        if self.count >= self.limit:
            raise StopIteration
        
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value


def infinite_sequence() -> Generator[int, None, None]:
    """Бесконечный генератор"""
    num = 0
    while True:
        yield num
        num += 1


# ============================================================================
# 6. МНОГОПОТОЧНОСТЬ И СИНХРОНИЗАЦИЯ
# ============================================================================

class ThreadSafeQueue:
    """Потокобезопасная очередь"""
    
    def __init__(self, maxsize: int = 0):
        self.queue = Queue(maxsize=maxsize)
        self.lock = threading.Lock()
    
    def put(self, item: Any) -> None:
        with self.lock:
            self.queue.put(item)
    
    def get(self) -> Any:
        with self.lock:
            return self.queue.get()


# ============================================================================
# 7. АБСТРАКТНЫЕ КЛАССЫ И ИНТЕРФЕЙСЫ
# ============================================================================

class DataProcessor(ABC):
    """Абстрактный обработчик данных"""
    
    @abstractmethod
    def process(self, data: Any) -> Any:
        pass
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass


class JSONProcessor(DataProcessor):
    """Конкретная реализация для JSON"""
    
    def process(self, data: str) -> Dict:
        if self.validate(data):
            return json.loads(data)
        raise ValueError("Невалидный JSON")
    
    def validate(self, data: str) -> bool:
        try:
            json.loads(data)
            return True
        except:
            return False


# ============================================================================
# 8. КОНТЕКСТНЫЕ МЕНЕДЖЕРЫ
# ============================================================================

class FileLogger:
    """Контекстный менеджер для логирования"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, 'a')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        return False


# ============================================================================
# 9. СЛОЖНЫЕ РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ И ПАРСИНГ
# ============================================================================

import re

def parse_url(url: str) -> Dict[str, str]:
    """Парсинг URL с регулярными выражениями"""
    pattern = r'(?P<protocol>\w+)://(?P<host>[^:/]+):?(?P<port>\d+)?(?P<path>/[^?]*)?(?:\?(?P<query>.*))?'
    match = re.match(pattern, url)
    
    if match:
        return match.groupdict()
    return {}


# ============================================================================
# 10. ФУНКЦИОНАЛЬНОЕ ПРОГРАММИРОВАНИЕ
# ============================================================================

from functools import reduce

def functional_pipeline(*functions: Callable) -> Callable:
    """Композиция функций"""
    def pipeline(arg):
        return reduce(lambda x, f: f(x), functions, arg)
    return pipeline


square = lambda x: x ** 2
times_two = lambda x: x * 2
plus_one = lambda x: x + 1

complex_function = functional_pipeline(square, times_two, plus_one)


# ============================================================================
# 11. АСИНХРОННОЕ ПРОГРАММИРОВАНИЕ (Пример структуры)
# ============================================================================

import asyncio

async def async_fetch(delay: int) -> str:
    """Асинхронная операция"""
    await asyncio.sleep(delay)
    return f"Результат после {delay} секунд"


async def async_main():
    """Асинхронная главная функция"""
    tasks = [async_fetch(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    return results


# ============================================================================
# 12. ДЕКОРАТОР КЛАССОВ
# ============================================================================

def add_repr(cls):
    """Декоратор для автоматического __repr__"""
    def __repr__(self):
        attrs = ', '.join(f'{k}={v!r}' for k, v in self.__dict__.items())
        return f'{cls.__name__}({attrs})'
    
    cls.__repr__ = __repr__
    return cls


@add_repr
@dataclass
class Person:
    name: str
    age: int
    skills: List[str] = field(default_factory=list)


# ============================================================================
# ТЕСТИРОВАНИЕ
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("СЛОЖНЫЙ КОД НА PYTHON - ПРИМЕРЫ")
    print("=" * 70)
    
    # 1. Синглтон
    print("\n1. СИНГЛТОН:")
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"Один и тот же объект? {db1 is db2}")
    
    # 2. Мемоизация
    print("\n2. МЕМОИЗАЦИЯ:")
    print(f"Результат: {expensive_computation(1000)}")
    print(f"Из кэша: {expensive_computation(1000)}")
    
    # 3. ДП - LCS
    print("\n3. ДИНАМИЧЕСКОЕ ПРОГРАММИРОВАНИЕ:")
    result = DynamicProgramming.longest_common_subsequence("ABCDGH", "AEDFHR")
    print(f"Самая длинная общая подпоследовательность: {result}")
    
    # 4. Расстояние редактирования
    distance = DynamicProgramming.min_edit_distance("horse", "ros")
    print(f"Расстояние редактирования: {distance}")
    
    # 5. Граф и Дейкстра
    print("\n4. ГРАФ И ДЕЙКСТРА:")
    g = Graph(6)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 2)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 3, 8)
    g.add_edge(2, 4, 10)
    g.add_edge(3, 4, 2)
    distances = g.dijkstra(0)
    print(f"Кратчайшие расстояния от вершины 0: {distances}")
    
    # 6. Генератор Фибоначчи
    print("\n5. ГЕНЕРАТОР:")
    fib = FibonacciGenerator(10)
    print(f"Первые 10 чисел Фибоначчи: {list(fib)}")
    
    # 7. Парсинг URL
    print("\n6. ПАРСИНГ URL:")
    url_result = parse_url("https://example.com:8080/path?query=value")
    print(f"Распарсенный URL: {url_result}")
    
    # 8. Функциональное программирование
    print("\n7. КОМПОЗИЦИЯ ФУНКЦИЙ:")
    print(f"f(2) = ((2^2) * 2) + 1 = {complex_function(2)}")
    
    # 9. Person класс
    print("\n8. DATACLASS И ДЕКОРАТОР:")
    person = Person("Алиса", 30, ["Python", "Java"])
    print(person)
    
    # 10. LRU Cache
    print("\n9. LRU CACHE:")
    @lru_cache(maxsize=128)
    def fibonacci(n: int) -> int:
        if n < 2:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    print(f"Fibonacci(30) = {fibonacci(30)}")
    
    print("\n" + "=" * 70)
    print("КОД СОДЕРЖИТ ОЧЕНЬ СЛОЖНЫЕ КОНЦЕПЦИИ!")
    print("=" * 70)
