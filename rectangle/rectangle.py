class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # Return an iterator for the Rectangle
        yield {'length': self.length}
        yield {'width': self.width}

# Example usage:
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    
    for dimension in rect:
        print(dimension)
