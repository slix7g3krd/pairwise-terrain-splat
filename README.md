# pairwise-terrain-splat

地形笔刷叠加后颜色发脏、陡坡拉伸、远处闪烁：splat 权重按顶点色；三层以上不归一；高度混合用固定阈值；三平面映射按世界坐标；陡坡没做法线投影；细节贴图按分辨率；远处 mip 没偏置；笔刷边缘硬切；多层材质顺序固定；地形 LOD 切换权重跳变。render/terrain_splat.py 是核心，tests/test_terrain_splat.py 15个红。要修的是：权重归一；多层混合；高度可调；三平面缩放；坡面投影；细节分辨率；mip 偏置；笔刷羽化；材质排序；LOD 权重连续。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：图形渲染；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
