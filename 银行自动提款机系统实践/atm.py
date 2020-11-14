
from card import Card
from user import User
import random
class ATM(object):
    def __init__(self):
        self.allUsers = {}
    #开户
    def creatUser(self):
        # 用用户中添加一对键值对(卡号--用户)
        name = input("请输入您的姓名：")
        idCard = input("请输入您的身份证号码：")
        phoneNum = input("请输入您的电话号码：")
        prestoreMoney = int(input("请输入您的预存款金额："))
        if prestoreMoney < 0:
            print("您输入的金额有误，开户失败")
            return -1
        cardPasswd = input("请输入您设置的密码：")
        if not self.checkPasswd(cardPasswd):
            print("密码输入错误，开户失败……")
            return -1
        cardId = self.randomCardId()
        print(cardId)
        card = Card(cardId,cardPasswd,prestoreMoney)
        user = User(name, idCard, phoneNum, card)
        self.allUsers[cardId] = user
        print("开户成功！请牢记卡号:%s"%cardId)
    def searchUserInfo(self):
        cardId = input("请输入您的卡号：")
            # 判断卡号存在
        user = self.allUsers.get(cardId)
        if not user:
             print("该卡号不存在!查询失败……")
             return -1
        # 判断是否被锁定
        if user.card.cardLock:
            print("该卡号被锁定!请解锁后再进行其他操作……")
        # 验证密码
        if not self.checkPasswd(user.card.cardPasswd):
            user.card.cardLock = True
            print("密码错误！该卡号被锁定!请解锁后再进行其他操作……")
            return -1
        print("账号：%s  余额：%d"%(user.card.cardId,user.card.cardMoney))



    def getMoney(self):
        pass
    def saveMoney(self):
        pass
    def transferMoney(self):
        pass
    def changePasswd(self):
        pass
    def lockUser(self):
        cardId = input("请输入您的卡号：")
        user = self.allUsers.get(cardId)
        if not user:
            print("该卡号不存在!锁定失败……")
            return -1
        if user.card.cardLock:
            print("该卡已经被锁定！")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码错误！锁定失败……")
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！锁定失败……")
            return -1
        # 锁她
        user.card.cardLock = True
        print("锁定成功！")




    def unlockUser(self):
        cardId = input("请输入您的卡号：")
        user = self.allUsers.get(cardId)
        if not user:
            print("该卡号不存在！解锁失败……")
            return -1
        if not user.card.cardLock:
            print("该卡未被锁定！")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("密码错误！解锁失败……")
            return -1
        tempIdCard = input("请输入您的身份证号码：")
        if tempIdCard != user.idCard:
            print("身份证输入错误！解锁失败……")
            return -1
        # 开锁
        user.card.cardLock = False
        print("解锁成功！")

    def newCard(self):
        pass
    def killUser(self):
        pass

    # 验证密码
    def checkPasswd(self,realPasswd):
        for i in range(3):
            tempPasswd = input("请输入密码:")
            if tempPasswd ==realPasswd:
                return True
        return False
    # 生成卡号
    def randomCardId(self):
        while True:
            str = ""
            for i in range(6):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch
            # 判断不重复
            if not self.allUsers.get(str):
                return str



