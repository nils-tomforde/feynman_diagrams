

import diagram_maker as dm
import svg_high_level


def main():

    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_1a, file_path=".\\output\\other\\app_sheet_9_diagram_1a.svg")
    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_2a_1, file_path=".\\output\\other\\app_sheet_9_diagram_2a_1.svg")
    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_2a_2, file_path=".\\output\\other\\app_sheet_9_diagram_2a_2.svg")
    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_2b_1, file_path=".\\output\\other\\app_sheet_9_diagram_2b_1.svg")
    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_2b_2, file_path=".\\output\\other\\app_sheet_9_diagram_2b_2.svg")
    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_3a_1, file_path=".\\output\\other\\app_sheet_9_diagram_3a_1.svg")
    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_3a_2, file_path=".\\output\\other\\app_sheet_9_diagram_3a_2.svg")


def cmds_diagram_1a(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_ = dm.ExtPoint(ctx, 0.1, 0.4)

    vx_1 = dm.Vertex(ctx, 0.4, 0.4)

    vx_2 = dm.Vertex(ctx, 0.6, 0.7)

    out_1 = dm.ExtPoint(ctx, 0.7, 0.1)

    out_2 = dm.ExtPoint(ctx, 0.9, 0.5)
    out_3 = dm.ExtPoint(ctx, 0.9, 0.9)

    dm.fermion_line(ctx, in_, vx_1)
    dm.fermion_line(ctx, vx_1, out_1)

    dm.boson_line(ctx, vx_1, vx_2, start_with_dale=True)

    dm.fermion_line(ctx, vx_2, out_2, is_anti_particle=True)
    dm.fermion_line(ctx, vx_2, out_3)

    dm.vertex(ctx, vx_1)
    dm.vertex(ctx, vx_2)

    dm.draw_formula(ctx, r"u", 0.05, 0.4)
    dm.draw_formula(ctx, r"d", 0.75, 0.1)

    dm.draw_formula(ctx, r"W^+", 0.42, 0.62)

    dm.draw_formula(ctx, r"e^+", 0.95, 0.5)
    dm.draw_formula(ctx, r"\nu_e", 0.95, 0.9)


def cmds_diagram_2a_1(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_2 = dm.ExtPoint(ctx, 0.15, 0.9)
    in_1 = dm.ExtPoint(ctx, 0.15, 0.1)

    vx_1 = dm.Vertex(ctx, 0.3, 0.5)
    vx_2 = dm.Vertex(ctx, 0.7, 0.5)

    out_1 = dm.ExtPoint(ctx, 0.85, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.85, 0.9)

    dm.fermion_line(ctx, in_1, vx_1, is_anti_particle=True)
    dm.fermion_line(ctx, in_2, vx_1)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.boson_line(ctx, vx_2, out_1, number_of_waves=6)
    dm.boson_line(ctx, vx_2, out_2, number_of_waves=6)

    dm.draw_formula(ctx, r"e^+", 0.1, 0.1)
    dm.draw_formula(ctx, r"e^-", 0.1, 0.9)

    dm.draw_formula(ctx, r"\gamma / Z^0", 0.5, 0.4)

    dm.draw_formula(ctx, r"W^+", 0.95, 0.1)
    dm.draw_formula(ctx, r"W^-", 0.95, 0.9)


def cmds_diagram_2a_2(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_2 = dm.ExtPoint(ctx, 0.15, 0.9)
    in_1 = dm.ExtPoint(ctx, 0.15, 0.1)

    vx_1 = dm.Vertex(ctx, 0.3, 0.5)
    vx_2 = dm.Vertex(ctx, 0.7, 0.5)

    out_1 = dm.ExtPoint(ctx, 0.85, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.85, 0.9)

    dm.fermion_line(ctx, in_1, vx_1, is_anti_particle=True)
    dm.fermion_line(ctx, in_2, vx_1)

    dm.vertex(ctx, vx_1)

    dm.scalar_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.boson_line(ctx, vx_2, out_1, number_of_waves=6)
    dm.boson_line(ctx, vx_2, out_2, number_of_waves=6, start_with_dale=True)

    dm.draw_formula(ctx, r"e^+", 0.1, 0.1)
    dm.draw_formula(ctx, r"e^-", 0.1, 0.9)

    dm.draw_formula(ctx, r"H", 0.5, 0.45)

    dm.draw_formula(ctx, r"W^+", 0.95, 0.1)
    dm.draw_formula(ctx, r"W^-", 0.95, 0.9)


def cmds_diagram_2b_1(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_2 = dm.ExtPoint(ctx, 0.15, 0.9)
    in_1 = dm.ExtPoint(ctx, 0.15, 0.1)

    vx_1 = dm.Vertex(ctx, 0.3, 0.5)
    vx_2 = dm.Vertex(ctx, 0.7, 0.5)

    out_1 = dm.ExtPoint(ctx, 0.85, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.85, 0.9)

    dm.fermion_line(ctx, in_1, vx_1, is_anti_particle=True)
    dm.fermion_line(ctx, in_2, vx_1)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.boson_line(ctx, vx_2, out_1, number_of_waves=6)
    dm.boson_line(ctx, vx_2, out_2, number_of_waves=6)

    dm.draw_formula(ctx, r"\bar{\nu}", 0.1, 0.1)
    dm.draw_formula(ctx, r"\nu", 0.1, 0.9)

    dm.draw_formula(ctx, r"Z^0", 0.5, 0.4)

    dm.draw_formula(ctx, r"W^+", 0.95, 0.1)
    dm.draw_formula(ctx, r"W^-", 0.95, 0.9)


def cmds_diagram_2b_2(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_2 = dm.ExtPoint(ctx, 0.15, 0.9)
    in_1 = dm.ExtPoint(ctx, 0.15, 0.1)

    vx_1 = dm.Vertex(ctx, 0.3, 0.5)
    vx_2 = dm.Vertex(ctx, 0.7, 0.5)

    out_1 = dm.ExtPoint(ctx, 0.85, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.85, 0.9)

    dm.fermion_line(ctx, in_1, vx_1, is_anti_particle=True)
    dm.fermion_line(ctx, in_2, vx_1)

    dm.vertex(ctx, vx_1)

    dm.scalar_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.boson_line(ctx, vx_2, out_1, number_of_waves=6)
    dm.boson_line(ctx, vx_2, out_2, number_of_waves=6, start_with_dale=True)

    dm.draw_formula(ctx, r"\bar{\nu}", 0.1, 0.1)
    dm.draw_formula(ctx, r"\nu", 0.1, 0.9)

    dm.draw_formula(ctx, r"H", 0.5, 0.45)

    dm.draw_formula(ctx, r"W^+", 0.95, 0.1)
    dm.draw_formula(ctx, r"W^-", 0.95, 0.9)


def cmds_diagram_3a_1(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1_a = dm.ExtPoint(ctx, 0.2, 0.1)
    in_1_b = dm.ExtPoint(ctx, 0.2, 0.2)
    in_1_c = dm.ExtPoint(ctx, 0.2, 0.3)

    in_2_a = dm.ExtPoint(ctx, 0.2, 0.7)
    in_2_b = dm.ExtPoint(ctx, 0.2, 0.8)
    in_2_c = dm.ExtPoint(ctx, 0.2, 0.9)

    out_1_a = dm.ExtPoint(ctx, 0.9, 0.1)
    out_1_b = dm.ExtPoint(ctx, 0.9, 0.2)

    out_2_b = dm.ExtPoint(ctx, 0.9, 0.8)
    out_2_c = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_l = dm.Vertex(ctx, 0.4, 0.5)
    vx_r = dm.Vertex(ctx, 0.7, 0.5)

    out_m_1 = dm.Vertex(ctx, 0.9, 0.4)
    out_m_2 = dm.Vertex(ctx, 0.9, 0.6)

    dm.fermion_line(ctx, in_1_a, out_1_a)
    dm.fermion_line(ctx, in_1_b, out_1_b)

    dm.fermion_line(ctx, in_2_b, out_2_b, is_anti_particle=True)
    dm.fermion_line(ctx, in_2_c, out_2_c, is_anti_particle=True)

    dm.fermion_line(ctx, in_1_c, vx_l)
    dm.fermion_line(ctx, in_2_a, vx_l, is_anti_particle=True)

    dm.boson_line(ctx, vx_l, vx_r)

    dm.fermion_line(ctx, vx_r, out_m_1)
    dm.fermion_line(ctx, vx_r, out_m_2, is_anti_particle=True)

    dm.vertex(ctx, vx_l)
    dm.vertex(ctx, vx_r)

    dm.draw_formula(ctx, r"u", 0.15, 0.1)
    dm.draw_formula(ctx, r"u", 0.15, 0.2)
    dm.draw_formula(ctx, r"d", 0.15, 0.3)

    dm.draw_formula(ctx, r"X", 0.95, 0.15)

    dm.draw_formula(ctx, r"\bar{u}", 0.15, 0.7)
    dm.draw_formula(ctx, r"\bar{u}", 0.15, 0.8)
    dm.draw_formula(ctx, r"\bar{d}", 0.15, 0.9)

    dm.draw_formula(ctx, r"Y", 0.95, 0.85)

    dm.draw_formula(ctx, r"\ell", 0.95, 0.4)
    dm.draw_formula(ctx, r"\bar{\nu}_\ell", 0.95, 0.6)

    dm.draw_formula(ctx, r"W^-", x=0.55, y=0.38)

    dm.draw_formula(ctx, r"p", 0.05, 0.2)
    dm.draw_formula(ctx, r"\bar{p}", 0.05, 0.8)

    dm.draw_formula(ctx, r"\{", x=0.1, y=0.2)
    dm.draw_formula(ctx, r"\{", x=0.1, y=0.8)


def cmds_diagram_3a_2(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1_a = dm.ExtPoint(ctx, 0.2, 0.1)
    in_1_b = dm.ExtPoint(ctx, 0.2, 0.2)
    in_1_c = dm.ExtPoint(ctx, 0.2, 0.3)

    in_2_a = dm.ExtPoint(ctx, 0.2, 0.7)
    in_2_b = dm.ExtPoint(ctx, 0.2, 0.8)
    in_2_c = dm.ExtPoint(ctx, 0.2, 0.9)

    out_1_a = dm.ExtPoint(ctx, 0.9, 0.1)
    out_1_b = dm.ExtPoint(ctx, 0.9, 0.2)

    out_2_b = dm.ExtPoint(ctx, 0.9, 0.8)
    out_2_c = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_l = dm.Vertex(ctx, 0.4, 0.5)
    vx_r = dm.Vertex(ctx, 0.7, 0.5)

    out_m_1 = dm.Vertex(ctx, 0.9, 0.4)
    out_m_2 = dm.Vertex(ctx, 0.9, 0.6)

    dm.fermion_line(ctx, in_1_a, out_1_a)
    dm.fermion_line(ctx, in_1_b, out_1_b)

    dm.fermion_line(ctx, in_2_b, out_2_b, is_anti_particle=True)
    dm.fermion_line(ctx, in_2_c, out_2_c, is_anti_particle=True)

    dm.fermion_line(ctx, in_1_c, vx_l)
    dm.fermion_line(ctx, in_2_a, vx_l, is_anti_particle=True)

    dm.boson_line(ctx, vx_l, vx_r)

    dm.fermion_line(ctx, vx_r, out_m_1, is_anti_particle=True)
    dm.fermion_line(ctx, vx_r, out_m_2)

    dm.vertex(ctx, vx_l)
    dm.vertex(ctx, vx_r)

    dm.draw_formula(ctx, r"d", 0.15, 0.1)
    dm.draw_formula(ctx, r"u", 0.15, 0.2)
    dm.draw_formula(ctx, r"u", 0.15, 0.3)

    dm.draw_formula(ctx, r"X", 0.95, 0.15)

    dm.draw_formula(ctx, r"\bar{d}", 0.15, 0.7)
    dm.draw_formula(ctx, r"\bar{u}", 0.15, 0.8)
    dm.draw_formula(ctx, r"\bar{u}", 0.15, 0.9)

    dm.draw_formula(ctx, r"Y", 0.95, 0.85)

    dm.draw_formula(ctx, r"\bar{\ell}", 0.95, 0.4)
    dm.draw_formula(ctx, r"\nu_\ell", 0.95, 0.6)

    dm.draw_formula(ctx, r"W^+", x=0.55, y=0.38)

    dm.draw_formula(ctx, r"p", 0.05, 0.2)
    dm.draw_formula(ctx, r"\bar{p}", 0.05, 0.8)

    dm.draw_formula(ctx, r"\{", x=0.1, y=0.2)
    dm.draw_formula(ctx, r"\{", x=0.1, y=0.8)




if __name__ == "__main__":
    main()
