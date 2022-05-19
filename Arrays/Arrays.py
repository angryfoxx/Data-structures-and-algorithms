import ctypes
class Dynamic_Array:
    def __init__(self):
        self.n = 0
        self.cap = 1
        self.a = self.make_arr(self.cap)

    def __len__(self):
        return self.n

    def __getitem__(self, item):
        if not 0 <= item < self.n:
            raise IndexError("İndex dışı !")

        return self.a[item]

    def append(self, val):
        if self.n == self.cap:
            self.resize(2 * self.cap)

        self.a[self.n] = val
        self.n += 1

    def resize(self, new_cap):
        B = self.make_arr(new_cap)

        for i in range(self.n):
            B[i] = self.a[i]

        self.a = B
        self.cap = new_cap

    def make_arr(self, new_cap):
        return (new_cap * ctypes.py_object)()



arr = Dynamic_Array()

arr.append(1)
print(arr[0])

arr.append(3)
print(arr[0],arr[1])

arr.append(5)
print(arr[0],arr[1],arr[2])