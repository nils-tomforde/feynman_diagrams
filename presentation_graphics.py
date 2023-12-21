import thesis_diagrams
import thesis_diagrams_nnlo as nnlo
import thesis_feynman_rules
import thesis_other_graphics

import diagram_maker as dm
import svg_high_level


def main():
    dm.draw_diagram(width=256, height=512, commands=lambda ctx: thesis_diagrams.cmds_standard_process(ctx, "fermions", True), file_path=".\\output\\presentation\\diagrams\\diagram_tree_level_fermions_momenta.svg")
    dm.draw_diagram(width=256, height=512, commands=lambda ctx: thesis_diagrams.cmds_virtual_gluon_process(ctx, True), file_path=".\\output\\presentation\\diagrams\\diagram_virtual_momenta.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_virtual_vanishing(ctx), file_path=".\\output\\presentation\\diagrams\\diagrams_virtual_scaleless.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: thesis_diagrams.cmds_real_gluon_emission_both(ctx, True), file_path=".\\output\\presentation\\diagrams\\diagrams_emission_momenta.svg")

    dm.draw_diagram(width=512, height=256, commands=nnlo.cmds_colors_lo_and_nlo_virtual, file_path=".\\output\\presentation\\diagrams\\diagrams_colors_lo_and_nlo_virtual.svg")

    dm.draw_diagram(width=256*10, height=256*4, commands=cmds_nnlo_diagrams, file_path=".\\output\\presentation\\diagrams\\diagrams_nnlo_diagrams.svg")
    dm.draw_diagram(width=256*10, height=256*4 + 32*4, commands=cmds_nnlo_diagrams_with_description, file_path=".\\output\\presentation\\diagrams\\diagrams_nnlo_diagrams_with_description.svg")

    dm.draw_diagram(width=512, height=384, commands=cmds_kinematics_two_particles, file_path=".\\output\\presentation\\other_graphics\\graphic_kinematics_two_particles.svg")


def cmds_virtual_vanishing(ctx: svg_high_level.Context):
    ctx.set_fontsize(40)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, thesis_diagrams.cmds_virtual_gluon_process_scaleless_1, x=0, y=0, width=1/2, height=1)
    dm.group(ctx, thesis_diagrams.cmds_virtual_gluon_process_scaleless_2, x=1/2, y=0, width=1/2, height=1)


def cmds_nnlo_diagrams_with_description(ctx: svg_high_level.Context):
    ctx.set_fontsize(40)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_nnlo_diagrams, x=0, y=1/8, width=1, height=7/8)

    dm.draw_formula(ctx, r"\gamma^\ast \rightarrow q \bar{q}", x=1.5/10, y=1/16)
    dm.draw_formula(ctx, r"\gamma^\ast \rightarrow q \bar{q} g", x=5/10, y=1/16)
    dm.draw_formula(ctx, r"\gamma^\ast \rightarrow q \bar{q} g g", x=8/10, y=1/16)
    dm.draw_formula(ctx, r"\gamma^\ast \rightarrow q \bar{q} q \bar{q}", x=9.5/10, y=1/16)

    dm.group(ctx, lambda ctx_: dm.draw_formula(ctx_, r"\{", x=0, y=0, fontsize=60), x=1.5/10, y=1.7/16, width=3/10, height=1.5/10, rotation_angle=90, scale_x=2, scale_y=10)
    dm.group(ctx, lambda ctx_: dm.draw_formula(ctx_, r"\{", x=0, y=0, fontsize=60), x=5/10, y=1.7/16, width=3/10, height=1.5/10, rotation_angle=90, scale_x=2, scale_y=10*4/3)
    dm.group(ctx, lambda ctx_: dm.draw_formula(ctx_, r"\{", x=0, y=0, fontsize=60), x=8/10, y=1.7/16, width=3/10, height=1.5/10, rotation_angle=90, scale_x=2, scale_y=10*2/3)
    dm.group(ctx, lambda ctx_: dm.draw_formula(ctx_, r"\{", x=0, y=0, fontsize=60), x=9.5/10, y=1.7/16, width=3/10, height=1.5/10, rotation_angle=90, scale_x=2, scale_y=10*1/3)


