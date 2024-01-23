

import diagram_maker as dm
import svg_high_level


def main():

    dm.draw_diagram(width=256, height=256, commands=cmds_diagram_2d_hww, file_path=".\\output\\other\\app_sheet_11_diagram_2d_hww.svg")
    dm.draw_diagram(width=256, height=256, commands=cmds_diagram_2d_hhww, file_path=".\\output\\other\\app_sheet_11_diagram_2d_hhww.svg")
    dm.draw_diagram(width=256, height=256, commands=cmds_diagram_2d_hzz, file_path=".\\output\\other\\app_sheet_11_diagram_2d_hzz.svg")
    dm.draw_diagram(width=256, height=256, commands=cmds_diagram_2d_hhzz, file_path=".\\output\\other\\app_sheet_11_diagram_2d_hhzz.svg")
    dm.draw_diagram(width=1024, height=256, commands=cmds_diagram_2d, file_path=".\\output\\other\\app_sheet_11_diagram_2d.svg")


def cmds_diagram_2d(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_diagram_2d_hww, 0, 0, 1/4, 1)
    dm.group(ctx, cmds_diagram_2d_hhww, 1/4, 0, 1/4, 1)
    dm.group(ctx, cmds_diagram_2d_hzz, 2/4, 0, 1/4, 1)
    dm.group(ctx, cmds_diagram_2d_hhzz, 3/4, 0, 1/4, 1)

def cmds_diagram_2d_hww(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.18, 0.4)

    vx = dm.Vertex(ctx, 0.5, 0.4)

    out_1 = dm.ExtPoint(ctx, 0.82, 0.15)
    out_2 = dm.ExtPoint(ctx, 0.82, 0.65)

    dm.scalar_line(ctx, in_1, vx)

    dm.boson_line(ctx, vx, out_1, start_with_dale=False)
    dm.boson_line(ctx, vx, out_2, start_with_dale=True)

    dm.vertex(ctx, vx)

    dm.draw_formula(ctx, r"W^+", 0.925, 0.15)
    dm.draw_formula(ctx, r"W^-", 0.925, 0.65)

    dm.draw_formula(ctx, r"H", 0.075, 0.4)

    dm.draw_formula(ctx, r"HWW \; \mathrm{term}", 0.5, 0.8)


def cmds_diagram_2d_hhww(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.18, 0.15)
    in_2 = dm.ExtPoint(ctx, 0.18, 0.65)

    vx = dm.Vertex(ctx, 0.5, 0.4)

    out_1 = dm.ExtPoint(ctx, 0.82, 0.15)
    out_2 = dm.ExtPoint(ctx, 0.82, 0.65)

    dm.scalar_line(ctx, in_1, vx)
    dm.scalar_line(ctx, in_2, vx)

    dm.boson_line(ctx, vx, out_1, start_with_dale=False)
    dm.boson_line(ctx, vx, out_2, start_with_dale=True)

    dm.vertex(ctx, vx)

    dm.draw_formula(ctx, r"W^+", 0.925, 0.15)
    dm.draw_formula(ctx, r"W^-", 0.925, 0.65)

    dm.draw_formula(ctx, r"H", 0.075, 0.15)
    dm.draw_formula(ctx, r"H", 0.075, 0.65)

    dm.draw_formula(ctx, r"HHWW \; \mathrm{term}", 0.5, 0.8)


def cmds_diagram_2d_hhzz(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.18, 0.15)
    in_2 = dm.ExtPoint(ctx, 0.18, 0.65)

    vx = dm.Vertex(ctx, 0.5, 0.4)

    out_1 = dm.ExtPoint(ctx, 0.82, 0.15)
    out_2 = dm.ExtPoint(ctx, 0.82, 0.65)

    dm.scalar_line(ctx, in_1, vx)
    dm.scalar_line(ctx, in_2, vx)

    dm.boson_line(ctx, vx, out_1, start_with_dale=False)
    dm.boson_line(ctx, vx, out_2, start_with_dale=True)

    dm.vertex(ctx, vx)

    dm.draw_formula(ctx, r"Z", 0.925, 0.15)
    dm.draw_formula(ctx, r"Z", 0.925, 0.65)

    dm.draw_formula(ctx, r"H", 0.075, 0.15)
    dm.draw_formula(ctx, r"H", 0.075, 0.65)

    dm.draw_formula(ctx, r"HHZZ \; \mathrm{term}", 0.5, 0.8)


def cmds_diagram_2d_hzz(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.18, 0.4)

    vx = dm.Vertex(ctx, 0.5, 0.4)

    out_1 = dm.ExtPoint(ctx, 0.82, 0.15)
    out_2 = dm.ExtPoint(ctx, 0.82, 0.65)

    dm.scalar_line(ctx, in_1, vx)

    dm.boson_line(ctx, vx, out_1, start_with_dale=False)
    dm.boson_line(ctx, vx, out_2, start_with_dale=True)

    dm.vertex(ctx, vx)

    dm.draw_formula(ctx, r"Z", 0.925, 0.15)
    dm.draw_formula(ctx, r"Z", 0.925, 0.65)

    dm.draw_formula(ctx, r"H", 0.075, 0.4)

    dm.draw_formula(ctx, r"HZZ \; \mathrm{term}", 0.5, 0.8)



if __name__ == "__main__":
    main()
