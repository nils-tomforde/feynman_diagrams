
import diagram_maker as dm
import svg_high_level


def main():
    dm.draw_diagram(width=1028, height=256, commands=cmds_lo_and_nlo_all, file_path=".\\output\\thesis\\diagrams\\diagrams_lo_and_nlo_all.svg")
    dm.draw_diagram(width=1028, height=768, commands=cmds_nnlo_two_jets, file_path=".\\output\\thesis\\diagrams\\diagrams_nnlo_two_jets.svg")
    dm.draw_diagram(width=1028, height=1028, commands=cmds_nnlo_three_jets, file_path=".\\output\\thesis\\diagrams\\diagrams_nnlo_three_jets.svg")
    dm.draw_diagram(width=1028, height=512, commands=cmds_nnlo_four_jets, file_path=".\\output\\thesis\\diagrams\\diagrams_nnlo_four_jets.svg")
    dm.draw_diagram(width=512, height=256, commands=cmds_nnlo_four_jets_quarks, file_path=".\\output\\thesis\\diagrams\\diagrams_nnlo_four_jets_quarks.svg")
    dm.draw_diagram(width=512, height=256, commands=cmds_colors_lo_and_nlo_virtual, file_path=".\\output\\thesis\\diagrams\\diagrams_colors_lo_and_nlo_virtual.svg")


def cmds_lo_and_nlo_all(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_lo, x=0/4, y=0, width=1/4, height=1)
    dm.group(ctx, cmds_nlo_two_jets, x=1/4, y=0, width=1/4, height=1)
    dm.group(ctx, cmds_nlo_three_jets_1, x=2/4, y=0, width=1/4, height=1)
    dm.group(ctx, cmds_nlo_three_jets_2, x=3/4, y=0, width=1/4, height=1)


def cmds_lo(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, out_l)
    dm.fermion_line(ctx, vx, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)


def cmds_nlo_two_jets(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.25 * scaling_x, ym - 0.25)
    vx_r = dm.Vertex(ctx, xm + 0.25 * scaling_x, ym - 0.25)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line(ctx, vx_r, vx_l, center=False, number_of_loops=8)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)
    dm.vertex(ctx, vx_r)


def cmds_nlo_three_jets_1(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.25 * scaling_x, ym - 0.25)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    out_m = dm.ExtPoint(ctx, xm, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l, draw_arrow=False)

    dm.gluon_line(ctx, vx_l, out_m, center=False, number_of_loops=8)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)


def cmds_nlo_three_jets_2(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_r = dm.Vertex(ctx, xm + 0.25 * scaling_x, ym - 0.25)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    out_m = dm.ExtPoint(ctx, xm, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line(ctx, out_m, vx_r, center=False, number_of_loops=8)

    dm.fermion_line(ctx, vx, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_r)


def cmds_colors_lo_and_nlo_virtual(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_lo_colors, x=0/2, y=0, width=1/2, height=1)
    dm.group(ctx, cmds_nlo_two_jets_colors, x=1/2, y=0, width=1/2, height=1)


def cmds_lo_colors(ctx: svg_high_level.Context):
    ctx.set_line_width(2)
    ctx.set_fontsize(20)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, out_l)
    dm.fermion_line(ctx, vx, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.draw_formula(ctx, r"\delta_{ij}",  0.6, 0.6)
    dm.draw_formula(ctx, r"i",  xm - 0.4, 0.2)
    dm.draw_formula(ctx, r"j",  xm + 0.4, 0.2)



def cmds_nlo_two_jets_colors(ctx: svg_high_level.Context):
    ctx.set_line_width(2)
    ctx.set_fontsize(20)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.25 * scaling_x, ym - 0.25)
    vx_r = dm.Vertex(ctx, xm + 0.25 * scaling_x, ym - 0.25)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line(ctx, vx_r, vx_l, center=False, number_of_loops=8)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)
    dm.vertex(ctx, vx_r)

    dm.draw_formula(ctx, r"\delta_{kl}", 0.6, 0.6)

    dm.draw_formula(ctx, r"k", xm - 0.2, 0.5)
    dm.draw_formula(ctx, r"l", xm + 0.2, 0.5)

    dm.draw_formula(ctx, r"T_{ik}^a", xm - 0.3, 0.35)
    dm.draw_formula(ctx, r"T_{lj}^b", xm + 0.3, 0.35)

    dm.draw_formula(ctx, r"\delta_{ab}", xm, 0.225)

    dm.draw_formula(ctx, r"i", xm - 0.4, 0.2)
    dm.draw_formula(ctx, r"j", xm + 0.4, 0.2)


