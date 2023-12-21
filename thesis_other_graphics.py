
import diagram_maker as dm
import svg_high_level


def main():
    dm.draw_diagram(width=512, height=384, commands=cmds_kinematics_two_particles, file_path=".\\output\\thesis\\other_graphics\\graphic_kinematics_two_particles.svg")
    dm.draw_diagram(width=256, height=256, commands=cmds_backcover, file_path=".\\output\\thesis\\other_graphics\\graphic_backcover.svg")

def cmds_kinematics_two_particles(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)
    # dm.grid(ctx)

    p_a1 = dm.Point(ctx, 0.1, 0.5)
    p_a2 = dm.Point(ctx, 0.47, 0.5)

    p_b1 = dm.Point(ctx, 0.9, 0.5)
    p_b2 = dm.Point(ctx, 0.53, 0.5)

    p_c1 = dm.Point(ctx, 0.52, 0.475)
    p_c2 = dm.Point(ctx, 0.8, 0.1)

    p_d1 = dm.Point(ctx, 0.48, 0.525)
    p_d2 = dm.Point(ctx, 0.2, 0.9)

    dm.draw_arrow(ctx, p_a1, p_a2)
    dm.draw_arrow(ctx, p_b1, p_b2)

    dm.draw_arrow(ctx, p_c1, p_c2)
    dm.draw_arrow(ctx, p_d1, p_d2)

    dm.draw_formula(ctx, r"p_1", 0.06, 0.5)
    dm.draw_formula(ctx, r"p_2", 0.94, 0.5)

    dm.draw_formula(ctx, r"k_1", 0.83, 0.07)
    dm.draw_formula(ctx, r"k_2", 0.17, 0.93)

    dm.draw_formula(ctx, r"\theta", 0.6, 0.45)

    # Arc for the angle

    ctx.path_init(stroke_width=ctx.line_width, fill_opacity=0, stroke_color_rgb=ctx.line_color)
    ctx.path_move_to(0.65 * ctx.scaling_x, 0.5 * ctx.scaling_y)
    ctx.path_rel_quadratic_bezier(0.0 * ctx.scaling_x, -0.07 * ctx.scaling_y,
                                  -0.045 * ctx.scaling_x, -0.14 * ctx.scaling_y)

    ctx.path_finish()


def cmds_backcover(ctx: svg_high_level.Context):
    ctx.set_line_width(4)

    p_l = dm.Point(ctx, 0.1, 0.5)
    p_r = dm.Point(ctx, 0.9, 0.5)

    dm.boson_line_curved(ctx, p_l, p_r, curvature="left")
    dm.boson_line_curved(ctx, p_r, p_l, curvature="left", start_with_dale=True)


if __name__ == "__main__":
    main()
