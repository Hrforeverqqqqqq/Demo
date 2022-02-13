# # # # # import random
# # # # # import sys
# # # # #
# # # # # def human_guess():
# # # # #     num = random.randint(0, 1000)
# # # # #     i = 0
# # # # #     while 1:
# # # # #         try:
# # # # #             guess = int(input('‘请输入数字0~1000：'))
# # # # #         except ValueError:
# # # # #             print("请输入正确的数字0~1000")
# # # # #             continue
# # # # #         i += 1
# # # # #         if guess > num:
# # # # #             print("猜大了：", guess)
# # # # #         elif guess < num:
# # # # #             print("猜小了：", guess)
# # # # #         else:
# # # # #             print("你猜对了！共猜了", i, "次")
# # # # #             sys.exit(0)
# # # # #
# # # # #
# # # # # def computer_guess():
# # # # #     print('请在心里想一个0~1000范围内的数字')
# # # # #     small = 0
# # # # #     big = 1000
# # # # #     guess = 500
# # # # #     i = 0
# # # # #     while 1:
# # # # #         guess = int((big + small) / 2)
# # # # #         i += 1
# # # # #         print('是这个数吗：' + str(guess) +'\n' +'B:大了，S：小了，C：正确')
# # # # #         char = input()
# # # # #         if char == 'B':
# # # # #             big = guess
# # # # #         elif char == 'S':
# # # # #             small = guess
# # # # #         elif char == 'C':
# # # # #             print("共猜了{0}次，得到正确结果{1}".format(i, guess))
# # # # #             sys.exit(0)
# # # # #         else:
# # # # #             print('请正确输入回答：（B：大了，S：小了，C：正确）')
# # # # #
# # # # #
# # # # # def main():
# # # # #
# # # # #     while True:
# # # # #         who_guess = input('游戏方（D:电脑，W：玩家）:')
# # # # #         if who_guess =="D" and who_guess!=None:
# # # # #             human_guess()
# # # # #         elif who_guess =='W'and who_guess!=None:
# # # # #             computer_guess()
# # # # #
# # # # #
# # # # #
# # # # # if __name__ == '__main__':
# # # # #     main()
# # # #
# # #
# # # import numpy as np
# # # from tkinter import *
# # #
# # #
# # # class Game(object):
# # #     def __init__(self):
# # #         self.chess = np.zeros((3, 3), dtype=int)  # 棋盘状态数组  0---空格  1---叉电脑  2---圈玩家
# # #         self.iscircle = True  # 当前圈下，默认玩家先手
# # #         self.select_i, self.select_j = -1, -1
# # #         self.root = Tk()
# # #         self.root.title('井字棋')
# # #         self.canvas = Canvas(self.root, width=230, height=230, bg="white")
# # #         self.canvas.pack()
# # #         self.canvas.create_rectangle(25, 25, 205, 205, fill="#CA9762")
# # #         for i in range(1, 5):
# # #             self.canvas.create_line(25, 25 + 60 * (i - 1), 205, 25 + 60 * (i - 1))  # 横线
# # #             self.canvas.create_line(25 + 60 * (i - 1), 25, 25 + 60 * (i - 1), 205)  # 竖线
# # #
# # #         self.canvas.bind("<Button-1>", self.player)
# # #         self.root.mainloop()
# # #
# # #     def player(self, event):
# # #         x = event.x
# # #         y = event.y
# # #         if self.iscircle and (25 <= x <= 205) and (25 <= y <= 205):
# # #             i = int((y - 25) / 60)
# # #             j = int((x - 25) / 60)
# # #             if self.chess[i][j] == 0:
# # #                 self.chess[i][j] = 2
# # #                 # 画圈
# # #                 self.drawcircle(i, j)
# # #                 # 画完，判断是否结束游戏
# # #                 self.isGameOver(2)
# # #                 self.iscircle = False
# # #                 # 轮到电脑下
# # #                 self.computer()
# # #
# # #     def win(self, chesstemp, who):
# # #         t = chesstemp.copy()
# # #         for i in range(3):
# # #             if t[i][0] == who and t[i][1] == who and t[i][2] == who:  # 竖直方向
# # #                 return True
# # #             if t[0][i] == who and t[1][i] == who and t[2][i] == who:  # 水平方向
# # #                 return True
# # #         if t[0][0] == who and t[1][1] == who and t[2][2] == who:
# # #             return True
# # #         if t[0][2] == who and t[1][1] == who and t[2][0] == who:
# # #             return True
# # #         return False
# # #
# # #     def isGameOver(self, who):
# # #         # 游戏结束 1、满格平局  2、电脑胜 3、玩家胜
# # #         t = self.chess.copy()
# # #         empty_cells = [(i, j) for i in range(3) for j in range(3) if t[i][j] == 0]
# # #
# # #         if self.win(t, who):
# # #             return True
# # #         else:
# # #             if len(empty_cells) == 0:  # 没有人赢，但是没有空格了,游戏结束
# # #                 return True
# # #             else:  # 游戏没有结束
# # #                 return False
# # #
# # #     def drawcircle(self, i, j):
# # #         x = 25 + 60 * j
# # #         y = 25 + 60 * i
# # #         self.canvas.create_oval(x + 30 - 20, y + 30 - 20, x + 30 + 20, y + 30 + 20)
# # #
# # #     def drawcha(self, i, j):
# # #         x = 25 + 60 * j
# # #         y = 25 + 60 * i
# # #         self.canvas.create_line(x, y, x + 60, y + 60)
# # #         self.canvas.create_line(x + 60, y, x, y + 60)
# # #
# # #     def computer(self):  #
# # #         # 进行 a-b剪枝 ，返回下一步该下的坐标
# # #         if not self.iscircle:
# # #
# # #             i, j, score = self.alphabeta2(self.chess, -10000, 10000, True, 2000000000)
# # #             if 0 <= i < 3 and 0 <= j < 3:
# # #                 print('Computer下棋的位置 ，i ,j ', i, j, score)
# # #                 self.drawcha(i, j)
# # #                 self.chess[i][j] = 1
# # #                 self.isGameOver(1)
# # #                 self.iscircle = True
# # #             '''
# # #             score = self.alphabeta3(self.chess, -10000, 10000, True, True, 6)
# # #             print('Computer下棋的位置 ，i ,j ', self.select_i, self.select_j, score)
# # #             if 0 <= self.select_i < 3 and 0 <= self.select_j < 3:
# # #                 self.drawcha(self.select_i, self.select_j)
# # #                 self.chess[self.select_i][self.select_j] = 1
# # #                 self.isGameOver(1)
# # #                 self.iscircle = True
# # #                 self.select_i, self.select_j=-1,-1
# # # '''
# # #
# # #     def evaluate(self, chessborad):
# # #         temp1 = chessborad.copy()
# # #         temp2 = chessborad.copy()
# # #         '''if self.win(temp2,2):  # 玩家赢
# # #             return -10000
# # #         if self.win(temp1,1):  # 电脑赢
# # #             return 10000'''
# # #         # max
# # #         maxscore = 0
# # #         for i in range(3):
# # #             for j in range(3):
# # #                 if temp1[i][j] == 0:
# # #                     temp1[i][j] = 1
# # #         for i in range(3):
# # #             if temp1[i][0] == 1 and temp1[i][1] == 1 and temp1[i][2] == 1:  # 竖直方向
# # #                 maxscore += 1
# # #             if temp1[0][i] == 1 and temp1[1][i] == 1 and temp1[2][i] == 1:  # 水平方向
# # #                 maxscore += 1
# # #         if temp1[0][0] == 1 and temp1[1][1] == 1 and temp1[2][2] == 1:
# # #             maxscore += 1
# # #         if temp1[0][2] == 1 and temp1[1][1] == 1 and temp1[2][0] == 1:
# # #             maxscore += 1
# # #         # min
# # #         minscore = 0
# # #         for i in range(3):
# # #             for j in range(3):
# # #                 if temp2[i][j] == 0:
# # #                     temp2[i][j] = 2
# # #         for i in range(3):
# # #             if temp2[i][0] == 2 and temp2[i][1] == 2 and temp2[i][2] == 2:  # 竖直方向
# # #                 minscore += 1
# # #             if temp2[0][i] == 2 and temp2[1][i] == 2 and temp2[2][i] == 2:  # 水平方向
# # #                 minscore += 1
# # #         if temp2[0][0] == 2 and temp2[1][1] == 2 and temp2[2][2] == 2:
# # #             minscore += 1
# # #         if temp2[0][2] == 2 and temp2[1][1] == 2 and temp2[2][0] == 2:
# # #             minscore += 1
# # #
# # #         return maxscore - minscore
# # #
# # #     def alphabeta(self, chessborad, alpha, beta, isMax, depth=3):
# # #         tempChess = chessborad.copy()
# # #         if isMax:  # MAX
# # #             alpha_beta = alpha
# # #             empty_cells = [(i, j) for i in range(3) for j in range(3) if tempChess[i][j] == 0]
# # #             if len(empty_cells) != 0:  # 有MIN子节点
# # #                 change_i, change_j = empty_cells[0]
# # #                 for index in range(len(empty_cells)):
# # #                     i, j = empty_cells[index]
# # #                     tempChess[i][j] = 1
# # #                     if self.win(tempChess, 1):
# # #                         score = 10000
# # #                     elif depth == 0:  # 不再向下搜索
# # #                         score = self.evaluate(tempChess)
# # #                     else:
# # #                         temp_i, temp_j, score = self.alphabeta(tempChess, alpha_beta, beta, not isMax, depth - 1)
# # #                     if score > alpha_beta:
# # #                         alpha_beta = score
# # #                         change_i, change_j = i, j
# # #                         print(alpha_beta)
# # #                     print('MAx下棋的位置 ，i ,j ', i, j, score)
# # #                     print(tempChess)
# # #                     if alpha_beta >= beta:
# # #                         print('剪枝了')
# # #                         break
# # #                     tempChess[i][j] = 0
# # #                 print('change,score', change_i, change_j, alpha_beta)
# # #                 return change_i, change_j, alpha_beta
# # #             else:
# # #                 score = self.evaluate(tempChess)
# # #                 if score > alpha_beta:
# # #                     alpha_beta = score
# # #                 return -1, -1, alpha_beta
# # #         else:  # MIN
# # #             alpha_beta = beta
# # #             empty_cells = [(i, j) for i in range(3) for j in range(3) if tempChess[i][j] == 0]
# # #             if len(empty_cells) != 0:  # 有MIN节点
# # #                 change_i, change_j = empty_cells[0]
# # #                 for index in range(len(empty_cells)):
# # #                     i, j = empty_cells[index]
# # #                     tempChess[i][j] = 2
# # #                     if self.win(tempChess, 2):
# # #                         score = -10000
# # #                     elif depth == 0:  # 不再向下搜索
# # #                         score = self.evaluate(tempChess)
# # #                     else:
# # #                         temp_i, temp_j, score = self.alphabeta(tempChess, alpha, alpha_beta, not isMax, depth - 1)
# # #                     if score < alpha_beta:
# # #                         alpha_beta = score
# # #                         change_i, change_j = i, j
# # #                     print('MIN下棋的位置 ，i ,j ', i, j, score)
# # #                     print(tempChess)
# # #                     if alpha_beta <= alpha:
# # #                         print('剪枝了')
# # #                         break
# # #                     tempChess[i][j] = 0
# # #                 print('change,score', change_i, change_j, alpha_beta)
# # #                 return change_i, change_j, alpha_beta
# # #             else:
# # #                 # 深度不为0，但是没有子节点，不再继续向下搜索，将当前节点当做子节点进行评价
# # #                 score = self.evaluate(tempChess)
# # #                 if score < alpha_beta:
# # #                     alpha_beta = score
# # #                 return -1, -1, alpha_beta
# # #
# # #     def alphabeta2(self, chessborad, alpha, beta, isMax, depth=3):
# # #         tempChess = chessborad.copy()
# # #         alpha_beta = alpha if isMax else beta
# # #         empty_cells = [(i, j) for i in range(3) for j in range(3) if tempChess[i][j] == 0]
# # #         if len(empty_cells) != 0:  # 有子节点
# # #             change_i, change_j = empty_cells[0]
# # #             for index in range(len(empty_cells)):
# # #                 i, j = empty_cells[index]
# # #                 tempChess[i][j] = 1 if isMax else 2
# # #                 if self.win(tempChess, 1 if isMax else 2):
# # #                     print('reeeeeeeeeeeeeeeeeeeeee')
# # #                     print(tempChess)
# # #                     if isMax:
# # #                         score = 10000
# # #                     else:
# # #                         score = -10000
# # #                 elif depth == 0:  # 不再向下搜索
# # #                     score = self.evaluate(tempChess)
# # #                 else:
# # #                     if isMax:
# # #                         temp_i, temp_j, score = self.alphabeta2(tempChess, alpha_beta, beta, not isMax, depth - 1)
# # #                     else:
# # #                         temp_i, temp_j, score = self.alphabeta2(tempChess, alpha, alpha_beta, not isMax, depth - 1)
# # #                 if isMax:
# # #                     if score > alpha_beta:
# # #                         alpha_beta = score
# # #                         change_i, change_j = i, j
# # #                     if alpha_beta >= beta:
# # #                         break
# # #                 else:
# # #                     if score < alpha_beta:
# # #                         alpha_beta = score
# # #                         change_i, change_j = i, j
# # #                     if alpha_beta <= alpha:
# # #                         break
# # #                 tempChess[i][j] = 0
# # #             return change_i, change_j, alpha_beta
# # #         else:  # 没有子节点，对当前节点进行评估并返回
# # #             score = self.evaluate(tempChess)
# # #             if isMax and score > alpha_beta:
# # #                 alpha_beta = score
# # #             # MIN
# # #             if not isMax and score < alpha_beta:
# # #                 alpha_beta = score
# # #             return -1, -1, alpha_beta
# # #
# # #
# # # if __name__ == '__main__':
# # #     Game()
# # #
# # #
# # #
# # # -*- coding: utf-8 -*-
# # """
# # Created on Mon Apr 20 10:08:31 2020
# #
# # @author: Administrator
# # """
# #
# # from PIL import Image
# # import os
# # import math
# # import random
# # import pickle
# # from copy import deepcopy
# #
# #
# #
# #
# # # 读取图像
# # def GetImage(ori_img):
# # 	img = Image.open(ori_img)
# # 	color = []
# # 	width, height = img.size
# # 	for j in range(height):
# # 		temp = []
# # 		for i in range(width):
# # 			r, g, b = img.getpixel((i, j))[:3]
# # 			temp.append([r, g, b])
# # 		color.append(temp)
# # 	return color, img.size
# #
# #
# #
# # # 初始化
# # def RandGenes(size):
# # 	width, height = size
# # 	genes = []
# # 	for i in range(100):
# # 		gene = []
# # 		for j in range(height):
# # 			temp = []
# # 			for i in range(width):
# # 				r = random.randint(0, 255)
# # 				g = random.randint(0, 255)
# # 				b = random.randint(0, 255)
# # 				temp.append([r, g, b])
# # 			gene.append(temp)
# # 		genes.append([gene, 0])
# # 	return genes
# #
# #
# #
# # # 计算适应度
# # # 为了方便，定义的并不规范，谨慎参考
# # def CalcFitness(genes, target):
# # 	for k, gene in enumerate(genes):
# # 		count = 0
# # 		for i, row in enumerate(gene[0]):
# # 			for j, col in enumerate(row):
# # 				t_r, t_g, t_b= target[i][j]
# # 				r, g, b= col
# # 				count += (abs(t_r-r) + abs(t_g-g) + abs(t_b-b))
# # 		genes[k][1] = count//2700
# # 	genes.sort(key = lambda x: x[1])
# # 	return genes
# #
# #
# #
# # # 变异
# # def Variation(genes):
# # 	rate = 0.5
# # 	for k, gene in enumerate(genes):
# # 		for i, row in enumerate(gene[0]):
# # 			for j, col in enumerate(row):
# # 				if random.random() < rate:
# # 					liubo=gene[1]//10
# # 					a = [-1, 1][random.randint(0, 1)] * random.randint(0,liubo)
# # 					b = [-1, 1][random.randint(0, 1)] * random.randint(0,liubo)
# # 					c = [-1, 1][random.randint(0, 1)] * random.randint(0,liubo)
# # 					genes[k][0][i][j][0] += a
# # 					genes[k][0][i][j][1] += b
# # 					genes[k][0][i][j][2] += c
# # 	return genes
# #
# #
# #
# #
# # # 交叉
# # def Merge(gene1, gene2, size):
# # 	width, height = size
# # 	y = random.randint(0, width-1)
# # 	x = random.randint(0, height-1)
# # 	new_gene = deepcopy(gene1[0][:x])
# # 	new_gene = [new_gene, 0]
# # 	new_gene[0][x:] = deepcopy(gene2[0][x:])
# # 	new_gene[0][x][:y] = deepcopy(gene1[0][x][:y])
# # 	return new_gene
# #
# #
# #
# # # 自然选择
# # def Select(genes, size):
# # 	seek = len(genes) * 2 // 3
# # 	i = 0
# # 	j = seek + 1
# # 	while i < seek:
# # 		genes[j] = Merge(genes[i], genes[i+1], size)
# # 		j += 1
# # 		i += 2
# # 	return genes
# #
# #
# #
# #
# # # 保存生成的图片
# # def SavePic(gene, generation, ori_img):
# # 	gene = gene[0]
# # 	img = Image.open(ori_img)
# # 	for j, row in enumerate(gene):
# # 		for i, col in enumerate(row):
# # 			r, g, b= col
# # 			img.putpixel((i, j), (r, g, b))
# # 	img.save("D:/test/1111/"+"{}.png".format(generation))
# #
# #
# #
# #
# #
# #
# #
# # # 备份
# # def SaveData(data, backup):
# # 	print('[INFO]: Save data to {}...'.format(backup))
# # 	with open(backup, 'wb') as f:
# # 		pickle.dump(data, f)
# # 	f.close()
# #
# #
# #
# # # 读取备份
# # def ReadData(backup):
# # 	print('[INFO]: Read data from {}...'.format(backup))
# # 	with open(backup, 'rb') as f:
# # 		data = pickle.load(f)
# # 		genes = data['genes']
# # 		generation = data['generation']
# # 	f.close()
# # 	return genes, generation
# #
# #
# #
# #
# #
# #
# #
# # # 运行
# #
# # def run(ori_img, backup, resume=False):
# # 	data, size = GetImage(ori_img)
# # 	if resume:
# # 		genes, generation = ReadData(backup)
# # 	else:
# # 		genes = RandGenes(size)
# # 		generation = 0
# # 	while True:
# # 		genes = Variation(genes)
# # 		genes = CalcFitness(genes, data)
# # 		genes = Select(genes, size)
# # 		generation += 1
# # 		if generation % 1 == 0:
# # 			SaveData({'gene`在这里插入代码片`s': genes, 'generation': generation}, backup)
# #
# # 			SavePic(genes[0], generation, ori_img)
# #
# # 		print('<Generation>: {}, <BestFit-Top3>: {:.4f} {:.4f} {:.4f}'.format(generation, genes[0][1], genes[1][1], genes[2][1]))
# #
# #
# #
# #
# # if __name__ == '__main__':
# # 	# 备份
# # 	backup = r'D:\test\001.bmp'
# # 	# 原始图像
# # 	ori_img =r'D:\test\001.jpg'
# # 	# resume为True则读取备份文件，在其基础上进行自然选择，交叉变异
# # 	run(ori_img, backup, resume=False)
# #
# #coding:utf-8
# # -*- coding: utf-8 -*-
# #代码参考自中国大学mooc人工智能与信息社会（陈斌）
#
# from PIL import Image, ImageDraw
# import os
# import gc
# import random as r
# import minpy.numpy as np
#
# class Color(object):
#     '''
#     定义颜色的类，这个类包含r,g,b,a表示颜色属性
#     '''
#     def __init__(self):
#         self.r = r.randint(0, 255)
#         self.g = r.randint(0, 255)
#         self.b = r.randint(0, 255)
#         self.a = r.randint(95, 115)
#
#
# def mutate_or_not(rate):
#     '''
#     生成随机数，判断是否需要变异
#     '''
#     return True if rate > r.random() else False
#
#
# class Triangle(object):
#     '''
#     定义三角形的类
#     属性：
#             ax,ay,bx,by,cx,cy：表示每个三角形三个顶点的坐标
#             color 			 : 表示三角形的颜色
#             img_t			 : 三角形绘制成的图，用于合成图片
#     方法：
#             mutate_from(self, parent):      从父代三角形变异
#             draw_it(self, size=(256, 256)): 绘制三角形
#     '''
#
#
#     max_mutate_rate = 0.08
#     mid_mutate_rate = 0.3
#     min_mutate_rate = 0.8
#
#
#     def __init__(self, size=(255, 255)):
#         self.ax = r.randint(0, size[0])
#         self.ay = r.randint(0, size[1])
#         self.bx = r.randint(0, size[0])
#         self.by = r.randint(0, size[1])
#         self.cx = r.randint(0, size[0])
#         self.cy = r.randint(0, size[1])
#         self.color = Color()
#         self.img_t = None
#
#
#     def mutate_from(self, parent):
#         if mutate_or_not(self.max_mutate_rate):
#             self.ax = r.randint(0, 255)
#             self.ay = r.randint(0, 255)
#         if mutate_or_not(self.mid_mutate_rate):
#             self.ax = min(max(0, parent.ax + r.randint(-15, 15)), 255)
#             self.ay = min(max(0, parent.ay + r.randint(-15, 15)), 255)
#         if mutate_or_not(self.min_mutate_rate):
#             self.ax = min(max(0, parent.ax + r.randint(-3, 3)), 255)
#             self.ay = min(max(0, parent.ay + r.randint(-3, 3)), 255)
#
#         if mutate_or_not(self.max_mutate_rate):
#             self.bx = r.randint(0, 255)
#             self.by = r.randint(0, 255)
#         if mutate_or_not(self.mid_mutate_rate):
#             self.bx = min(max(0, parent.bx + r.randint(-15, 15)), 255)
#             self.by = min(max(0, parent.by + r.randint(-15, 15)), 255)
#         if mutate_or_not(self.min_mutate_rate):
#             self.bx = min(max(0, parent.bx + r.randint(-3, 3)), 255)
#             self.by = min(max(0, parent.by + r.randint(-3, 3)), 255)
#
#         if mutate_or_not(self.max_mutate_rate):
#             self.cx = r.randint(0, 255)
#             self.cy = r.randint(0, 255)
#         if mutate_or_not(self.mid_mutate_rate):
#             self.cx = min(max(0, parent.cx + r.randint(-15, 15)), 255)
#             self.cy = min(max(0, parent.cy + r.randint(-15, 15)), 255)
#         if mutate_or_not(self.min_mutate_rate):
#             self.cx = min(max(0, parent.cx + r.randint(-3, 3)), 255)
#             self.cy = min(max(0, parent.cy + r.randint(-3, 3)), 255)
#         # color
#         if mutate_or_not(self.max_mutate_rate):
#             self.color.r = r.randint(0, 255)
#         if mutate_or_not(self.mid_mutate_rate):
#             self.color.r = min(max(0, parent.color.r + r.randint(-30, 30)), 255)
#         if mutate_or_not(self.min_mutate_rate):
#             self.color.r = min(max(0, parent.color.r + r.randint(-10, 10)), 255)
#
#         if mutate_or_not(self.max_mutate_rate):
#             self.color.g = r.randint(0, 255)
#         if mutate_or_not(self.mid_mutate_rate):
#             self.color.g = min(max(0, parent.color.g + r.randint(-30, 30)), 255)
#         if mutate_or_not(self.min_mutate_rate):
#             self.color.g = min(max(0, parent.color.g + r.randint(-10, 10)), 255)
#
#         if mutate_or_not(self.max_mutate_rate):
#             self.color.b = r.randint(0, 255)
#         if mutate_or_not(self.mid_mutate_rate):
#             self.color.b = min(max(0, parent.color.b + r.randint(-30, 30)), 255)
#         if mutate_or_not(self.min_mutate_rate):
#             self.color.b = min(max(0, parent.color.b + r.randint(-10, 10)), 255)
#         # alpha
#         if mutate_or_not(self.mid_mutate_rate):
#             self.color.a = r.randint(95, 115)
#         # if mutate_or_not(self.mid_mutate_rate):
#         #     self.color.a = min(max(0, parent.color.a + r.randint(-30, 30)), 255)
#         # if mutate_or_not(self.min_mutate_rate):
#         #     self.color.a = min(max(0, parent.color.a + r.randint(-10, 10)), 255)
#
#
#     def draw_it(self, size=(256, 256)):
#         self.img_t = Image.new('RGBA', size)
#         draw = ImageDraw.Draw(self.img_t)
#         draw.polygon([(self.ax, self.ay),
#                       (self.bx, self.by),
#                       (self.cx, self.cy)],
#                      fill=(self.color.r, self.color.g, self.color.b, self.color.a))
#         return self.img_t
#
#
# class Canvas(object):
#     '''
#     定义每一张图片的类
#     属性：
#             mutate_rate	 : 变异概率
#             size		 : 图片大小
#             target_pixels: 目标图片像素值
#     方法：
#             add_triangles(self, num=1)      : 在图片类中生成num个三角形
#             mutate_from_parent(self, parent): 从父代图片对象进行变异
#             calc_match_rate(self)			: 计算环境适应度
#             draw_it(self, i)				: 保存图片
#     '''
#
#
#     mutate_rate = 0.01
#     size = (256, 256)
#     target_pixels = []
#
#
#     def __init__(self):
#         self.triangles = []
#         self.match_rate = 0
#         self.img = None
#
#
#     def add_triangles(self, num=1):
#         for i in range(0, num):
#             triangle = Triangle()
#             self.triangles.append(triangle)
#
#
#     def mutate_from_parent(self, parent):
#         flag = False
#         for triangle in parent.triangles:
#             t = triangle
#             if mutate_or_not(self.mutate_rate):
#                 flag = True
#                 a = Triangle()
#                 a.mutate_from(t)
#                 self.triangles.append(a)
#                 continue
#             self.triangles.append(t)
#         if not flag:
#             self.triangles.pop()
#             t = parent.triangles[r.randint(0, len(parent.triangles) - 1)]
#             a = Triangle()
#             a.mutate_from(t)
#             self.triangles.append(a)
#
#
#     def calc_match_rate(self):
#         if self.match_rate > 0:
#             return self.match_rate
#         self.match_rate = 0
#         self.img = Image.new('RGBA', self.size)
#         draw = ImageDraw.Draw(self.img)
#         draw.polygon([(0, 0), (0, 255), (255, 255), (255, 0)], fill=(255, 255, 255, 255))
#         for triangle in self.triangles:
#             self.img = Image.alpha_composite(self.img, triangle.img_t or triangle.draw_it(self.size))
#         # 与下方代码功能相同，此版本便于理解但效率低
#         # pixels = [self.img.getpixel((x, y)) for x in range(0, self.size[0], 2) for y in range(0, self.size[1], 2)]
#         # for i in range(0, min(len(pixels), len(self.target_pixels))):
#         #     delta_red   = pixels[i][0] - self.target_pixels[i][0]
#         #     delta_green = pixels[i][1] - self.target_pixels[i][1]
#         #     delta_blue  = pixels[i][2] - self.target_pixels[i][2]
#         #     self.match_rate += delta_red   * delta_red   + \
#         #                        delta_green * delta_green + \
#         #                        delta_blue  * delta_blue
#         arrs = [np.array(x) for x in list(self.img.split())]    # 分解为RGBA四通道
#         for i in range(3):                                      # 对RGB通道三个矩阵分别与目标图片相应通道作差取平方加和评估相似度
#             self.match_rate += np.sum(np.square(arrs[i]-self.target_pixels[i]))[0]
#
#     def draw_it(self, i):
#         #self.img.save(os.path.join(PATH, "%s_%d_%d_%d.png" % (PREFIX, len(self.triangles), i, self.match_rate)))
#         self.img.save(os.path.join(PATH, "%d.png" % (i)))
#
#
# def main():
#         global LOOP, PREFIX, PATH, TARGET, TRIANGLE_NUM
#         # 声明全局变量
#         img = Image.open(TARGET).resize((256, 256)).convert('RGBA')
#         size = (256, 256)
#         Canvas.target_pixels = [np.array(x) for x in list(img.split())]
#         # 生成一系列的图片作为父本，选择其中最好的一个进行遗传
#         parentList = []
#         for i in range(20):
#             print('正在生成第%d个初代个体' % (i))
#             parentList.append(Canvas())
#             parentList[i].add_triangles(TRIANGLE_NUM)
#             parentList[i].calc_match_rate()
#         parent = sorted(parentList, key=lambda x: x.match_rate)[0]
#         del parentList
#         gc.collect()
#         # 进入遗传算法的循环
#         i = 0
#         while i < 30000:
#             childList = []
#             # 每一代从父代中变异出10个个体
#             for j in range(10):
#                 childList.append(Canvas())
#                 childList[j].mutate_from_parent(parent)
#                 childList[j].calc_match_rate()
#             child = sorted(childList, key=lambda x: x.match_rate)[0]
#             # 选择其中适应度最好的一个个体
#             del childList
#             gc.collect()
#             parent.calc_match_rate()
#             if i % LOOP == 0:
#                 print ('%10d parent rate %11d \t child1 rate %11d' % (i, parent.match_rate, child.match_rate))
#             parent = parent if parent.match_rate < child.match_rate else child
#             # 如果子代比父代更适应环境，那么子代成为新的父代
#             # 否则保持原样
#             child = None
#             if i % LOOP == 0:
#                 # 每隔LOOP代保存一次图片
#                 parent.draw_it(i)
#                 #print(parent.match_rate)
#                 #print ('%10d parent rate %11d \t child1 rate %11d' % (i, parent.match_rate, child.match_rate))
#             i += 1
#
#
# '''
# 定义全局变量，获取待处理的图片名
# '''
# NAME = input('请输入原图片文件名：')
# LOOP = 100
# PREFIX = NAME.split('/')[-1].split('.')[0]  # 取文件名
# PATH = os.path.abspath('.')  # 取当前路径
# PATH = os.path.join(PATH,'results')
# TARGET = NAME  # 源图片文件名
# TRIANGLE_NUM = 256  # 三角形个数
#
# if __name__ == '__main__':
#     #print('开始进行遗传算法')
#     main()
#
# i=0
# var = 1
# while var==1:
#     a=int(input())
#     if a%2==0:
#         b = a+1
#     else:
#         b=a
#     i=i+1
#     if b==a:
#         break
# print(i)