def cmds_nnlo_diagrams(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    # Two jets
    dm.group(ctx, nnlo.cmds_nnlo_two_jets_01, x=0/10, y=0/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_two_jets_02, x=1/10, y=0/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_two_jets_03, x=2/10, y=0/4, width=1/10, height=1/4)

    dm.group(ctx, nnlo.cmds_nnlo_two_jets_04, x=0/10, y=1/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_two_jets_06, x=1/10, y=1/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_two_jets_08, x=2/10, y=1/4, width=1/10, height=1/4)

    dm.group(ctx, nnlo.cmds_nnlo_two_jets_05, x=0/10, y=2/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_two_jets_07, x=1/10, y=2/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_two_jets_09, x=2/10, y=2/4, width=1/10, height=1/4)

    dm.group(ctx, nnlo.cmds_nnlo_two_jets_10, x=0/10, y=3/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_two_jets_11, x=1/10, y=3/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_two_jets_12, x=2/10, y=3/4, width=1/10, height=1/4)

    # Three jets
    dm.group(ctx, nnlo.cmds_nnlo_three_jets_01, x=3/10, y=0/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_three_jets_04, x=4/10, y=0/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_three_jets_06, x=5/10, y=0/4, width=1/10, height=1/4)

    dm.group(ctx, nnlo.cmds_nnlo_three_jets_02, x=3/10, y=1/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_three_jets_05, x=4/10, y=1/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_three_jets_07, x=5/10, y=1/4, width=1/10, height=1/4)

    dm.group(ctx, nnlo.cmds_nnlo_three_jets_08, x=3/10, y=2/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_three_jets_10, x=4/10, y=2/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_three_jets_12, x=5/10, y=2/4, width=1/10, height=1/4)

    dm.group(ctx, nnlo.cmds_nnlo_three_jets_09, x=3/10, y=3/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_three_jets_11, x=4/10, y=3/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_three_jets_13, x=5/10, y=3/4, width=1/10, height=1/4)

    dm.group(ctx, nnlo.cmds_nnlo_three_jets_03, x=6/10, y=1.5/4, width=1/10, height=1/4)

    # Four jets
    dm.group(ctx, lambda ctx_: nnlo.cmds_nnlo_four_jets_01(ctx_, switched=False), x=7/10, y=0/4, width=1/10, height=1/4)
    dm.group(ctx, lambda ctx_: nnlo.cmds_nnlo_four_jets_01(ctx_, switched=True), x=7/10, y=1/4, width=1/10, height=1/4)
    dm.group(ctx, lambda ctx_: nnlo.cmds_nnlo_four_jets_02(ctx_, switched=False), x=7/10, y=2/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_four_jets_04a, x=7/10, y=3/4, width=1/10, height=1/4)

    dm.group(ctx, lambda ctx_: nnlo.cmds_nnlo_four_jets_03(ctx_, switched=False), x=8/10, y=0/4, width=1/10, height=1/4)
    dm.group(ctx, lambda ctx_: nnlo.cmds_nnlo_four_jets_03(ctx_, switched=True), x=8/10, y=1/4, width=1/10, height=1/4)
    dm.group(ctx, lambda ctx_: nnlo.cmds_nnlo_four_jets_02(ctx_, switched=True), x=8/10, y=2/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_four_jets_04b, x=8/10, y=3/4, width=1/10, height=1/4)

    # Four jets (quarks)
    dm.group(ctx, nnlo.cmds_nnlo_four_jets_quarks_1, x=9/10, y=0.5/4, width=1/10, height=1/4)
    dm.group(ctx, nnlo.cmds_nnlo_four_jets_quarks_2, x=9/10, y=2.5/4, width=1/10, height=1/4)


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

    dm.draw_formula(ctx, r"e^-", 0.15, 0.425)
    dm.draw_formula(ctx, r"e^+", 0.85, 0.425)

    dm.draw_formula(ctx, r"f", 0.68, 0.15)
    dm.draw_formula(ctx, r"\bar{f}", 0.32, 0.85)

    # Arc for the angle

    ctx.path_init(stroke_width=ctx.line_width, fill_opacity=0, stroke_color_rgb=ctx.line_color)
    ctx.path_move_to(0.65 * ctx.scaling_x, 0.5 * ctx.scaling_y)
    ctx.path_rel_quadratic_bezier(0.0 * ctx.scaling_x, -0.07 * ctx.scaling_y,
                                  -0.045 * ctx.scaling_x, -0.14 * ctx.scaling_y)

    ctx.path_finish()


if __name__ == "__main__":
    main()