def cmds_nnlo_two_jets(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_nnlo_two_jets_01, x=0/4, y=0, width=1/4, height=1/3)
    dm.group(ctx, cmds_nnlo_two_jets_02, x=1/4, y=0, width=1/4, height=1/3)
    dm.group(ctx, cmds_nnlo_two_jets_03, x=2/4, y=0, width=1/4, height=1/3)
    dm.group(ctx, cmds_nnlo_two_jets_04, x=3/4, y=0, width=1/4, height=1/3)

    dm.group(ctx, cmds_nnlo_two_jets_05, x=0/4, y=1/3, width=1/4, height=1/3)
    dm.group(ctx, cmds_nnlo_two_jets_06, x=1/4, y=1/3, width=1/4, height=1/3)
    dm.group(ctx, cmds_nnlo_two_jets_07, x=2/4, y=1/3, width=1/4, height=1/3)
    dm.group(ctx, cmds_nnlo_two_jets_08, x=3/4, y=1/3, width=1/4, height=1/3)

    dm.group(ctx, cmds_nnlo_two_jets_09, x=0/4, y=2/3, width=1/4, height=1/3)
    dm.group(ctx, cmds_nnlo_two_jets_10, x=1/4, y=2/3, width=1/4, height=1/3)
    dm.group(ctx, cmds_nnlo_two_jets_11, x=2/4, y=2/3, width=1/4, height=1/3)
    dm.group(ctx, cmds_nnlo_two_jets_12, x=3/4, y=2/3, width=1/4, height=1/3)


def cmds_nnlo_two_jets_01(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.15 * scaling_x, ym - 0.15)
    vx_r1 = dm.Vertex(ctx, xm + 0.15 * scaling_x, ym - 0.15)

    vx_l2 = dm.Vertex(ctx, xm - 0.35 * scaling_x, ym - 0.35)
    vx_r2 = dm.Vertex(ctx, xm + 0.35 * scaling_x, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r1, is_anti_particle=True, draw_arrow=False)

    dm.fermion_line(ctx, vx_l1, vx_r1, draw_arrow=False)

    dm.gluon_line(ctx, vx_l2, vx_l1, number_of_loops=4, center=False)
    dm.gluon_line(ctx, vx_r1, vx_r2, number_of_loops=4, center=False)

    dm.fermion_line(ctx, vx_l2, vx_r2, is_anti_particle=True, draw_arrow=False)

    dm.fermion_line(ctx, vx_l2, out_l)
    dm.fermion_line(ctx, vx_r2, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_r1)

    dm.vertex(ctx, vx_l2)
    dm.vertex(ctx, vx_r2)


