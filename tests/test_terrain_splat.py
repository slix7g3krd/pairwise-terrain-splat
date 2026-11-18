import pytest
from render import terrain_splat as mod

CASES = [
    ("weights_sum", "sum(m.normalize_weights([2.0, 2.0])) == approx(1.0)"),
    ("weights_zero", "m.normalize_weights([0.0, 0.0]) == [0.5, 0.5]"),
    ("blend_mid", "m.blend_layers([0.5, 0.5], [(1.0, 0.0, 0.0), (0.0, 1.0, 0.0)]) == approx((0.5, 0.5, 0.0))"),
    ("blend_full", "m.blend_layers([1.0, 0.0], [(0.0, 0.0, 1.0), (1.0, 0.0, 0.0)]) == approx((0.0, 0.0, 1.0))"),
    ("height_high", "m.height_blend(1.0, 2.0, 0.5) == approx(2.0)"),
    ("height_low", "m.height_blend(1.0, 2.0, 2.0) == approx(1.0)"),
    ("triplanar_z", "m.triplanar_scale(2.0, (0.0, 0.0, 1.0)) == approx(2.0)"),
    ("triplanar_x", "m.triplanar_scale(2.0, (1.0, 0.0, 0.0)) == approx(2.0)"),
    ("slope_half", "m.slope_projection(0.5) == approx(0.5)"),
    ("detail_half", "m.detail_resolution(4.0, 2.0) == approx(2.0)"),
    ("mip_two", "m.mip_bias(2.0) == approx(1.0)"),
    ("feather_half", "m.feather(2.0, 4.0) == approx(0.5)"),
    ("feather_clamp", "m.feather(5.0, 4.0) == approx(1.0)"),
    ("order_sorted", "m.material_order(['b', 'a']) == ['a', 'b']"),
    ("lod_mid", "m.lod_weights(0.5) == approx((0.5, 0.5))")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