# class Test:
#     def prt(self):
#         print("hello!")
# t = Test()
# t.prt()
#

# def find(a,b):
#     a1 = sorted(a)
#     print(a1)
#     b1 = sorted(b)
#     print(b1)
#     i = 0
#     j = 0
#     while(i<len(a1) and j<len(b1)):
#         if(a1[i]<=b1[j]):
#             j=j+1
#         i = i + 1
#
#     return i
#
# print(find([1,2],[1,2,3]))
# import numpy as np
#
# a=np.array([1,2])
# b=np.array([1,2,3])
# print(len(a)&len(b))
# print(len(a) and len(b))
# [[1,2], [2,4], [1,3]]

# import numpy as np
#
# def Tosum(a,target):
#     j=len(a)-1
#     i=0
#     while True:
#         sum = a[i] + a[j]
#         if sum==target:
#             return [i,j]
#         if sum<target:
#             i=i+1
#         else:
#             j=j-1
#     # for i in range(len(a)):
#     #     for j in range(len(a)):
#     #         sum=a[i]+a[j]
#     #         if sum==target:
#     #             return [i,j]
#     #         if sum<target:
#     #             i=i+1
#     #         else:
#     #             j=j-1
#
# b=Tosum([2,7,11,15],9)
# print(b)


# import numpy as np
#
# def merge(a,b):
#     i=len(b)-1
#     j=len(a)-1
#     print(i,j,a[j],b[i])
#     while True:
#         if a[j]<b[i]:
#             a[j]=b[i]
#         j=j-1
#         i=i-1
#         if i+1==0:
#             return sorted(a)
#
# x = merge([1,2,3,0,0,0],[2,5,6])
#
# print(x)
# def mySqrt(a):
#     if a==0:
#         return a
#     l = 1
#     r = a
#     while(l<=r):
#         mid = l + (r - l ) / 2
#         # mid = l + (r - l) / 2
#         sqrt=a/mid
#         if sqrt==mid:
#             return mid
#         elif mid>sqrt:
#             r=mid-1
#         else:
#             l=mid+1
#     # if (a == 0) :
#     #     return a
#     # l = 1
#     # r = a
#     # while (l <= r) :
#     #     mid = l + (r - l) / 2
#     #     sqrt = a / mid
#     #     if (sqrt == mid) :
#     #         return mid
#     #     elif(mid > sqrt):
#     #         r = mid - 1
#     #     else :
#     #         l = mid + 1
#
#     return r
#     # x = a
#     # while (x * x > a):
#     #     x = (x + a / x) / 2
#     # return x
#
#
#
# x = mySqrt(8)
# print(x)
#
#
# strs = ['a', 'ab', 'abc', 'abcd']
# dicts ={}
# for i in range(len(strs)):
#     dicts[i] = strs[i]
#     print(dicts[i])
# print(dicts)

