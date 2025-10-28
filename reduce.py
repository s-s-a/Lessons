def fox_reduce(string: str) -> str:
    return ' '.join(string.split())

if __name__ == '__main__':
    print(fox_reduce('   Hello,    World!   '))