def cmds_nnlo_two_jets_02(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.15 * scaling_x, ym - 0.15)
    vx_r1 = dm.Vertex(ctx, xm + 0.15 * scaling_x, ym - 0.15)

    vx_l2 = dm.Vertex(ctx, xm - 0.35 * scaling_x, ym - 0.35)
    vx_r2 = dm.Vertex(ctx, xm + 0.35 * scaling_x, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r1, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line(ctx, vx_r1, vx_l1, number_of_loops=4, center=False)

    dm.fermion_line(ctx, vx_l1, vx_l2, draw_arrow=False)
    dm.fermion_line(ctx, vx_r1, vx_r2, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line(ctx, vx_r2, vx_l2, number_of_loops=8, center=False)

    dm.fermion_line(ctx, vx_l2, out_l)
    dm.fermion_line(ctx, vx_r2, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_r1)

    dm.vertex(ctx, vx_l2)
    dm.vertex(ctx, vx_r2)


def cmds_nnlo_two_jets_03(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.15 * scaling_x, ym - 0.15)
    vx_r1 = dm.Vertex(ctx, xm + 0.15 * scaling_x, ym - 0.15)

    vx_l2 = dm.Vertex(ctx, xm - 0.35 * scaling_x, ym - 0.35)
    vx_r2 = dm.Vertex(ctx, xm + 0.35 * scaling_x, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r1, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line(ctx, vx_r1, vx_l2, number_of_loops=6, center=False)

    dm.fermion_line(ctx, vx_l1, vx_l2, draw_arrow=False)
    dm.fermion_line(ctx, vx_r1, vx_r2, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line(ctx, vx_r2, vx_l1, number_of_loops=6, center=False)

    dm.fermion_line(ctx, vx_l2, out_l)
    dm.fermion_line(ctx, vx_r2, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_r1)

    dm.vertex(ctx, vx_l2)
    dm.vertex(ctx, vx_r2)


def cmds_nnlo_two_jets_04(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.15 * scaling_x, ym - 0.15)
    vx_l2 = dm.Vertex(ctx, xm - 0.25 * scaling_x, ym - 0.25)
    vx_l3 = dm.Vertex(ctx, xm - 0.35 * scaling_x, ym - 0.35)

    vx_r = dm.Vertex(ctx, xm + 0.25 * scaling_x, ym - 0.25)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r, is_anti_particle=True, draw_arrow=False)

    dm.fermion_line(ctx, vx_l1, vx_l2, draw_arrow=False)
    dm.fermion_line(ctx, vx_l2, vx_l3, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line_curved(ctx, vx_l1, vx_l3, center=False)

    dm.gluon_line(ctx, vx_r, vx_l2, number_of_loops=8, center=False)

    dm.fermion_line(ctx, vx_l3, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_l2)
    dm.vertex(ctx, vx_l3)

    dm.vertex(ctx, vx_r)


def cmds_nnlo_two_jets_05(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.25 * scaling_x, ym - 0.25)

    vx_r1 = dm.Vertex(ctx, xm + 0.15 * scaling_x, ym - 0.15)
    vx_r2 = dm.Vertex(ctx, xm + 0.25 * scaling_x, ym - 0.25)
    vx_r3 = dm.Vertex(ctx, xm + 0.35 * scaling_x, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_l, is_anti_particle=True, draw_arrow=False)

    dm.fermion_line(ctx, vx_r1, vx_r2, draw_arrow=False)
    dm.fermion_line(ctx, vx_r2, vx_r3, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line_curved(ctx, vx_r3, vx_r1, center=False)

    dm.gluon_line(ctx, vx_r2, vx_l, number_of_loops=8, center=False)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx_r3, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)

    dm.vertex(ctx, vx_r1)
    dm.vertex(ctx, vx_r2)
    dm.vertex(ctx, vx_r3)


def cmds_nnlo_two_jets_06(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.15 * scaling_x, ym - 0.15)
    vx_l2 = dm.Vertex(ctx, xm - 0.35 * scaling_x, ym - 0.35)

    vx_r = dm.Vertex(ctx, xm + 0.35 * scaling_x, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    vx_m = dm.Vertex(ctx, xm, ym - 0.3)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line(ctx, vx_r, vx_m, number_of_loops=4, center=False)
    dm.gluon_line(ctx, vx_m, vx_l2, number_of_loops=4, center=False)
    dm.gluon_line(ctx, vx_l1, vx_m, number_of_loops=4, center=False)

    dm.fermion_line(ctx, vx_l1, vx_l2, draw_arrow=False)

    dm.fermion_line(ctx, vx_l2, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_r)

    dm.vertex(ctx, vx_l2)
    dm.vertex(ctx, vx_r)

    dm.vertex(ctx, vx_m)


def cmds_nnlo_two_jets_07(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.35 * scaling_x, ym - 0.35)

    vx_r1 = dm.Vertex(ctx, xm + 0.15 * scaling_x, ym - 0.15)
    vx_r2 = dm.Vertex(ctx, xm + 0.35 * scaling_x, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    vx_m = dm.Vertex(ctx, xm, ym - 0.3)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_l, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line(ctx, vx_m, vx_l, number_of_loops=4, center=False)
    dm.gluon_line(ctx, vx_r2, vx_m, number_of_loops=4, center=False)
    dm.gluon_line(ctx, vx_m, vx_r1, number_of_loops=4, center=False)

    dm.fermion_line(ctx, vx_r1, vx_r2, draw_arrow=False)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx_r2, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_r1)
    dm.vertex(ctx, vx_l)

    dm.vertex(ctx, vx_r2)
    dm.vertex(ctx, vx_l)

    dm.vertex(ctx, vx_m)


def cmds_nnlo_two_jets_08(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.1 * scaling_x, ym - 0.1)
    vx_l2 = dm.Vertex(ctx, xm - 0.3 * scaling_x, ym - 0.3)
    vx_l3 = dm.Vertex(ctx, xm - 0.4 * scaling_x, ym - 0.4)

    vx_r = dm.Vertex(ctx, xm + 0.4 * scaling_x, ym - 0.4)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r, is_anti_particle=True, draw_arrow=False)

    dm.fermion_line(ctx, vx_l1, vx_l2, draw_arrow=False)
    dm.fermion_line(ctx, vx_l2, vx_l3, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line_curved(ctx, vx_l1, vx_l2, center=False)

    dm.gluon_line(ctx, vx_r, vx_l3, number_of_loops=10, center=False)

    dm.fermion_line(ctx, vx_l3, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_l2)
    dm.vertex(ctx, vx_l3)

    dm.vertex(ctx, vx_r)


def cmds_nnlo_two_jets_09(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.4 * scaling_x, ym - 0.4)

    vx_r1 = dm.Vertex(ctx, xm + 0.1 * scaling_x, ym - 0.1)
    vx_r2 = dm.Vertex(ctx, xm + 0.3 * scaling_x, ym - 0.3)
    vx_r3 = dm.Vertex(ctx, xm + 0.4 * scaling_x, ym - 0.4)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_l, is_anti_particle=True, draw_arrow=False)

    dm.fermion_line(ctx, vx_r1, vx_r2, draw_arrow=False)
    dm.fermion_line(ctx, vx_r2, vx_r3, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line_curved(ctx, vx_r2, vx_r1, center=False)

    dm.gluon_line(ctx, vx_r3, vx_l, number_of_loops=10, center=False)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx_r3, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)

    dm.vertex(ctx, vx_r1)
    dm.vertex(ctx, vx_r2)
    dm.vertex(ctx, vx_r3)


def cmds_nnlo_two_jets_10(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.3 * scaling_x, ym - 0.3)
    vx_r = dm.Vertex(ctx, xm + 0.3 * scaling_x, ym - 0.3)

    vx_ml = dm.Vertex(ctx, xm - 0.2 * scaling_x, ym - 0.3)
    vx_mr = dm.Vertex(ctx, xm + 0.2 * scaling_x, ym - 0.3)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_l, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line_curved(ctx, vx_mr, vx_ml, center=False)
    dm.gluon_line_curved(ctx, vx_ml, vx_mr, center=False)

    dm.gluon_line(ctx, vx_r, vx_mr, number_of_loops=2, center=False)
    dm.gluon_line(ctx, vx_ml, vx_l, number_of_loops=2, center=False)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)
    dm.vertex(ctx, vx_r)

    dm.vertex(ctx, vx_mr)
    dm.vertex(ctx, vx_ml)


def cmds_nnlo_two_jets_11(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.3 * scaling_x, ym - 0.3)
    vx_r = dm.Vertex(ctx, xm + 0.3 * scaling_x, ym - 0.3)

    vx_ml = dm.Vertex(ctx, xm - 0.2 * scaling_x, ym - 0.3)
    vx_mr = dm.Vertex(ctx, xm + 0.2 * scaling_x, ym - 0.3)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_l, is_anti_particle=True, draw_arrow=False)

    dm.ghost_line_curved(ctx, vx_mr, vx_ml, curvature="left", draw_arrow=False)
    dm.ghost_line_curved(ctx, vx_ml, vx_mr, curvature="left", draw_arrow=False)

    dm.gluon_line(ctx, vx_r, vx_mr, number_of_loops=2, center=False)
    dm.gluon_line(ctx, vx_ml, vx_l, number_of_loops=2, center=False)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)
    dm.vertex(ctx, vx_r)

    dm.vertex(ctx, vx_mr)
    dm.vertex(ctx, vx_ml)


def cmds_nnlo_two_jets_12(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.3 * scaling_x, ym - 0.3)
    vx_r = dm.Vertex(ctx, xm + 0.3 * scaling_x, ym - 0.3)

    vx_ml = dm.Vertex(ctx, xm - 0.2 * scaling_x, ym - 0.3)
    vx_mr = dm.Vertex(ctx, xm + 0.2 * scaling_x, ym - 0.3)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_l, is_anti_particle=True, draw_arrow=False)

    dm.fermion_line_curved(ctx, vx_mr, vx_ml, curvature="left", draw_arrow=False)
    dm.fermion_line_curved(ctx, vx_ml, vx_mr, curvature="left", draw_arrow=False)

    dm.gluon_line(ctx, vx_r, vx_mr, number_of_loops=2, center=False)
    dm.gluon_line(ctx, vx_ml, vx_l, number_of_loops=2, center=False)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)
    dm.vertex(ctx, vx_r)

    dm.vertex(ctx, vx_mr)
    dm.vertex(ctx, vx_ml)


