class Stack:
    def __init__(self, size=5):
        self.stack = []
        self.size = size
        self.top = 0

    def push(self, data):
        if data in self.stack:
            print("{} 값은 중복된 데이터입니다.".format(data))
        else:
            if self.size > self.top:
                self.stack.append(data)
                self.top += 1
                print("{} 값을 스택에 추가합니다.".format(data))
            else:
                print("overflow")
        self.view()

    def pop(self):
        if self.top <= 0:
            print("underflow 발생...스택에 값이 존재하지 않습니다.")
        else:
            print("{} 값을 pop() 했습니다.".format(self.stack[-1]))
            del self.stack[-1]
            self.top -= 1
        self.view()
    def view(self):
        print("스택에 저장된 데이터", end = "")
        if self.top <= 0:
            print("가 없습니다.")
        else:
            print("", end = " : ")
            for elem in self.stack:
                print(elem, end = " ")
            print()

st = Stack()
st.view()
st.pop()
st.push(1)
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.push(6)
print('=' * 80)
st.view()
print('=' * 80)
st.pop()
st.pop()
st.pop()
st.pop()
st.pop()
st.pop()