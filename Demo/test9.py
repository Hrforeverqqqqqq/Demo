#列表切片，左闭右开
l=[1,2,3,4,5,6]
# print(l[::-1])

l.append(7)#末尾添加一个数据
l.extend([8,9])#末尾添加多个数据
l.insert(3,9)#在特定位置插入数据


# print(l)

L1 = [1, 2, 3]
# a, b, c = L1
# print(a, b, c)
#
# print(dir(list))
# print(dir(set))

A = [1, 3, 5, 7, 9, 11, 13, 15, 17]
b = [1, 2, 3, 5, 8, 13, 21]
# print([i for i in A if i in b])


# 千万级数组 A = [1, 3, 5, 7, 9, 11, 13, 15, 17, ...]
# 万级数据 b = [1, 2, 3, 5, 8, 13, 21, ....]
# A 和 b 都是元素唯一上升序列
# x = [1, 3, 5, 13, 21, ...]

# a = set(A)
# #
# # if len(list(a))==len(A):
# #     print('true')




# def maxarry(num):
#     if len(num)==0:
#         return 0
#     dp = [0 for _ in range(len(num))]
#     print(dp)
#     dp[0]=num[0]
#     for i in range(1,len(num)):
#         if dp[i-1]>=0:
#             dp[i]=dp[i-1]+num[i]
#         else:
#             dp[i]=num[i]
#     return max(dp)
#
#
# a =maxarry([-2,1,-3,4,-1,2,1,-5,4])
# print(a)


# from tensorboardX import SummaryWriter
#
# # Creates writer1 object.
# # The log will be saved in 'runs/exp'
# writer1 = SummaryWriter('./Demo/runs/exp')
#
# # Creates writer2 object with auto generated file name
# # The log directory will be something like 'runs/Aug20-17-20-33'
# writer2 = SummaryWriter()
#
# # Creates writer3 object with auto generated file name, the comment will be appended to the filename.
# # The log directory will be something like 'runs/Aug20-17-20-33-resnet'
# writer3 = SummaryWriter(comment='resnet')



# from tensorboardX import SummaryWriter
# writer = SummaryWriter('runs/scalar_example')
# for i in range(10):
#     writer.add_scalar('quadratic', i**2, global_step=i)
#     writer.add_scalar('exponential', 2**i, global_step=i)
#

#
# from tensorboardX import SummaryWriter
# import numpy as np
#
# writer = SummaryWriter('runs/embedding_example')
# writer.add_histogram('normal_centered', np.random.normal(0, 1, 1000), global_step=1)
# writer.add_histogram('normal_centered', np.random.normal(0, 2, 1000), global_step=50)
# writer.add_histogram('normal_centered', np.random.normal(0, 3, 1000), global_step=100)
#
# from torch.utils.tensorboard import SummaryWriter
# from tensorboardX import SummaryWriter
# import numpy as np
# np.random.seed(20200910)
# writer = SummaryWriter('runs/test1')
# # writer = SummaryWriter('林祖泉的日志文件目录/运行')
# # writer = SummaryWriter('林麻子的日志文件目录')
# for n_iter in range(100):
#     writer.add_scalar('Loss/train', np.random.random(), n_iter)
#     writer.add_scalar('Loss/test', np.random.random(), n_iter)
#     writer.add_scalar('Accuracy/train', np.random.random(), n_iter)
#     writer.add_scalar('Accuracy/test', np.random.random(), n_iter)
#
#
# '''
#
# tensorboard --logdir=runs
#
# '''


# import cv2
#
# vc = cv2.VideoCapture('1.mp4')  # 读入视频文件
# c = 1
#
# if vc.isOpened():  # 判断是否正常打开
#     rval, frame = vc.read()
#     print('success')

# else:
#     rval = False
#
# timeF = 1000  # 视频帧计数间隔频率
#
# while rval:  # 循环读取视频帧
#     rval, frame = vc.read()
#     if (c % timeF == 0):  # 每隔timeF帧进行存储操作
#         cv2.imwrite('image/' + str(c) + '.jpg', frame)  # 存储为图像
#     c = c + 1
#     cv2.waitKey(1)
# vc.release()

# a = [1,2,3,4,5,6,7,8,9,10,11]
#
#
# def find(arr):
#     sta = 0
#     mid = 0
#     for i in range(len(arr)):
#         if arr[i]==5:
#             end =mid + 1
#             print([sta,end])
#             sta=end
#         else:
#             mid += 1
#             print("''''''''''{}".format(mid))
#
# find(a)


import cv2
import string, random


# def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))
#
#
# cap = cv2.VideoCapture("1.mp4")
#
# while cap.isOpened():
#     ret, frame = cap.read()
#     # print('frame.shape:', frame.shape)
#     cv2.imshow('frame', frame)
#
#     key = cv2.waitKey(delay=1)
# #     if key == ord('q'):
# #         break
# #     elif key == ord('s'):
# #         cv2.imwrite(id_generator() + '.jpg', frame)
# #
# cap.release()
# cv2.destroyAllWindows()

# import numpy as np
# import cv2 as cv
# cap = cv.VideoCapture("1.mp4")
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()
# while True:
#     # 逐帧捕获
#     ret, frame = cap.read()
#     # 如果正确读取帧，ret为True
#     if not ret:
#         print("Can't receive frame (stream end?). Exiting ...")
#         break
#     # 我们在框架上的操作到这里
#     gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     # 显示结果帧e
#     cv.imshow('frame', gray)
#     if cv.waitKey(1) == ord('q'):
#         break
# # 完成所有操作后，释放捕获器
# cap.release()
# cv.destroyAllWindows()

# import numpy as np
# import cv2 as cv
# cap = cv.VideoCapture('1.mp4')
# while cap.isOpened():
#   ret, frame = cap.read()
#   # 如果正确读取帧，ret为True
#   if not ret:
#     print("Can't receive frame (stream end?). Exiting ...")
#     break
#   gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#   cv.imshow('frame', gray)
#   if cv.waitKey(60) == ord('q'):
#     break
# cap.release()
# cv.destroyAllWindows()


import cv2
import numpy as np
cap = cv2.VideoCapture('1.mp4')
cap2 = cv2.VideoCapture('2.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
current_frame=00
while(1):
    ret2,frame2 = cap2.read()
    ret ,frame = cap.read()
    if ret != True and ret2!=True:
        break
    framup = np.hstack((frame,frame2))
    cv2.imshow('video',framup)
    key=cv2.waitKey(0) & 0xff
    if key ==ord("q"):
        break
    if key == ord(" "):
        cv2.waitKey(int(1/fps))
    if key ==ord("s"):
        cv2.imwrite('D:/pycharm/untitled2/Demo/output/'+str(current_frame*fps)+'.jpg',framup)
        print("success")
    current_frame += 1
cv2.destroyAllWindows()
cap.release()
cap2.release()