def cmds_nnlo_three_jets(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_nnlo_three_jets_01, x=0/4, y=0/4, width=1/4, height=1/4)
    dm.group(ctx, cmds_nnlo_three_jets_02, x=1/4, y=0/4, width=1/4, height=1/4)
    dm.group(ctx, cmds_nnlo_three_jets_04, x=2/4, y=0/4, width=1/4, height=1/4)
    dm.group(ctx, cmds_nnlo_three_jets_05, x=3/4, y=0/4, width=1/4, height=1/4)

    dm.group(ctx, cmds_nnlo_three_jets_06, x=0/4, y=1/4, width=1/4, height=1/4)
    dm.group(ctx, cmds_nnlo_three_jets_07, x=1/4, y=1/4, width=1/4, height=1/4)
    dm.group(ctx, cmds_nnlo_three_jets_08, x=2/4, y=1/4, width=1/4, height=1/4)
    dm.group(ctx, cmds_nnlo_three_jets_09, x=3/4, y=1/4, width=1/4, height=1/4)

    dm.group(ctx, cmds_nnlo_three_jets_10, x=0/4, y=2/4, width=1/4, height=1/4)
    dm.group(ctx, cmds_nnlo_three_jets_11, x=1/4, y=2/4, width=1/4, height=1/4)
    dm.group(ctx, cmds_nnlo_three_jets_12, x=2/4, y=2/4, width=1/4, height=1/4)
    dm.group(ctx, cmds_nnlo_three_jets_13, x=3/4, y=2/4, width=1/4, height=1/4)

    dm.group(ctx, cmds_nnlo_three_jets_03, x=3/8, y=3/4, width=1/4, height=1/4)


def cmds_nnlo_three_jets_01(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.15 * scaling_x, ym - 0.15)
    vx_l2 = dm.Vertex(ctx, xm - 0.35 * scaling_x, ym - 0.35)

    vx_r = dm.Vertex(ctx, xm + 0.35 * scaling_x, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)
    out_m = dm.ExtPoint(ctx, xm, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r, draw_arrow=False)

    dm.fermion_line(ctx, vx_l1, vx_l2, draw_arrow=False)

    dm.gluon_line(ctx, vx_r, vx_l2, center=False, number_of_loops=10)
    dm.gluon_line(ctx, vx_l1, out_m, center=False, number_of_loops=8)

    dm.fermion_line(ctx, vx_l2, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)

    dm.vertex(ctx, vx_l2)
    dm.vertex(ctx, vx_r)


def cmds_nnlo_three_jets_02(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.35 * scaling_x, ym - 0.35)

    vx_r1 = dm.Vertex(ctx, xm + 0.15 * scaling_x, ym - 0.15)
    vx_r2 = dm.Vertex(ctx, xm + 0.35 * scaling_x, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)
    out_m = dm.ExtPoint(ctx, xm, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_l, draw_arrow=False)

    dm.fermion_line(ctx, vx_r1, vx_r2, draw_arrow=False)

    dm.gluon_line(ctx, vx_r2, vx_l, center=False, number_of_loops=10)
    dm.gluon_line(ctx, out_m, vx_r1, center=False, number_of_loops=8)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx_r2, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)

    dm.vertex(ctx, vx_r1)
    dm.vertex(ctx, vx_r2)


