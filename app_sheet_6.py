

import diagram_maker as dm
import svg_high_level


def main():
    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_a1, file_path=".\\output\\other\\app_sheet_6_diagram_a1.svg")
    dm.draw_diagram(width=256, height=384, commands=cmds_diagram_a2, file_path=".\\output\\other\\app_sheet_6_diagram_a2.svg")
    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_a3, file_path=".\\output\\other\\app_sheet_6_diagram_a3.svg")
    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_b1, file_path=".\\output\\other\\app_sheet_6_diagram_b1.svg")
    dm.draw_diagram(width=256, height=384, commands=cmds_diagram_b2, file_path=".\\output\\other\\app_sheet_6_diagram_b2.svg")


def cmds_diagram_a1(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_2 = dm.ExtPoint(ctx, 0.1, 0.9)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.3, 0.5)
    vx_2 = dm.Vertex(ctx, 0.7, 0.5)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_1 = dm.ExtPoint(ctx, 0.9, 0.1)

    dm.fermion_line(ctx, in_2, vx_1)
    dm.fermion_line(ctx, out_1, vx_2, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.fermion_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.boson_line(ctx, vx_1, in_1)
    dm.boson_line(ctx, vx_2, out_2)

    dm.draw_formula(ctx, r"f", 0.05, 0.9)
    dm.draw_formula(ctx, r"\gamma", 0.95, 0.9)

    dm.draw_formula(ctx, r"f", 0.5, 0.4)

    dm.draw_formula(ctx, r"\gamma", 0.05, 0.1)
    dm.draw_formula(ctx, r"f", 0.95, 0.1)


def cmds_diagram_a2(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    in_2 = dm.ExtPoint(ctx, 0.1, 0.9)

    vx_1 = dm.ExtPoint(ctx, 0.5, 0.3)
    vx_2 = dm.ExtPoint(ctx, 0.5, 0.7)

    out_1 = dm.ExtPoint(ctx, 0.9, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    dm.vertex(ctx, vx_1)
    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, in_1, vx_1, is_anti_particle=True)
    dm.fermion_line(ctx, in_2, vx_2)
    dm.fermion_line(ctx, vx_2, vx_1)

    dm.boson_line(ctx, vx_1, out_1, start_with_dale=True)
    dm.boson_line(ctx, vx_2, out_2)

    dm.draw_formula(ctx, r"\bar{f}", 0.1, 0.05)
    dm.draw_formula(ctx, r"\gamma", 0.9, 0.05)

    dm.draw_formula(ctx, r"f", 0.55, 0.5)

    dm.draw_formula(ctx, r"f", 0.1, 0.95)
    dm.draw_formula(ctx, r"\gamma", 0.9, 0.95)


def cmds_diagram_a3(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    in_2 = dm.ExtPoint(ctx, 0.1, 0.9)

    vx_1 = dm.ExtPoint(ctx, 0.4, 0.3)
    vx_2 = dm.ExtPoint(ctx, 0.4, 0.7)

    out_1 = dm.ExtPoint(ctx, 0.9, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    dm.vertex(ctx, vx_1)
    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_2)

    dm.boson_line(ctx, vx_2, vx_1)

    dm.fermion_line(ctx, vx_1, out_2)
    dm.fermion_line(ctx, vx_2, out_1)

    dm.draw_formula(ctx, r"e", 0.05, 0.1)
    dm.draw_formula(ctx, r"e", 0.95, 0.1)

    dm.draw_formula(ctx, r"\gamma", 0.45, 0.5)

    dm.draw_formula(ctx, r"e", 0.05, 0.9)
    dm.draw_formula(ctx, r"e", 0.95, 0.9)


def cmds_diagram_b1(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_2 = dm.ExtPoint(ctx, 0.1, 0.9)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.3, 0.5)
    vx_2 = dm.Vertex(ctx, 0.7, 0.5)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_1 = dm.ExtPoint(ctx, 0.9, 0.1)

    dm.fermion_line(ctx, in_1, vx_1, is_anti_particle=True)
    dm.fermion_line(ctx, in_2, vx_1)

    dm.fermion_line(ctx, vx_2, out_1, is_anti_particle=True)
    dm.fermion_line(ctx, vx_2, out_2)

    dm.vertex(ctx, vx_1)
    dm.vertex(ctx, vx_2)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.draw_formula(ctx, r"\bar{f}", 0.05, 0.1)
    dm.draw_formula(ctx, r"f", 0.05, 0.9)

    dm.draw_formula(ctx, r"\gamma", 0.5, 0.4)

    dm.draw_formula(ctx, r"\bar{f}", 0.95, 0.1)
    dm.draw_formula(ctx, r"f", 0.95, 0.9)


def cmds_diagram_b2(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    in_2 = dm.ExtPoint(ctx, 0.1, 0.9)

    vx_1 = dm.ExtPoint(ctx, 0.5, 0.3)
    vx_2 = dm.ExtPoint(ctx, 0.5, 0.7)

    out_1 = dm.ExtPoint(ctx, 0.9, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    dm.vertex(ctx, vx_1)
    dm.vertex(ctx, vx_2)

    dm.boson_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_2)
    dm.fermion_line(ctx, vx_2, vx_1)

    dm.fermion_line(ctx, vx_1, out_1, is_anti_particle=True)
    dm.boson_line(ctx, vx_2, out_2)

    dm.draw_formula(ctx, r"\gamma", 0.1, 0.05)
    dm.draw_formula(ctx, r"f", 0.9, 0.05)

    dm.draw_formula(ctx, r"f", 0.55, 0.5)

    dm.draw_formula(ctx, r"f", 0.1, 0.95)
    dm.draw_formula(ctx, r"\gamma", 0.9, 0.95)


if __name__ == "__main__":
    main()