# def add(x:int, y:int) -> int:
#     return x + y
#
# print(add(2,3))

# import random
#
# d = {x: random.randint(60, 101) for x in "abcdxyz"}
# print(d)
# a = d.items()
# print(a)
# s = sorted(a,key= lambda x:x[1])
# print(s)
#
# add=lambda x,y:y+x
# print(add(1,2))

# a=2
# b=1
# c=2
# print(a is b)
# print(a==c)


# l1 = ['b','c','d','b','c','a','a']
# l2 = list(set(l1))
# print(l2)

# s = 'ilovechina'
# x = list(s)
# print(x)
# x.reverse()
# print(x)
# print(''.join(x))

# def foo(name):
#   return 'hello %s' % name
# # 2. format()
# def foo1(name):
#   return 'hello {}'.format(name)
# # f-string
# def foo2(name):
#   return f'hello {name}'
# a=foo(name='ksl')
# b=foo1(name='ksl')
# c=foo2(name='ksl')
#
# print(a,b,c)
#
# print('hello{}'.format('sdsa'))
# s = " adabdw "
#
#
# print(s.strip('a'))
#

# s = '123456'
#
# print(s[:2])
#


# a = 'python'
#
# b = a[::-1]
#
# print(b)  # nohtyp
#
# c = a[:-2]
#
# print(c)  # nhy
#
# a=[0,1,2,3,4,5,6,7,8,9]
# b=a[::-1]
# print(b)

