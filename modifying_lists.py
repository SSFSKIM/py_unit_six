#Steve
#11.13

def create_list(a, b):
    list = []
    for i in range(b-a+1):
        list.append(i+a)
    return list
def main():
    a = int(input())
    b = int(input())
    print(create_list(a, b))

main()