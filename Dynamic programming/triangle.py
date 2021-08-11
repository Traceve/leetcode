'''
Author: Traceve
Date: 2021-08-11 16:24:49
LastEditTime: 2021-08-11 16:28:18
Description: 
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。

 

示例 1：

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
示例 2：

输入：triangle = [[-10]]
输出：-10
 

提示：

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 

进阶：

你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
'''
class Solution:
    def minimumTotal(self, triangle):
        if len(triangle) < 1:
            return
        elif len(triangle) == 1:
            return triangle[0][0]
        
        # len>1
        paths = triangle[0]  # paths 记录当前的所有路径值
        length = len(triangle)
        for i in range(1, length):
            data = triangle[i]
            size = len(paths)
            temp = []  # temp用于记录新的路径值
            for j in range(size):
                currentValue = paths[j]
                if j == 0:
                    temp.append(currentValue + data[j])  # 正下
                    temp.append(currentValue + data[j + 1])  # 右下
                else:
                    if (currentValue + data[j]) < temp[j]:
                        temp[j] = currentValue + data[j]
                    temp.append(currentValue + data[j + 1])
            paths = temp
        return min(paths)
 
 
if __name__ == '__main__':
    s = Solution()
    ans = s.minimumTotal([
     [2],
    [3, 4],    [6, 5, 7],   [4, 1, 8, 3] ])
#     ans = s.minimumTotal([[2]])
    print (ans)