# a='AAAAAa'
# print(a.lower())
# print("aaaaaaa")

# strip()除去空格
# split()分割
# set()无序不重复元素集合交、并、差
# tuple(list) # tuple转list
# list(tuple) # list 转tuple
# read将整个文本都读取为一个字符串，占用内存大，
# readline读取为一个生成器，支持遍历和迭代，占用空间小。
# readlines将文本读取为列表，占用空间大
# 列表、元组添加数据可以用extend()
# 列表中可以append可以添加单个元素，两个列表合并时可以直接相加
# zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组）




# # 奇技淫巧
# list_a = [1,2,3,4,5,6]
# list_b = [2,3,6]
# set1 = set(list_a)
# print(set1)
# set2 = set(list_b)
# print(set2)
# # 相同元素
# print(set1&set2)
# # 不同元素
# print(set1^set2)

# mm = [[1,2],[3,4],[5,6]]
# b=[j for a in mm for j in a]
# print(b)

# a = [1,5,7,9]
# b = [2,2,6,8]
# # 方法1
# # a.extend(b)
# # print(a)
# # 方法2
# # a[0:0] = b
# # print(a)
# # 方法3
# a += b
# print(a)
# a = {'a':1,'b':2}
# b = {'c':3,'d':4}
# c = {}
# # c.update(a)
# # c.update(b)
# # # 2.
# # c = dict(a,**b)
# # 3.
# c = {**a,**b} # 官方推荐这种方式
# print(c)
# a = ('a','b')
# b = (1,2)
# z=zip(a,b)
# print(z)
# c = dict(z)
# print(c)

