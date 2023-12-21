
import diagram_maker as dm
import svg_high_level


def main():
    dm.draw_diagram(width=384, height=256, commands=cmds_diagram_1a, file_path=".\\output\\other\\app_sheet_8_diagram_1a.svg")
    dm.draw_diagram(width=384*2, height=256, commands=cmds_diagram_2b, file_path=".\\output\\other\\app_sheet_8_diagram_2b.svg")

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

    dm.draw_formula(ctx, r"\mu^-", 0.05, 0.4)
    dm.draw_formula(ctx, r"\nu_\mu", 0.75, 0.1)

    dm.draw_formula(ctx, r"W^-", 0.42, 0.62)

    dm.draw_formula(ctx, r"\bar{\nu}_e", 0.95, 0.5)
    dm.draw_formula(ctx, r"e^-", 0.95, 0.9)



def cmds_diagram_2b(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_diagram_2b1, x=0, y=0, width=1/2, height=1)
    dm.group(ctx, cmds_diagram_2b2, x=1/2, y=0, width=1/2, height=1)


def cmds_diagram_2b1(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.2, 0.4)
    in_2 = dm.ExtPoint(ctx, 0.2, 0.6)

    vx_1 = dm.Vertex(ctx, 0.4, 0.5)
    vx_2 = dm.Vertex(ctx, 0.7, 0.5)

    out_1 = dm.ExtPoint(ctx, 0.9, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    dm.fermion_line(ctx, in_1, vx_1, is_anti_particle=True)
    dm.fermion_line(ctx, in_2, vx_1)

    dm.fermion_line(ctx, vx_2, out_1, is_anti_particle=True)
    dm.fermion_line(ctx, vx_2, out_2)

    dm.vertex(ctx, vx_1)
    dm.vertex(ctx, vx_2)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.draw_formula(ctx, r"\bar{u}", 0.15, 0.4)
    dm.draw_formula(ctx, r"d", 0.15, 0.6)

    dm.draw_formula(ctx, r"\{", 0.1, 0.5, fontsize=35)

    dm.draw_formula(ctx, r"\pi^-", 0.05, 0.5)

    dm.draw_formula(ctx, r"\gamma", 0.55, 0.4)

    dm.draw_formula(ctx, r"\bar{\nu}_\mu", 0.95, 0.1)
    dm.draw_formula(ctx, r"\mu^-", 0.95, 0.9)


def cmds_diagram_2b2(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.2, 0.4)
    in_2 = dm.ExtPoint(ctx, 0.2, 0.6)

    vx_1 = dm.Vertex(ctx, 0.4, 0.5)
    vx_2 = dm.Vertex(ctx, 0.7, 0.5)

    out_1 = dm.ExtPoint(ctx, 0.9, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    dm.fermion_line(ctx, in_1, vx_1, is_anti_particle=True)
    dm.fermion_line(ctx, in_2, vx_1)

    dm.fermion_line(ctx, vx_2, out_1, is_anti_particle=True)
    dm.fermion_line(ctx, vx_2, out_2)

    dm.vertex(ctx, vx_1)
    dm.vertex(ctx, vx_2)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.draw_formula(ctx, r"\bar{u}", 0.15, 0.4)
    dm.draw_formula(ctx, r"d", 0.15, 0.6)

    dm.draw_formula(ctx, r"\{", 0.1, 0.5, fontsize=35)

    dm.draw_formula(ctx, r"\pi^-", 0.05, 0.5)

    dm.draw_formula(ctx, r"\gamma", 0.55, 0.4)

    dm.draw_formula(ctx, r"\bar{\nu}_e", 0.95, 0.1)
    dm.draw_formula(ctx, r"e^-", 0.95, 0.9)


if __name__ == "__main__":
    main()