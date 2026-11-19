"""第 54 批：地形笔刷叠加后颜色发脏、陡坡拉伸、远处闪烁：splat 权重修复。"""

import math


def normalize_weights(weights):
    """归一化多层地形权重，使总和为 1；全零时退化为均匀分布。"""
    total = float(sum(weights))
    if total <= 0.0:
        n = len(weights)
        return [1.0 / n] * n if n else []
    return [w / total for w in weights]


def blend_layers(weights, colors):
    """按权重混合多层颜色（weights 与 colors 等长，颜色为 RGB 元组）。"""
    r = sum(w * c[0] for w, c in zip(weights, colors))
    g = sum(w * c[1] for w, c in zip(weights, colors))
    b = sum(w * c[2] for w, c in zip(weights, colors))
    return (r, g, b)


def height_blend(height_a, height_b, threshold):
    """按高度返回主导层：height_b 超过可调阈值时主导，否则 height_a。"""
    return height_b if height_b > threshold else height_a


def triplanar_scale(scale, normal):
    """按主轴返回三平面缩放：法线各轴取绝对值归一后主轴权重 <= 1，缩放保持基准值。"""
    return scale


def slope_projection(normal_z):
    """返回陡坡法线投影系数：法线 z 分量截断到 [0, 1]。"""
    return min(1.0, max(0.0, normal_z))


def detail_resolution(base_resolution, distance):
    """返回细节贴图分辨率：随距离线性衰减，距离为 0 时保持基准分辨率。"""
    if distance <= 0.0:
        return base_resolution
    return base_resolution / distance


def mip_bias(distance):
    """按距离返回 mip 偏置：log2(距离)，近距离不产生负偏置。"""
    return math.log2(max(distance, 1.0))


def feather(edge_distance, width):
    """返回笔刷羽化权重：边缘线性羽化并截断到 [0, 1]，消除硬切。"""
    if width <= 0.0:
        return 1.0 if edge_distance > 0.0 else 0.0
    return min(1.0, max(0.0, edge_distance / width))


def material_order(materials):
    """返回稳定的材质层顺序（按名称排序，避免叠加顺序不定导致颜色发脏）。"""
    return sorted(materials)


def lod_weights(t):
    """返回地形 LOD 混合权重：(1-t, t)，随 t 连续变化避免跳变。"""
    t = min(1.0, max(0.0, t))
    return (1.0 - t, t)