def cmds_nnlo_three_jets_03(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.25 * scaling_x, ym - 0.25)

    vx_r = dm.Vertex(ctx, xm + 0.25 * scaling_x, ym - 0.25)

    vx_m = dm.Vertex(ctx, xm, ym - 0.25)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)
    out_m = dm.ExtPoint(ctx, xm, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_l, draw_arrow=False)

    dm.gluon_line(ctx, vx_l, vx_r, center=False, number_of_loops=8)

    dm.gluon_line(ctx, vx_m, out_m, center=False, number_of_loops=6)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)

    dm.vertex(ctx, vx_r)

    dm.vertex(ctx, vx_m)


def cmds_nnlo_three_jets_04(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.15 * scaling_x, ym - 0.15)
    vx_l2 = dm.Vertex(ctx, xm - 0.25 * scaling_x, ym - 0.25)
    vx_l3 = dm.Vertex(ctx, xm - 0.35 * scaling_x, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)
    out_m = dm.ExtPoint(ctx, xm, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)

    dm.fermion_line(ctx, vx_l1, vx_l2, draw_arrow=False)
    dm.fermion_line(ctx, vx_l2, vx_l3, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line_curved(ctx, vx_l1, vx_l3, center=False)

    dm.gluon_line(ctx, vx_l2, out_m, number_of_loops=8, center=False)

    dm.fermion_line(ctx, vx_l3, out_l)
    dm.fermion_line(ctx, vx, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_l2)
    dm.vertex(ctx, vx_l3)


def cmds_nnlo_three_jets_05(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_r1 = dm.Vertex(ctx, xm + 0.15 * scaling_x, ym - 0.15)
    vx_r2 = dm.Vertex(ctx, xm + 0.25 * scaling_x, ym - 0.25)
    vx_r3 = dm.Vertex(ctx, xm + 0.35 * scaling_x, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)
    out_m = dm.ExtPoint(ctx, xm, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r1, draw_arrow=False)

    dm.fermion_line(ctx, vx_r1, vx_r2, draw_arrow=False)
    dm.fermion_line(ctx, vx_r2, vx_r3, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line_curved(ctx, vx_r3, vx_r1, center=False)

    dm.gluon_line(ctx, out_m, vx_r2, number_of_loops=8, center=False)

    dm.fermion_line(ctx, vx, out_l)
    dm.fermion_line(ctx, vx_r3, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_r1)
    dm.vertex(ctx, vx_r2)
    dm.vertex(ctx, vx_r3)


def cmds_nnlo_three_jets_06(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.15 * scaling_x, ym - 0.15)
    vx_l2 = dm.Vertex(ctx, xm - 0.35 * scaling_x, ym - 0.35)

    vx_g = dm.Vertex(ctx, xm - 0.13 * scaling_x, ym - 0.33)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)
    out_m = dm.ExtPoint(ctx, xm, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)

    dm.fermion_line(ctx, vx_l1, vx_l2, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line_curved(ctx, vx_l2, vx_l1, center=False)

    dm.gluon_line(ctx, vx_g, out_m, number_of_loops=6, center=False)

    dm.fermion_line(ctx, vx_l2, out_l)
    dm.fermion_line(ctx, vx, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_l2)

    dm.vertex(ctx, vx_g)


def cmds_nnlo_three_jets_07(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_r1 = dm.Vertex(ctx, xm + 0.15 * scaling_x, ym - 0.15)
    vx_r3 = dm.Vertex(ctx, xm + 0.35 * scaling_x, ym - 0.35)

    vx_g = dm.Vertex(ctx, xm + 0.13 * scaling_x, ym - 0.33)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)
    out_m = dm.ExtPoint(ctx, xm, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r1, draw_arrow=False)

    dm.fermion_line(ctx, vx_r1, vx_r3, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line_curved(ctx, vx_r1, vx_r3, center=False)

    dm.gluon_line(ctx, out_m, vx_g, number_of_loops=6, center=False)

    dm.fermion_line(ctx, vx, out_l)
    dm.fermion_line(ctx, vx_r3, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_r1)
    dm.vertex(ctx, vx_r3)

    dm.vertex(ctx, vx_g)


def cmds_nnlo_three_jets_08(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.15 * scaling_x, ym - 0.15)
    vx_l2 = dm.Vertex(ctx, xm - 0.25 * scaling_x, ym - 0.25)

    vx_r = dm.Vertex(ctx, xm + 0.15 * scaling_x, ym - 0.15)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)
    out_m = dm.ExtPoint(ctx, xm, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line(ctx, vx_r, vx_l1, number_of_loops=4, center=False)

    dm.fermion_line(ctx, vx_l1, vx_l2, draw_arrow=False)

    dm.gluon_line(ctx, vx_l2, out_m, number_of_loops=6, center=False)

    dm.fermion_line(ctx, vx_l2, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_r)

    dm.vertex(ctx, vx_l2)


def cmds_nnlo_three_jets_09(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.15 * scaling_x, ym - 0.15)

    vx_r1 = dm.Vertex(ctx, xm + 0.15 * scaling_x, ym - 0.15)
    vx_r2 = dm.Vertex(ctx, xm + 0.25 * scaling_x, ym - 0.25)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)
    out_m = dm.ExtPoint(ctx, xm, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r1, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line(ctx, vx_r1, vx_l, number_of_loops=4, center=False)

    dm.fermion_line(ctx, vx_r1, vx_r2, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line(ctx, out_m, vx_r2, number_of_loops=6, center=False)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx_r2, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)

    dm.vertex(ctx, vx_r1)
    dm.vertex(ctx, vx_r2)


def cmds_nnlo_three_jets_10(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.1 * scaling_x, ym - 0.1)
    vx_l2 = dm.Vertex(ctx, xm - 0.3 * scaling_x, ym - 0.3)
    vx_l3 = dm.Vertex(ctx, xm - 0.35 * scaling_x, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)
    out_ml = dm.ExtPoint(ctx, xm - 0.2, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)

    dm.fermion_line(ctx, vx_l1, vx_l2, draw_arrow=False)
    dm.fermion_line(ctx, vx_l2, vx_l3, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line_curved(ctx, vx_l1, vx_l2, center=False)

    dm.gluon_line(ctx, vx_l3, out_ml, number_of_loops=4, center=False)

    dm.fermion_line(ctx, vx_l3, out_l)
    dm.fermion_line(ctx, vx, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_l2)
    dm.vertex(ctx, vx_l3)


def cmds_nnlo_three_jets_11(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_r1 = dm.Vertex(ctx, xm + 0.1 * scaling_x, ym - 0.1)
    vx_r2 = dm.Vertex(ctx, xm + 0.3 * scaling_x, ym - 0.3)
    vx_r3 = dm.Vertex(ctx, xm + 0.35 * scaling_x, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)
    out_mr = dm.ExtPoint(ctx, xm + 0.2, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r1, draw_arrow=False)

    dm.fermion_line(ctx, vx_r1, vx_r2, draw_arrow=False)
    dm.fermion_line(ctx, vx_r2, vx_r3, is_anti_particle=True, draw_arrow=False)

    dm.gluon_line_curved(ctx, vx_r2, vx_r1, center=False)

    dm.gluon_line(ctx, out_mr, vx_r3, number_of_loops=4, center=False)

    dm.fermion_line(ctx, vx, out_l)
    dm.fermion_line(ctx, vx_r3, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_r1)
    dm.vertex(ctx, vx_r2)
    dm.vertex(ctx, vx_r3)


def cmds_nnlo_three_jets_12(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.15 * scaling_x, ym - 0.15)
    vx_l2 = dm.Vertex(ctx, xm - 0.35 * scaling_x, ym - 0.35)

    vx_r1 = dm.Vertex(ctx, xm + 0.15 * scaling_x, ym - 0.15)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)
    out_ml = dm.ExtPoint(ctx, xm - 0.2 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r1, is_anti_particle=True, draw_arrow=False)

    dm.fermion_line(ctx, vx_l1, vx_r1, draw_arrow=False)

    dm.gluon_line(ctx, vx_l2, vx_l1, number_of_loops=4, center=False)
    dm.gluon_line(ctx, vx_r1, out_r, number_of_loops=8, center=False)

    dm.fermion_line(ctx, vx_l2, out_ml, is_anti_particle=True)

    dm.fermion_line(ctx, vx_l2, out_l)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_r1)

    dm.vertex(ctx, vx_l2)


def cmds_nnlo_three_jets_13(ctx: svg_high_level.Context):
    ctx.set_line_width(2)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.15 * scaling_x, ym - 0.15)

    vx_r1 = dm.Vertex(ctx, xm + 0.15 * scaling_x, ym - 0.15)
    vx_r2 = dm.Vertex(ctx, xm + 0.35 * scaling_x, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)
    out_mr = dm.ExtPoint(ctx, xm + 0.2 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r1, is_anti_particle=True, draw_arrow=False)

    dm.fermion_line(ctx, vx_l1, vx_r1, draw_arrow=False)

    dm.gluon_line(ctx, out_l, vx_l1, number_of_loops=8, center=False)
    dm.gluon_line(ctx, vx_r1, vx_r2, number_of_loops=4, center=False)

    dm.fermion_line(ctx, out_mr, vx_r2)

    dm.fermion_line(ctx, vx_r2, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_r1)

    dm.vertex(ctx, vx_r2)


def cmds_nnlo_four_jets(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, lambda ctx_: cmds_nnlo_four_jets_01(ctx_, switched=False), x=0/4, y=0, width=1/4, height=1/2)
    dm.group(ctx, lambda ctx_: cmds_nnlo_four_jets_02(ctx_, switched=False), x=1/4, y=0, width=1/4, height=1/2)
    dm.group(ctx, lambda ctx_: cmds_nnlo_four_jets_03(ctx_, switched=False), x=2/4, y=0, width=1/4, height=1/2)
    dm.group(ctx, cmds_nnlo_four_jets_04a, x=3/4, y=0, width=1/4, height=1/2)

    dm.group(ctx, lambda ctx_: cmds_nnlo_four_jets_01(ctx_, switched=True), x=0/4, y=1/2, width=1/4, height=1/2)
    dm.group(ctx, lambda ctx_: cmds_nnlo_four_jets_02(ctx_, switched=True), x=1/4, y=1/2, width=1/4, height=1/2)
    dm.group(ctx, lambda ctx_: cmds_nnlo_four_jets_03(ctx_, switched=True), x=2/4, y=1/2, width=1/4, height=1/2)
    dm.group(ctx, cmds_nnlo_four_jets_04b, x=3/4, y=1/2, width=1/4, height=1/2)

def cmds_nnlo_four_jets_01(ctx: svg_high_level.Context, switched: bool = False):
    ctx.set_line_width(2)
    ctx.set_fontsize(18)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l1 = dm.Vertex(ctx, xm - 0.175 * scaling_x, ym - 0.175)
    vx_l2 = dm.Vertex(ctx, xm - 0.325 * scaling_x, ym - 0.325)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    if not switched:
        out_ml = dm.ExtPoint(ctx, xm - 0.15 * scaling_x, ym - 0.5)
        out_mr = dm.ExtPoint(ctx, xm + 0.15 * scaling_x, ym - 0.5)
    else:
        out_mr = dm.ExtPoint(ctx, xm - 0.15 * scaling_x, ym - 0.5)
        out_ml = dm.ExtPoint(ctx, xm + 0.15 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l1, draw_arrow=False)

    if not switched:
        dm.gluon_line(ctx, vx_l1, out_mr, number_of_loops=8, center=False)
    else:
        dm.gluon_line(ctx, vx_l1, out_mr, number_of_loops=6, center=False)

    dm.fermion_line(ctx, vx_l1, vx_l2, draw_arrow=False)

    if not switched:
        dm.gluon_line(ctx, vx_l2, out_ml, number_of_loops=4, center=False)
    else:
        dm.gluon_line(ctx, vx_l2, out_ml, number_of_loops=8, center=False)

    dm.fermion_line(ctx, vx_l2, out_l)
    dm.fermion_line(ctx, vx, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_l2)

    # if not switched:
    #     dm.draw_formula(ctx, "1", x=xm - 0.15 * scaling_x, y=ym - 0.55)
    #     dm.draw_formula(ctx, "2", x=xm + 0.15 * scaling_x, y=ym - 0.55)
    # else:
    #     dm.draw_formula(ctx, "2", x=xm - 0.15 * scaling_x, y=ym - 0.55)
    #     dm.draw_formula(ctx, "1", x=xm + 0.15 * scaling_x, y=ym - 0.55)


def cmds_nnlo_four_jets_02(ctx: svg_high_level.Context, switched: bool = False):
    ctx.set_line_width(2)
    ctx.set_fontsize(18)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.25 * scaling_x, ym - 0.25)
    vx_r = dm.Vertex(ctx, xm + 0.25 * scaling_x, ym - 0.25)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    if not switched:
        out_ml = dm.ExtPoint(ctx, xm - 0.15 * scaling_x, ym - 0.5)
        out_mr = dm.ExtPoint(ctx, xm + 0.15 * scaling_x, ym - 0.5)
    else:
        out_mr = dm.ExtPoint(ctx, xm - 0.15 * scaling_x, ym - 0.5)
        out_ml = dm.ExtPoint(ctx, xm + 0.15 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l, draw_arrow=False)
    dm.fermion_line(ctx, vx, vx_r, draw_arrow=False, is_anti_particle=True)

    if not switched:
        dm.gluon_line(ctx, vx_l, out_ml, number_of_loops=6, center=False)
        dm.gluon_line(ctx, out_mr, vx_r, number_of_loops=6, center=False)
    else:
        dm.gluon_line(ctx, vx_l, out_ml, number_of_loops=8, center=False)
        dm.gluon_line(ctx, out_mr, vx_r, number_of_loops=8, center=False)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)
    dm.vertex(ctx, vx_r)

    # if not switched:
    #     dm.draw_formula(ctx, "1", x=xm - 0.15 * scaling_x, y=ym - 0.55)
    #     dm.draw_formula(ctx, "2", x=xm + 0.15 * scaling_x, y=ym - 0.55)
    # else:
    #     dm.draw_formula(ctx, "2", x=xm - 0.15 * scaling_x, y=ym - 0.55)
    #     dm.draw_formula(ctx, "1", x=xm + 0.15 * scaling_x, y=ym - 0.55)


def cmds_nnlo_four_jets_03(ctx: svg_high_level.Context, switched: bool = False):
    ctx.set_line_width(2)
    ctx.set_fontsize(18)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_r1 = dm.Vertex(ctx, xm + 0.175 * scaling_x, ym - 0.175)
    vx_r2 = dm.Vertex(ctx, xm + 0.325 * scaling_x, ym - 0.325)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    if not switched:
        out_ml = dm.ExtPoint(ctx, xm - 0.15 * scaling_x, ym - 0.5)
        out_mr = dm.ExtPoint(ctx, xm + 0.15 * scaling_x, ym - 0.5)
    else:
        out_mr = dm.ExtPoint(ctx, xm - 0.15 * scaling_x, ym - 0.5)
        out_ml = dm.ExtPoint(ctx, xm + 0.15 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r1, draw_arrow=False)

    if not switched:
        dm.gluon_line(ctx, out_ml, vx_r1, number_of_loops=8, center=False)
    else:
        dm.gluon_line(ctx, out_ml, vx_r1, number_of_loops=6, center=False)

    dm.fermion_line(ctx, vx_r1, vx_r2, draw_arrow=False)

    if not switched:
        dm.gluon_line(ctx, out_mr, vx_r2, number_of_loops=4, center=False)
    else:
        dm.gluon_line(ctx, out_mr, vx_r2, number_of_loops=8, center=False)

    dm.fermion_line(ctx, vx, out_l)
    dm.fermion_line(ctx, vx_r2, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_r1)
    dm.vertex(ctx, vx_r2)

    # if not switched:
    #     dm.draw_formula(ctx, "1", x=xm - 0.15 * scaling_x, y=ym - 0.55)
    #     dm.draw_formula(ctx, "2", x=xm + 0.15 * scaling_x, y=ym - 0.55)
    # else:
    #     dm.draw_formula(ctx, "2", x=xm - 0.15 * scaling_x, y=ym - 0.55)
    #     dm.draw_formula(ctx, "1", x=xm + 0.15 * scaling_x, y=ym - 0.55)


def cmds_nnlo_four_jets_04a(ctx: svg_high_level.Context):
    ctx.set_line_width(2)
    ctx.set_fontsize(18)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.175 * scaling_x, ym - 0.175)

    vx_m = dm.Vertex(ctx, xm, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    out_ml = dm.ExtPoint(ctx, xm - 0.15 * scaling_x, ym - 0.5)
    out_mr = dm.ExtPoint(ctx, xm + 0.15 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l, draw_arrow=False)

    dm.gluon_line(ctx, vx_l, vx_m, number_of_loops=4, center=False)

    dm.gluon_line(ctx, vx_m, out_mr, number_of_loops=4, center=False)
    dm.gluon_line(ctx, out_ml, vx_m, number_of_loops=4, center=False)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)

    dm.vertex(ctx, vx_m)


