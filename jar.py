
class Jar:
    def __init__(self):
        capacity_str = input("Enter capacity: ")
        self._capacity = int(capacity_str) if capacity_str.isdigit() else 12
        if self._capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Deposit amount must be a non-negative integer.")
        if self._size + n > self._capacity:
            raise ValueError("Not enough space in the jar.")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Withdrawal amount must be a non-negative integer.")
        if self._size < n:
            raise ValueError("Not enough cookies in the jar.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
