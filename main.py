import body
ball=body.ball

def create_ball(list1):
    pingpang_list=[]
    for i in range(len(list1)):
        pingpang_list.append(ball(list1[i], i))
    return pingpang_list

ball_list=[[1,-1,1],
           [-1,0,1],
           [-1,1,1],
           [-1,1,1]]
global ball_num
ball_num=len(ball_list)
pingpang_list=create_ball(ball_list)

def seek_ball(pos,available_list):
    point=[]
    for i in available_list:
        if i!=pos[0]:
            for j in range(len(pingpang_list[i].attach_pos)):
                if pingpang_list[i].attach_pos[j]*\
                        pingpang_list[pos[-2]].attach_pos[pos[-1]]<0:
                    point.append([i,j])
    return point

def draw_bauch(pos):
    pos_group=[]
    for i in range(0, len(pos), 4):
        pos_group.append(pos[i:i + 4])
        if i==0:
            C_Pnt=[20,p0*20+p_s,p1*20]
            pingpang_list[pos_group[0][0]].create(C_Pnt)
            pingpang_list[pos_group[0][0]].merged_to(pingpang_list[pos_group[0][2]], pos_group[0][3], pos_group[0][1])

        elif i>0:
            a=pos_group[-1]
            pingpang_list[a[0]].merged_to(pingpang_list[a[2]],a[3],a[1])


def arrange(level,pos=[None]):

    if level == 0 :
        global available_ball
        global p0,p1,p_s,t

        available_ball=[]
        for i in range(len(ball_list)):
            available_ball.append([i])
            for j in range(len(pingpang_list[i].attach_pos)):
                available_ball[i].append([j])
        level=level+1

        for i in range(len(ball_list)):
            for j in range(len(pingpang_list[i].attach_pos)):
                available_ball[i][j]=range(ball_num)
                available_ball[i][j].remove(i)
                available_pos=seek_ball([i,j],available_ball[i][j])
                p0=i
                p1=j
                p_s=0
                t = len(available_ball[p0][p1])
                for k in range(len(available_pos)):
                    pos=[i,j]+available_pos[k]
                    arrange(level,pos)

    elif level < ball_num and t>0 :
        t=len(available_ball[p0][p1])
        av_ball_points=[]
        for q in range(len(pingpang_list[pos[-2]].attach_pos)):
            av_ball_points.append([pos[-2],q])
            pass
        av_ball_points.remove([pos[-2],pos[-1]])
        available_ball[p0][p1].remove(pos[-2])
        t = len(available_ball[p0][p1])
        p = available_ball[p0][p1]
        for points in av_ball_points:
            available_pos=seek_ball(points,p)
            pos_baunch=[]
            if available_pos!=[]:
                for i in range(len(available_pos)):
                    pos_baunch.append(pos+points+available_pos[i])
                    # draw_bauch(pos)
                    arrange(level+1,pos_baunch[i])
    else:
        # p_s = p_s + 30
        draw_bauch(pos)
        print pos


arrange(0,)
body.start_display()#modules display

# available_list=range(ball_num)
# start_pos=[0,0]
# arr=seek_ball(start_pos,available_list)
# available_list.remove(start_pos[0])
# print(seek_ball([0,0],range(ball_num)))

# pingpang_list[0].create([10,10,0])
# pingpang_list[0].create([10,20,0])

# pingpang_list[0].merged_to(pingpang_list[1],0,0)
# pingpang_list[1].merged_to(pingpang_list[2],1,1)
# pingpang_list[2].merged_to(pingpang_list[3],2,2)
# # pingpang_list[3].merged_to(pingpang_list[4],2,1)

#
# for i in range(ball_num):
#     for j in range(pingpang_list[i].attach_num):
#         print('ball:',i,'attach point:',j,'attach states:',pingpang_list[i].attach_pos[j])
#
#
#
body.start_display()#modules display