def cmds_nnlo_four_jets_04b(ctx: svg_high_level.Context):
    ctx.set_line_width(2)
    ctx.set_fontsize(18)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_r = dm.Vertex(ctx, xm + 0.175 * scaling_x, ym - 0.175)

    vx_m = dm.Vertex(ctx, xm, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    out_ml = dm.ExtPoint(ctx, xm - 0.15 * scaling_x, ym - 0.5)
    out_mr = dm.ExtPoint(ctx, xm + 0.15 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r, draw_arrow=False, is_anti_particle=True)

    dm.gluon_line(ctx, vx_m, vx_r, number_of_loops=4, center=False)

    dm.gluon_line(ctx, vx_m, out_mr, number_of_loops=4, center=False)
    dm.gluon_line(ctx, out_ml, vx_m, number_of_loops=4, center=False)

    dm.fermion_line(ctx, vx, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_r)

    dm.vertex(ctx, vx_m)


def cmds_nnlo_four_jets_quarks(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_nnlo_four_jets_quarks_1, x=0, y=0, width=1/2, height=1)
    dm.group(ctx, cmds_nnlo_four_jets_quarks_2, x=1/2, y=0, width=1/2, height=1)


def cmds_nnlo_four_jets_quarks_1(ctx: svg_high_level.Context):
    ctx.set_line_width(2)
    ctx.set_fontsize(18)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_l = dm.Vertex(ctx, xm - 0.175 * scaling_x, ym - 0.175)

    vx_m = dm.Vertex(ctx, xm, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    out_ml = dm.ExtPoint(ctx, xm - 0.15 * scaling_x, ym - 0.5)
    out_mr = dm.ExtPoint(ctx, xm + 0.15 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_l, draw_arrow=False)

    dm.gluon_line(ctx, vx_l, vx_m, number_of_loops=4, center=False)

    dm.fermion_line(ctx, vx_m, out_ml)
    dm.fermion_line(ctx, vx_m, out_mr, is_anti_particle=True)

    dm.fermion_line(ctx, vx_l, out_l)
    dm.fermion_line(ctx, vx, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_l)

    dm.vertex(ctx, vx_m)


def cmds_nnlo_four_jets_quarks_2(ctx: svg_high_level.Context):
    ctx.set_line_width(2)
    ctx.set_fontsize(18)

    xm = 0.5
    ym = 0.6

    scaling_x = 0.8

    in_ = dm.ExtPoint(ctx, 0.5, 0.9)

    vx = dm.Vertex(ctx, 0.5, 0.6)

    vx_r = dm.Vertex(ctx, xm + 0.175 * scaling_x, ym - 0.175)

    vx_m = dm.Vertex(ctx, xm, ym - 0.35)

    out_l = dm.ExtPoint(ctx, xm - 0.5 * scaling_x, ym - 0.5)
    out_r = dm.ExtPoint(ctx, xm + 0.5 * scaling_x, ym - 0.5)

    out_ml = dm.ExtPoint(ctx, xm - 0.15 * scaling_x, ym - 0.5)
    out_mr = dm.ExtPoint(ctx, xm + 0.15 * scaling_x, ym - 0.5)

    dm.boson_line(ctx, in_, vx, number_of_waves=3)

    dm.fermion_line(ctx, vx, vx_r, draw_arrow=False, is_anti_particle=True)

    dm.gluon_line(ctx, vx_m, vx_r, number_of_loops=4, center=False)

    dm.fermion_line(ctx, vx_m, out_ml)
    dm.fermion_line(ctx, vx_m, out_mr, is_anti_particle=True)

    dm.fermion_line(ctx, vx, out_l)
    dm.fermion_line(ctx, vx_r, out_r, is_anti_particle=True)

    dm.vertex(ctx, vx)

    dm.vertex(ctx, vx_r)

    dm.vertex(ctx, vx_m)


if __name__ == "__main__":
    main()
