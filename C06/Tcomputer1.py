class TComputer:
    def __init__(self):
        self.possible_list=[]
        for i in range(1,10):
           for j in range(1,10):
               for x in range(1,10):
                   for y in range(1,10):
                       if i!=j and i!=x and i!=y and j!=x and j!=y and x!=y:
                           self.possible_list.append(i*1000+j*100+x*10+y)
    
    def __getinsible(self,all_possible,mac_num,shot_num):
        mac_str=str(mac_num)
        re_list=[]
        for every_num in all_possible:
           bingo_num=0
           for iter in range(4):
               if str(every_num)[iter]==mac_str[iter]:
                   bingo_num+=1
           if bingo_num==shot_num:
               re_list.append(every_num)
        return re_list
    
    def __getpossible(self,all_possible,mac_num,shot_num):
        list1=list(str(mac_num))
        re_list=[]
        for every_num in all_possible:
            bingo_num=0
            for every_char in list(str(every_num)):
                if every_char in list1:
                    bingo_num+=1
        if bingo_num==shot_num:
            re_list.append(every_num)
        return re_list
    
    def getuserinput(self,has_info,pos_info):
        self.has_info=has_info
        self.pos_info=pos_info
    
    def printnum(self):
        if self.has_info=='ok':
            self.cur_num=self.possible_list[618]
            return self.cur_num
        else:
            self.possible_list=self.__getpossible(self.possible_list,self.cur_num,self.has_info)
            self.possible_list=self.__getinsible(self.possible_list,self.cur_num,self.pos_info)
            if len(self.possible_list)==0:
              raise UserDataError()
            self.cur_num= self.possible_list[0]
            return self.possible_list[0]        
class BusiError(Exception):
    """程序异常错误信息总类"""
    pass
class UserInputError(BusiError):
     """用户格式错误：err_input记录错误信息，out_info记录提示信息"""
     def __init__(self, err_input, out_info):
         self.err_input= err_input
         self.out_info=out_info
class UserDataError(BusiError):
     """程序异常错误信息总类"""
     pass




if __name__=='__main__':
   computer=TComputer()
   print("计算机:准备猜数？")
   while 1:
     try:  
        value=input("人:")
        if value !='ok' and value !='yes' and (not value[0].isdigit() and  
            isdigit[1]!=',' and (not isdigit[2].isdigit()) ):
            raise UserInputError(value,"输入信息应该为ok、yes和两个数字中间带一个逗号")
        if value=="ok":
            computer.getuserinput(value,'')
            print("计算机:"+str(computer.printnum()))
        elif value=="yes":
            print("计算机:bingo")
            break
        else:
            computer.getuserinput(int(value.split(",")[0]),int(value.split(",")[1]))
            print("计算机:"+str(computer.printnum()))
     except UserInputError as InputError:
        print("你输入的："+InputError.err_input+"不正确")
        print("你应该输入："+InputError.out_info)
     except UserDataError:
        print("你输入的提示信息是错误的！请重新开始游戏")
        computer=TComputer()

