# Assignment #1
# string = "eeeeE llllLl lllzzZzzzz eroe operationr pollo "
# regex = \w\s|o$ or \w\s
# link: https://pythex.org/?regex=%5Cw%5Cs%7Co%24&test_string=eeeeE%20llllLl%20lllzzZzzzz%20eroe%20operationr%20pollo%20&ignorecase=0&multiline=0&dotall=0&verbose=0
# ----
# Assignment #2
# string = "EElzero11 LElzero111 ZElzero1111 EElzero11111 RElzero111111 OElzero1111111"
# regex = LElzero
# link: https://pythex.org/?regex=LElzero&test_string=EElzero11%20LElzero111%20ZElzero1111%20EElzero11111%20RElzero111111%20OElzero1111111&ignorecase=0&multiline=0&dotall=0&verbose=0
# ----
# Assignment #3
# string = ("+(0100) 600-1234\n+(0100) 60-1234\n(0100) 6000-1234\n01006001234\n0100 600 1234\n(0100) 600-1\n(0100) 600-12")
# regex = \+?\(\d{4}\)\s\d+-\d{4}
# link: https://pythex.org/?regex=%5C%2B%3F%5C(%5Cd%7B4%7D%5C)%5Cs%5Cd%2B-%5Cd%7B4%7D&test_string=%2B(0100)%20600-1234%0A%2B(0100)%2060-1234%0A(0100)%206000-1234%0A01006001234%0A0100%20600%201234%0A(0100)%20600-1%0A(0100)%20600-12&ignorecase=0&multiline=0&dotall=0&verbose=0
# ----
# Assignment #4
# string = "http://www.elzero.org:8888/link.php\nhttps://elzero.org:8888/link.php\nhttp://www.elzero.com/link.py\nhttps://elzero.com/link.py\nhttp://www.elzero.net\nhttps://elzero.net"
# regex = https?://(www\.)?\w+\.(org|com)(:\d+)?/\w+.+
# link: https://pythex.org/?regex=https%3F%3A%2F%2F(www%5C.)%3F%5Cw%2B%5C.(org%7Ccom)(%3A%5Cd%2B)%3F%2F%5Cw%2B.%2B&test_string=http%3A%2F%2Fwww.elzero.org%3A8888%2Flink.php%0Ahttps%3A%2F%2Felzero.org%3A8888%2Flink.php%0Ahttp%3A%2F%2Fwww.elzero.com%2Flink.py%0Ahttps%3A%2F%2Felzero.com%2Flink.py%0Ahttp%3A%2F%2Fwww.elzero.net%0Ahttps%3A%2F%2Felzero.net%0A(0100)%20600-12&ignorecase=0&multiline=0&dotall=0&verbose=0
# ----
# Assignment #5
# string = "http\nhttps\nabcd\nabcd"
# regex = https? or [^abcd]+ or ^h\w+ with multiline or ^[^a]+ with multiline or \w+ps?$
# ----
