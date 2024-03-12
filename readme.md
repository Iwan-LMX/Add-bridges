# Development notice
- Clone it to your IDE, configure the running environment by your self. (Cause I'm using vscode, the path is different to yours)

* Add your '.vscode' and other configure files / folders to '.gitignore'.

- Make a new branch, better name it with your name.


---

## 代码介绍

统计信息:

    1. 统计岛屿坐标与岛屿的value, 每两个相邻的岛屿对进行存储.
    2. 统计岛屿pairs, 两个(row, column相同)相邻岛屿, 表示可以生成桥路
    3. 统计出交叉部位

划分subsets的总元素:

    元素数量 = 岛屿数量Q + 桥数量表示长度 * 2(桥对 数量) + 交叉桥的数量

⭐生成subsets:

    第一步:

        1. 遍历岛屿/节点, (因为节点存储了相邻可以建桥的相邻节点).
        2. 枚举该岛屿与邻居桥lanes的数量的组合. 并将满足岛屿value的组合进行存储.
        3. 同时记录岛屿的序列

    第二步:

        1. 遍历桥对, (这里将会补充上cross节点的信息)
        2. 对于第i个桥对检查这一对岛屿是否出现在cross的记录中
        3. 存在于纪录中的 (交叉桥数量) 这一部分序列位置设为1, 否则设为0
        这一步的是判断是否取用 其对应第一步的组合方案.

⭐Dancing!

    按照X算法的描述步骤, 通过不断的删除行列来获得满足条件的subsets列.

    并将这些行号统计出来.

输出结果:

    只获取答案中 行是第二步生成的这些行.
    通过转化获得这些行对应的 桥对
    然后将桥的信息转化并显示