# def mul(n):
#   def wrapper():
#     print(n*2)
#
#
# a = mul(2)
#
# print(a)

# #闭包函数的实例
# # outer是外部函数 a和b都是外函数的临时变量
# def outer( a ):
#     b = 10
#     # inner是内函数
#     def inner():
#         #在内函数中 用到了外函数的临时变量
#         print(a+b)
#     # 外函数的返回值是内函数的引用
#     return inner
#
# if __name__ == '__main__':
#     # 在这里我们调用外函数传入参数5
#     #此时外函数两个临时变量 a是5 b是10 ，并创建了内函数，然后把内函数的引用返回存给了demo
#     # 外函数结束的时候发现内部函数将会用到自己的临时变量，这两个临时变量就不会释放，会绑定给这个内部函数
#     demo = outer(5)
#     # 我们调用内部函数，看一看内部函数是不是能使用外部函数的临时变量
#     # demo存了外函数的返回值，也就是inner函数的引用，这里相当于执行inner函数
#     demo() # 15
#
#     demo2 = outer(7)
#     demo2()#17


# _call_ 可以把类实例当做函数调用
# class Bar:
#     def __call__(self, *args, **kwargs):
#
#
#         print('in call')
#
# if __name__ == '__main__':
#     b = Bar()
#     b()



import cv2
import copy
import math

img=cv2.imread('D:/1.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度处理

# cv2.threshold(gray,140,255,0,gray)#二值化函数

print(img.shape)
logc=copy.deepcopy(gray)
rows=img.shape[0]
cols=img.shape[1]
for i in range(rows):
    for j in range(cols):
        logc[i][j]=255-logc[i][j]



cv2.imshow('img',img)
cv2.imshow('img1',gray)
cv2.imshow('logc',logc)


# print(gray)


cv2.waitKey(0)














