# coding: utf-8

from random import random

def creat_rectangle(number, max_width, max_height):
  ret = []
  for _ in range(number):
    ret.append((int(random() * max_width) + 1, int(random() * max_height) + 1))
  return ret

if __name__ == '__main__':
# 生成100个矩形，矩形最大宽100px 最大高100px
  rectangle_list = creat_rectangle(100, max_width=100, max_height=100)
# 将100个矩形按宽高排序
  print rectangle_list
  rectangle_list.sort(reverse=True)
  print rectangle_list


# 拆分剩余rect为left和right两个分支。
# ●---------●-----------------
# | picture |   right        |
# |         |                |
# ●---------------------------
# |                          |
# |        left              |
# |                          |
# |                          |
# |                          |
# ----------------------------
# 看图片, 主要通过三个● 和三块区域。迭代操作就是：继续对left进行分割，或者是right进行分割。
# 采用二叉树数据结构
# 按照上图的思路，采用二叉树数据结构。怎么将图片一个个插入到二叉树中呢？有一下几种方法：
# ● 前序遍历
# ● 后序遍历
# ● 中序遍历
# ● 层序遍历













