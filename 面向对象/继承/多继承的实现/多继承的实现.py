from child import Child

def main():
    c = Child(3000,100)
    print(c.money,c.faceValue)
    c.play()
    c.eat()
    c.func()
    # 注意：父类中方法名相同，默认调用的是在括号内排前面的父类方法
if __name__ == '__main__':
    main()
