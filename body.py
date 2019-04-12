from OCC.Display.SimpleGui import init_display
from OCC.BRepPrimAPI import BRepPrimAPI_MakeCylinder,BRepPrimAPI_MakeSphere
from OCC.gp import gp_Pnt,gp_Ax2,gp_Dir
import math
display, start_display, add_menu, add_function_to_menu = init_display()

def list_add(a,b):
    c = []
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c

class ball:
    def __init__(self,attach_pos,tag):
        self.default_Pnt=[0,tag*8,0]
        self.attach_pos=attach_pos
        self.divide_arg=2*math.pi/len(attach_pos)
        self.create(self.default_Pnt,0)
        self.attach_num=len(attach_pos)

    def create(self,center_Pnt,merged_arg=0):
        self.new_Pnt=center_Pnt
        self.new_gp_Pnt=gp_Pnt(center_Pnt[0],center_Pnt[1],center_Pnt[2])
        self.shape=BRepPrimAPI_MakeSphere(self.new_gp_Pnt,2.1).Shape()
        display.DisplayShape(self.shape, update=True, color='YELLOW')
        self.attach_gp_dir=[]
        self.attach_gp_Ax2=[]
        self.magnet=[]
        self.attach_dir = []

        for i in range(len(self.attach_pos)):
            if self.attach_pos[i]!=0:
                # self.attach_gp_dir.append(i)
                # self.attach_gp_Ax2.append(i)
                # self.magnet.append(i)

                self.dir=merged_arg
                merge_rotate=[math.cos(i * self.divide_arg)*math.cos(merged_arg)-
                              math.sin(i*self.divide_arg)*math.sin(merged_arg),
                              math.sin(i * self.divide_arg)*math.cos(merged_arg)+
                              math.cos(i * self.divide_arg)*math.sin(merged_arg),0]
                self.attach_dir.append([merge_rotate[0],merge_rotate[1],merge_rotate[2]])
                self.attach_gp_dir.append(gp_Dir(self.attach_dir[i][0],self.attach_dir[i][1],self.attach_dir[i][2]))
                self.attach_gp_Ax2.append(gp_Ax2(self.new_gp_Pnt,self.attach_gp_dir[i]))
                self.magnet.append(BRepPrimAPI_MakeCylinder(self.attach_gp_Ax2[i],0.25,2.4).Shape())
                if self.attach_pos[i]==1:
                    display.DisplayShape(self.magnet[i], update=True, color='RED')
                elif self.attach_pos[i]==-1:
                    display.DisplayShape(self.magnet[i], update=True, color=22)#22 is blue
            else:
                self.attach_gp_dir.append(i)
                self.attach_gp_Ax2.append(i)
                self.attach_dir.append(i)
                self.magnet.append(i)

    def merged_to(self,target_ball,target_point,self_point):

        merge_vector=list(map(lambda i:i*4.8,self.attach_dir[self_point]))
        target_center=list_add(merge_vector,self.new_Pnt)
        # target_center_gp=gp_Pnt(target_center[0],target_center[1],target_center[2])
        # merged_vector=[-merge_vector[0],-merge_vector[1],-merge_vector[2]]
        merged_arg=math.pi+self.dir+(self_point-target_point)*self.divide_arg
        # merged_dir=[-self.attach_dir[self_point][0],-self.attach_dir[self_point][1],-self.attach_dir[self_point][2]]
        target_ball.create(target_center,merged_arg)

# ball1=ball([1,0,1,0],0)
# ball2=ball([0,-1,1,0],1)
# ball1.create(gp_Pnt(10,2,9),1)
# my_cylinder = BRepPrimAPI_MakeCylinder(5, 20).Shape()
# my_ball=BRepPrimAPI_MakeSphere(ball_center, 2.1).Shape()
# start_display()
