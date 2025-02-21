
#Question A
class ReverseIterator:
    def __init__(self,data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
lst=[1,2,3,4,5]
rev=ReverseIterator(lst)
# print(rev)
# print(iter(rev))
# print(next(rev))
for val in rev:
    print(val)

        
#Question B

def even_numbers(n):
    for i in range(n):
        if i%2==0:
            yield i 


print("Even numbers are:")
# for i in even_numbers(10):
# print(next(even_numbers(10)))
for i in even_numbers(10):
    print(i)
    
    
#Question C

def copy_file_content(source, destination):
    try:
        with open(source, 'r') as src_file:
            content = src_file.read().upper()

        with open(destination, 'w') as dest_file:
            dest_file.write(content)

        print(f"Content copied successfully from '{source}' to '{destination}' in uppercase.")
    except FileNotFoundError:
        print(f"Error: The file '{source}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



copy_file_content('source.txt', 'destination.txt')