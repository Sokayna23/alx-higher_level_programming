#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    str = dir(hidden_4)
    for s in str:
        if s[:2] != "__":
            print(s)
