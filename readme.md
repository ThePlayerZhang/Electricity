# Electricity
#### *一个使用python的2D游戏制作工具*

---

## 文件格式与定义

- ### 地图文件

<font size=31>

```json
{
  "name": "Testing",
  "background": "#ffffff",
  "data": [ 
    {
      "type": "image", 
      "pos": [0, 0, 0, 0] 
    }
  ]
}
```
</font>

### 解释
- name：该地图的名称
- background：该地图的背景颜色，使用16进制（暂定），默认为 #000000（黑色）
- data：地图中所以包含的元素
  - type：该元素的类型
  - pos：左上的坐标与右下的坐标
  - data：可选，根据元素类型指定内容

### 地图元素类型

- #### 显示类
  - image：渲染图片（需要在data指定图片路径）
  - rect：渲染纯色方形（需要在data指定放开的颜色）
  - ~~func：使用代码渲染（需要在data指定代码）~~ （未实现）
- #### 交互类
  - wall：空气墙 *可配合image使用*
  - portal：传送门
  - trigger：触发器（由 玩家/物体/NPC 触碰触发）
  - button：按钮（由鼠标点击触发）
