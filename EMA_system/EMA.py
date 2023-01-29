import execjs
import math
import time
from explanatoryTool import*
from manim import*


def js_from_file(file_name):
    with open(file_name, 'r', encoding='UTF-8') as file:
        result = file.read()
    return result

class EMA(explanatoryTools):
    def construct(self):
        input = '( 23 + 35 ) * 2 - 11'
        mathsteps = execjs.compile(js_from_file('./mathsteps.js'))
        StepsText = mathsteps.call('steps', input)
        
        size = list(range(math.ceil(len(StepsText)**0.5)))
        locate = []
        unit_height = (config.frame_height-1.5)/len(size)
        unit_width = config.frame_width/len(size)
        for i in size:
            for j in size:
                locate.append([0.5+unit_width*i, 1.5+unit_height*j])
        length = unit_width-1
        question = input.replace('*','×').replace('-','−')+' = ?'
        
        self.ask(question, position=[4, 0, 0], font_size=36, bold=True)
        
        for i in range(len(StepsText)):
            command = StepsText[i][0]
            nums = StepsText[i][1]

            if command == 'add':
                self.numberLineAdd(nums[0], nums[1], position=[locate[i][0], locate[i][1], 0.0], length=length)
            elif command == 'sub':
                self.numberLineSub(nums[0], nums[1], position=[locate[i][0], locate[i][1], 0.0], length=length)
            elif command == 'mul':
                self.numberLineMul(nums[0], nums[1], position=[locate[i][0], locate[i][1], 0.0], length=length)
            elif command == 'ans':
                self.ans(nums[0], position=[locate[i][0], locate[i][1], 0.0])

class Add(explanatoryTools):
    def construct(self):
        self.numberLineAdd(199, 31, position=[(config.frame_width-10)/2, (config.frame_height-2)/2, 0.0], length=10)
        self.pause()

class Sub(explanatoryTools):
    def construct(self):
        self.numberLineSub(102, 77, position=[(config.frame_width-10)/2, (config.frame_height-2)/2, 0.0], length=10)
        self.pause()

class Mul(explanatoryTools):
    def construct(self):
        self.numberLineMul(58, 2, position=[(config.frame_width-10)/2, (config.frame_height-2)/2, 0.0], length=10)
        self.pause()





if __name__ == '__main__':
        timerecord=[0,0,0]
        for k in range(10):
            i=0
            with tempconfig({'quality':'medium_quality', 'disable_caching':True, "preview":True}):
                scene = []
                scene.append(Add())
                scene.append(Sub())
                for j in scene:
                    start=time.time()       
                    j.render()
                    timerecord[i]=timerecord[i]+time.time()-start
                    i+=1
        for i in range(3):
            print(timerecord[i]/10)