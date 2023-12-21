
import diagram_maker as dm
import svg_high_level


def main():
    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_2a1, file_path=".\\output\\other\\app_sheet_7_diagram_2a1.svg")
    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_2a2, file_path=".\\output\\other\\app_sheet_7_diagram_2a2.svg")
    dm.draw_diagram(width=384*2, height=256, commands=cmds_diagram_2a, file_path=".\\output\\other\\app_sheet_7_diagram_2a.svg")

    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_3_1, file_path=".\\output\\other\\app_sheet_7_diagram_3_1.svg")
    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_3_2, file_path=".\\output\\other\\app_sheet_7_diagram_3_2.svg")
    dm.draw_diagram(width=384*2, height=256, commands=cmds_diagram_3, file_path=".\\output\\other\\app_sheet_7_diagram_3.svg")


def cmds_diagram_2a(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_diagram_2a1, x=0, y=0, width=0.5, height=1)
    dm.group(ctx, cmds_diagram_2a2, x=1 / 2, y=0, width=0.5, height=1)


def cmds_diagram_2a1(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    in_2 = dm.ExtPoint(ctx, 0.1, 0.9)

    vx_1 = dm.Vertex(ctx, 0.3, 0.5)
    vx_2 = dm.Vertex(ctx, 0.7, 0.5)

    out_1 = dm.ExtPoint(ctx, 0.9, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    dm.fermion_line(ctx, in_2, vx_1)
    dm.fermion_line(ctx, vx_1, vx_2)
    dm.fermion_line(ctx, vx_2, out_2)

    dm.boson_line(ctx, in_1, vx_1, number_of_waves=6, start_with_dale=True)
    dm.boson_line(ctx, vx_2, out_1, number_of_waves=6)

    dm.vertex(ctx, vx_1)
    dm.vertex(ctx, vx_2)

    dm.draw_formula(ctx, r"f", 0.05, 0.9)
    dm.draw_formula(ctx, r"f", 0.95, 0.9)

    dm.draw_formula(ctx, r"f", 0.5, 0.6)

    dm.draw_formula(ctx, r"\gamma", 0.05, 0.1)
    dm.draw_formula(ctx, r"\gamma", 0.95, 0.1)


def cmds_diagram_2a2(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    in_2 = dm.ExtPoint(ctx, 0.1, 0.9)

    vx_1 = dm.Vertex(ctx, 0.3, 0.5)
    vx_2 = dm.Vertex(ctx, 0.7, 0.5)

    out_1 = dm.ExtPoint(ctx, 0.9, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    dm.fermion_line(ctx, in_2, vx_1)
    dm.fermion_line(ctx, vx_1, vx_2)
    dm.fermion_line(ctx, vx_2, out_2)

    dm.boson_line(ctx, in_1, vx_2, number_of_waves=14, start_with_dale=True)
    dm.boson_line(ctx, vx_1, out_1, number_of_waves=14)

    dm.vertex(ctx, vx_1)
    dm.vertex(ctx, vx_2)

    dm.draw_formula(ctx, r"f", 0.05, 0.9)
    dm.draw_formula(ctx, r"f", 0.95, 0.9)

    dm.draw_formula(ctx, r"f", 0.5, 0.6)

    dm.draw_formula(ctx, r"\gamma", 0.05, 0.1)
    dm.draw_formula(ctx, r"\gamma", 0.95, 0.1)


def cmds_diagram_3(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_diagram_3_1, x=0, y=0, width=0.5, height=1)
    dm.group(ctx, cmds_diagram_3_2, x=1 / 2, y=0, width=0.5, height=1)


def cmds_diagram_3_1(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1_a = dm.ExtPoint(ctx, 0.2, 0.1)
    in_1_b = dm.ExtPoint(ctx, 0.2, 0.2)

    in_2_a = dm.ExtPoint(ctx, 0.2, 0.7)
    in_2_b = dm.ExtPoint(ctx, 0.2, 0.8)
    in_2_c = dm.ExtPoint(ctx, 0.2, 0.9)

    out_1_a = dm.ExtPoint(ctx, 0.9, 0.1)

    out_2_b = dm.ExtPoint(ctx, 0.9, 0.8)
    out_2_c = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_l = dm.Vertex(ctx, 0.4, 0.45)
    vx_r = dm.Vertex(ctx, 0.7, 0.45)

    out_m_1 = dm.Vertex(ctx, 0.9, 0.35)
    out_m_2 = dm.Vertex(ctx, 0.9, 0.55)

    dm.fermion_line(ctx, in_1_a, out_1_a)

    dm.fermion_line(ctx, in_2_b, out_2_b)
    dm.fermion_line(ctx, in_2_c, out_2_c)

    dm.fermion_line(ctx, in_1_b, vx_l, is_anti_particle=True)
    dm.fermion_line(ctx, in_2_a, vx_l)

    dm.boson_line(ctx, vx_l, vx_r)

    dm.fermion_line(ctx, vx_r, out_m_1, is_anti_particle=True)
    dm.fermion_line(ctx, vx_r, out_m_2)

    dm.vertex(ctx, vx_l)
    dm.vertex(ctx, vx_r)

    dm.draw_formula(ctx, r"u", 0.15, 0.1)
    dm.draw_formula(ctx, r"\bar{d}", 0.15, 0.2)

    dm.draw_formula(ctx, r"X", 0.95, 0.1)

    dm.draw_formula(ctx, r"d", 0.15, 0.7)
    dm.draw_formula(ctx, r"d", 0.15, 0.8)
    dm.draw_formula(ctx, r"u", 0.15, 0.9)

    dm.draw_formula(ctx, r"Y", 0.95, 0.85)

    dm.draw_formula(ctx, r"e^+", 0.95, 0.35)
    dm.draw_formula(ctx, r"e^-", 0.95, 0.55)

    dm.draw_formula(ctx, r"\gamma", x=0.5, y=0.35)

    dm.draw_formula(ctx, r"\pi^+", 0.05, 0.15)
    dm.draw_formula(ctx, r"n", 0.05, 0.8)

    dm.draw_formula(ctx, r"\{", x=0.1, y=0.15)
    dm.draw_formula(ctx, r"\{", x=0.1, y=0.8)


def cmds_diagram_3_2(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1_a = dm.ExtPoint(ctx, 0.2, 0.1)
    in_1_b = dm.ExtPoint(ctx, 0.2, 0.2)

    in_2_a = dm.ExtPoint(ctx, 0.2, 0.7)
    in_2_b = dm.ExtPoint(ctx, 0.2, 0.8)
    in_2_c = dm.ExtPoint(ctx, 0.2, 0.9)

    out_1_a = dm.ExtPoint(ctx, 0.9, 0.1)

    out_2_b = dm.ExtPoint(ctx, 0.9, 0.8)
    out_2_c = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_l = dm.Vertex(ctx, 0.4, 0.45)
    vx_r = dm.Vertex(ctx, 0.7, 0.45)

    out_m_1 = dm.Vertex(ctx, 0.9, 0.35)
    out_m_2 = dm.Vertex(ctx, 0.9, 0.55)

    dm.fermion_line(ctx, in_1_a, out_1_a)

    dm.fermion_line(ctx, in_2_b, out_2_b)
    dm.fermion_line(ctx, in_2_c, out_2_c)

    dm.fermion_line(ctx, in_1_b, vx_l, is_anti_particle=True)
    dm.fermion_line(ctx, in_2_a, vx_l)

    dm.boson_line(ctx, vx_l, vx_r)

    dm.fermion_line(ctx, vx_r, out_m_1, is_anti_particle=True)
    dm.fermion_line(ctx, vx_r, out_m_2)

    dm.vertex(ctx, vx_l)
    dm.vertex(ctx, vx_r)

    dm.draw_formula(ctx, r"d", 0.15, 0.1)
    dm.draw_formula(ctx, r"\bar{u}", 0.15, 0.2)

    dm.draw_formula(ctx, r"X", 0.95, 0.1)

    dm.draw_formula(ctx, r"u", 0.15, 0.7)
    dm.draw_formula(ctx, r"u", 0.15, 0.8)
    dm.draw_formula(ctx, r"d", 0.15, 0.9)

    dm.draw_formula(ctx, r"Y", 0.95, 0.85)

    dm.draw_formula(ctx, r"\mu^+", 0.95, 0.35)
    dm.draw_formula(ctx, r"\mu^-", 0.95, 0.55)

    dm.draw_formula(ctx, r"\gamma", x=0.5, y=0.35)

    dm.draw_formula(ctx, r"\pi^-", 0.05, 0.15)
    dm.draw_formula(ctx, r"p", 0.05, 0.8)

    dm.draw_formula(ctx, r"\{", x=0.1, y=0.15)
    dm.draw_formula(ctx, r"\{", x=0.1, y=0.8)


if __name__ == "__main__":
    main()
