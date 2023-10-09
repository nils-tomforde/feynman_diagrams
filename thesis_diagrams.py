
import diagram_maker as dm
import svg_high_level


# TODO: Look where to set fontsize and linewidth also inside of the groups!!!

def main():

    # dm.draw_diagram(width=256, height=512, commands=lambda ctx: cmds_standard_process(ctx, "quarks"), file_path=".\\output\\thesis\\diagrams\\diagram_base_process_quarks.svg")
    # dm.draw_diagram(width=256, height=512, commands=lambda ctx: cmds_standard_process(ctx, "muons"), file_path=".\\output\\thesis\\diagrams\\diagram_base_process_muons.svg")
    # dm.draw_diagram(width=256, height=512, commands=lambda ctx: cmds_standard_process(ctx, "fermions", False), file_path=".\\output\\thesis\\diagrams\\diagram_tree_level_fermions.svg")
    dm.draw_diagram(width=256, height=512, commands=lambda ctx: cmds_standard_process(ctx, "fermions", True), file_path=".\\output\\thesis\\diagrams\\diagram_tree_level_fermions_momenta.svg")

    # dm.draw_diagram(width=256, height=512, commands=lambda ctx: cmds_virtual_gluon_process(ctx, False), file_path=".\\output\\thesis\\diagrams\\diagram_virtual.svg")
    dm.draw_diagram(width=256, height=512, commands=lambda ctx: cmds_virtual_gluon_process(ctx, True), file_path=".\\output\\thesis\\diagrams\\diagram_virtual_momenta.svg")
    dm.draw_diagram(width=768, height=512, commands=cmds_virtual_gluon_process_and_scaleless, file_path=".\\output\\thesis\\diagrams\\diagrams_virtual_momenta_and_scaleless.svg")

    # dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_real_gluon_emission_both(ctx, False), file_path=".\\output\\thesis\\diagrams\\diagrams_emission.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_real_gluon_emission_both(ctx, True), file_path=".\\output\\thesis\\diagrams\\diagrams_emission_momenta.svg")

    dm.draw_diagram(height=512, width=1024, commands=cmds_tree_level_collage, file_path=".\\output\\thesis\\diagrams\\diagrams_tree_level_collage.svg")

    # dm.draw_diagram(height=512, width=512, commands=cmds_initial_state_radiation, file_path=".\\output\\thesis\\diagrams\\diagram_initial_state_radiation.svg")

    # dm.draw_diagram(width=256, height=512, commands=cmds_vacuum_polarization, file_path=".\\output\\thesis\\diagrams\\diagram_vacuum_polarization.svg")

    dm.draw_diagram(width=768, height=512, commands=cmds_isr_and_vacuum_polarization, file_path=".\\output\\thesis\\diagrams\\diagrams_isr_and_vacuum_polarization.svg")

    dm.draw_diagram(width=768, height=512, commands=cmds_nlo_qed, file_path=".\\output\\thesis\\diagrams\\diagrams_nlo_qed.svg")
    dm.draw_diagram(width=768, height=512, commands=cmds_nlo_qcd, file_path=".\\output\\thesis\\diagrams\\diagrams_nlo_qcd.svg")


def cmds_standard_process(ctx: svg_high_level.Context, output_particles: str, show_momenta: bool = False):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.5, 0.7)
    vx_2 = dm.Vertex(ctx, 0.5, 0.3)

    out_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_1, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, vx_2, out_1)
    dm.fermion_line(ctx, vx_2, out_2, is_anti_particle=True)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.5)

    if output_particles == "quarks":
        dm.draw_formula(ctx, r"q", 0.1, 0.05)
        dm.draw_formula(ctx, r"\bar{q}", 0.9, 0.05)
    elif output_particles == "muons":
        dm.draw_formula(ctx, r"\mu^-", 0.1, 0.05)
        dm.draw_formula(ctx, r"\mu^+", 0.9, 0.05)
    elif output_particles == "fermions":
        dm.draw_formula(ctx, r"f", 0.1, 0.05)
        dm.draw_formula(ctx, r"\bar{f}", 0.9, 0.05)

    if show_momenta:
        dm.draw_arrow(ctx, dm.Point(ctx, 0.85, 0.82), dm.Point(ctx, 0.65, 0.72))
        dm.draw_arrow(ctx, dm.Point(ctx, 0.15, 0.82), dm.Point(ctx, 0.35, 0.72))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.4, 0.6), dm.Point(ctx, 0.4, 0.4))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.65, 0.28), dm.Point(ctx, 0.85, 0.18))
        dm.draw_arrow(ctx, dm.Point(ctx, 0.35, 0.28), dm.Point(ctx, 0.15, 0.18))


        dm.draw_formula(ctx, r"p_1", 0.2, 0.75)
        dm.draw_formula(ctx, r"p_2", 0.8, 0.75)
        dm.draw_formula(ctx, r"p_1 + p_2", 0.25, 0.5)
        dm.draw_formula(ctx, r"k_1", 0.2, 0.25)
        dm.draw_formula(ctx, r"k_2", 0.8, 0.25)


def cmds_virtual_gluon_process(ctx: svg_high_level.Context, show_momenta: bool = False):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.5, 0.7)
    vx_2 = dm.Vertex(ctx, 0.5, 0.4)

    vx_3 = dm.Vertex(ctx, 0.3, 0.25)
    vx_4 = dm.Vertex(ctx, 0.7, 0.25)

    out_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_1, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, vx_2, vx_3)
    dm.fermion_line(ctx, vx_2, vx_4, is_anti_particle=True)

    dm.vertex(ctx, vx_3)

    dm.gluon_line(ctx, vx_4, vx_3, center=False)

    dm.vertex(ctx, vx_4)

    dm.fermion_line(ctx, vx_3, out_1)
    dm.fermion_line(ctx, vx_4, out_2, is_anti_particle=True)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.55)

    dm.draw_formula(ctx, r"q", 0.1, 0.05)
    dm.draw_formula(ctx, r"\bar{q}", 0.9, 0.05)

    dm.draw_formula(ctx, r"g", 0.5, 0.28)

    if show_momenta:
        dm.draw_arrow(ctx, dm.Point(ctx, 0.85, 0.82), dm.Point(ctx, 0.65, 0.72))
        dm.draw_arrow(ctx, dm.Point(ctx, 0.15, 0.82), dm.Point(ctx, 0.35, 0.72))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.4, 0.65), dm.Point(ctx, 0.4, 0.45))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.6, 0.4), dm.Point(ctx, 0.6 + 0.4 / 3, 0.3))
        dm.draw_arrow(ctx, dm.Point(ctx, 0.4, 0.4), dm.Point(ctx, 0.4 - 0.4 / 3, 0.3))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.8, 0.25), dm.Point(ctx, 0.8 + 0.4 / 3, 0.15))
        dm.draw_arrow(ctx, dm.Point(ctx, 0.2, 0.25), dm.Point(ctx, 0.2 - 0.4 / 3, 0.15))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.65, 0.2), dm.Point(ctx, 0.35, 0.2))

        dm.draw_formula(ctx, r"p_1", 0.2, 0.72)
        dm.draw_formula(ctx, r"p_2", 0.8, 0.72)
        dm.draw_formula(ctx, r"p_1 + p_2", 0.25, 0.55)
        dm.draw_formula(ctx, r"k", 0.5, 0.17)
        dm.draw_formula(ctx, r"k_1 - k", 0.2, 0.37)
        dm.draw_formula(ctx, r"k_2 + k", 0.8, 0.37)
        dm.draw_formula(ctx, r"k_1", 0.1, 0.225)
        dm.draw_formula(ctx, r"k_2", 0.9, 0.225)


def cmds_virtual_gluon_process_scaleless_1(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.5, 0.7)
    vx_2 = dm.Vertex(ctx, 0.5, 0.4)

    vx_l1 = dm.Vertex(ctx, 0.5 - 0.1, 0.4 - 0.1 * 3/4)
    vx_l2 = dm.Vertex(ctx, 0.5 - 0.3, 0.4 - 0.3 * 3/4)

    out_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_1, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, vx_2, vx_l1)
    dm.fermion_line(ctx, vx_l1, vx_l2)
    dm.fermion_line(ctx, vx_l2, out_1)

    dm.fermion_line(ctx, vx_2, out_2, is_anti_particle=True)

    dm.vertex(ctx, vx_l1)
    dm.vertex(ctx, vx_l2)

    dm.gluon_line_curved(ctx, vx_l1, vx_l2, center=False)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.55)

    dm.draw_formula(ctx, r"q", 0.1, 0.05)
    dm.draw_formula(ctx, r"\bar{q}", 0.9, 0.05)

    dm.draw_formula(ctx, r"g", 0.1, 0.3)


def cmds_virtual_gluon_process_scaleless_2(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.5, 0.7)
    vx_2 = dm.Vertex(ctx, 0.5, 0.4)

    vx_r1 = dm.Vertex(ctx, 0.5 + 0.1, 0.4 - 0.1 * 3/4)
    vx_r2 = dm.Vertex(ctx, 0.5 + 0.3, 0.4 - 0.3 * 3/4)

    out_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_1, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, vx_2, out_1)

    dm.fermion_line(ctx, vx_2, vx_r1, is_anti_particle=True)
    dm.fermion_line(ctx, vx_r1, vx_r2, is_anti_particle=True)
    dm.fermion_line(ctx, vx_r2, out_2, is_anti_particle=True)

    dm.vertex(ctx, vx_r1)
    dm.vertex(ctx, vx_r2)

    dm.gluon_line_curved(ctx, vx_r2, vx_r1, center=False)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.55)

    dm.draw_formula(ctx, r"q", 0.1, 0.05)
    dm.draw_formula(ctx, r"\bar{q}", 0.9, 0.05)

    dm.draw_formula(ctx, r"g", 0.9, 0.3)


def cmds_virtual_gluon_process_and_scaleless(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, lambda ctx_: cmds_virtual_gluon_process(ctx_, show_momenta=True), x=0, y=0, width=1/3, height=1)
    dm.group(ctx, cmds_virtual_gluon_process_scaleless_1, x=1/3, y=0, width=1/3, height=1)
    dm.group(ctx, cmds_virtual_gluon_process_scaleless_2, x=2/3, y=0, width=1/3, height=1)

    # Labels
    dm.draw_circle(ctx, dm.Point(ctx, 1/6, 0.9), 20, fill_opacity=0)
    dm.draw_circle(ctx, dm.Point(ctx, 3/6, 0.9), 20, fill_opacity=0)
    dm.draw_circle(ctx, dm.Point(ctx, 5/6, 0.9), 20, fill_opacity=0)

    dm.draw_formula(ctx, "\mathrm{A}", 1/6, 0.9, fontsize=25)
    dm.draw_formula(ctx, "\mathrm{B}", 3/6, 0.9, fontsize=25)
    dm.draw_formula(ctx, "\mathrm{C}", 5/6, 0.9, fontsize=25)


def cmds_real_gluon_emission_process_1(ctx: svg_high_level.Context, show_momenta: bool = False):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.5, 0.7)
    vx_2 = dm.Vertex(ctx, 0.5, 0.4)
    vx_3 = dm.Vertex(ctx, 0.3, 0.25)

    out_1 = dm.Vertex(ctx, 0.1, 0.1)
    out_2 = dm.Vertex(ctx, 0.9, 0.1)
    out_3 = dm.Vertex(ctx, 0.5, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_1, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, vx_2, vx_3)
    dm.fermion_line(ctx, vx_2, out_2, is_anti_particle=True)

    dm.vertex(ctx, vx_3)

    dm.gluon_line(ctx, vx_3, out_3, center=False)

    dm.fermion_line(ctx, vx_3, out_1)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.55)

    dm.draw_formula(ctx, r"q", 0.1, 0.05)
    dm.draw_formula(ctx, r"\bar{q}", 0.9, 0.05)

    dm.draw_formula(ctx, r"g", 0.5, 0.05)

    if show_momenta:
        dm.draw_arrow(ctx, dm.Point(ctx, 0.85, 0.82), dm.Point(ctx, 0.65, 0.72))
        dm.draw_arrow(ctx, dm.Point(ctx, 0.15, 0.82), dm.Point(ctx, 0.35, 0.72))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.4, 0.65), dm.Point(ctx, 0.4, 0.45))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.6 + 0.4 / 3, 0.3), dm.Point(ctx, 0.6 + 2 * 0.4 / 3, 0.2))
        dm.draw_arrow(ctx, dm.Point(ctx, 0.4, 0.4), dm.Point(ctx, 0.4 - 0.4 / 3, 0.3))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.2, 0.25), dm.Point(ctx, 0.2 - 0.4 / 3, 0.15))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.45, 0.25), dm.Point(ctx, 0.45 + 0.4 / 3, 0.15))


        dm.draw_formula(ctx, r"p_1", 0.2, 0.72)
        dm.draw_formula(ctx, r"p_2", 0.8, 0.72)
        dm.draw_formula(ctx, r"p_1 + p_2", 0.25, 0.55)
        dm.draw_formula(ctx, r"k_3", 0.58, 0.22)
        dm.draw_formula(ctx, r"k_1 + k_3", 0.2, 0.37)
        dm.draw_formula(ctx, r"k_2", 0.85, 0.27)
        dm.draw_formula(ctx, r"k_1", 0.1, 0.225)


def cmds_real_gluon_emission_process_2(ctx: svg_high_level.Context, show_momenta: bool = False):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.ExtPoint(ctx, 0.5, 0.7)
    vx_2 = dm.ExtPoint(ctx, 0.5, 0.4)
    vx_3 = dm.ExtPoint(ctx, 0.7, 0.25)

    out_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.1)
    out_3 = dm.ExtPoint(ctx, 0.5, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_1, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, vx_2, out_1)
    dm.fermion_line(ctx, vx_2, vx_3, is_anti_particle=True)

    dm.vertex(ctx, vx_3)

    dm.gluon_line(ctx, out_3, vx_3, center=False)

    dm.fermion_line(ctx, vx_3, out_2, is_anti_particle=True)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.55)

    dm.draw_formula(ctx, r"q", 0.1, 0.05)
    dm.draw_formula(ctx, r"\bar{q}", 0.9, 0.05)

    dm.draw_formula(ctx, r"g", 0.5, 0.05)

    if show_momenta:
        dm.draw_arrow(ctx, dm.Point(ctx, 0.85, 0.82), dm.Point(ctx, 0.65, 0.72))
        dm.draw_arrow(ctx, dm.Point(ctx, 0.15, 0.82), dm.Point(ctx, 0.35, 0.72))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.4, 0.65), dm.Point(ctx, 0.4, 0.45))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.6, 0.4), dm.Point(ctx, 0.6 + 0.4 / 3, 0.3))
        dm.draw_arrow(ctx, dm.Point(ctx, 0.4 - 0.4 / 3, 0.3), dm.Point(ctx, 0.4 - 2 * 0.4 / 3, 0.2))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.8, 0.25), dm.Point(ctx, 0.8 + 0.4 / 3, 0.15))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.55, 0.25), dm.Point(ctx, 0.55 - 0.4 / 3, 0.15))

        dm.draw_formula(ctx, r"p_1", 0.2, 0.72)
        dm.draw_formula(ctx, r"p_2", 0.8, 0.72)
        dm.draw_formula(ctx, r"p_1 + p_2", 0.25, 0.55)
        dm.draw_formula(ctx, r"k_3", 0.42, 0.22)
        dm.draw_formula(ctx, r"k_1", 0.15, 0.27)
        dm.draw_formula(ctx, r"k_2 + k_3", 0.8, 0.37)
        dm.draw_formula(ctx, r"k_2", 0.9, 0.225)


def cmds_real_gluon_emission_both(ctx: svg_high_level.Context, show_momenta: bool = False):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, lambda ctx_: cmds_real_gluon_emission_process_1(ctx_, show_momenta=show_momenta), x=0, y=0, width=0.5, height=1)
    dm.group(ctx, lambda ctx_: cmds_real_gluon_emission_process_2(ctx_, show_momenta=show_momenta), x=0.5, y=0, width=0.5, height=1)

    # Labels
    dm.draw_circle(ctx, dm.Point(ctx, 0.25, 0.9), 20, fill_opacity=0)
    dm.draw_circle(ctx, dm.Point(ctx, 0.75, 0.9), 20, fill_opacity=0)

    dm.draw_formula(ctx, "\mathrm{A}", 0.25, 0.9, fontsize=25)
    dm.draw_formula(ctx, "\mathrm{B}", 0.75, 0.9, fontsize=25)


def cmds_initial_state_radiation_1(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.5, 0.6)
    vx_2 = dm.Vertex(ctx, 0.5, 0.3)
    vx_3 = dm.Vertex(ctx, 0.3, 0.75)

    out_1 = dm.Vertex(ctx, 0.1, 0.1)
    out_2 = dm.Vertex(ctx, 0.9, 0.1)
    out_3 = dm.Vertex(ctx, 0.1, 0.5)

    dm.fermion_line(ctx, in_1, vx_3)
    dm.fermion_line(ctx, vx_3, vx_1)
    dm.boson_line(ctx, vx_3, out_3)

    dm.fermion_line(ctx, in_2, vx_1, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, vx_2, out_1)
    dm.fermion_line(ctx, vx_2, out_2, is_anti_particle=True)

    dm.vertex(ctx, vx_3)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.45)

    dm.draw_formula(ctx, r"f", 0.1, 0.05)
    dm.draw_formula(ctx, r"\bar{f}", 0.9, 0.05)

    dm.draw_formula(ctx, r"\gamma", 0.1, 0.45)


def cmds_initial_state_radiation_2(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.ExtPoint(ctx, 0.5, 0.6)
    vx_2 = dm.ExtPoint(ctx, 0.5, 0.3)
    vx_3 = dm.ExtPoint(ctx, 0.7, 0.75)

    out_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.1)
    out_3 = dm.ExtPoint(ctx, 0.9, 0.5)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_3, is_anti_particle=True)
    dm.fermion_line(ctx, vx_3, vx_1, is_anti_particle=True)
    dm.boson_line(ctx, out_3, vx_3, start_with_dale=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, vx_2, out_1)
    dm.fermion_line(ctx, vx_2, out_2, is_anti_particle=True)

    dm.vertex(ctx, vx_3)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.45)

    dm.draw_formula(ctx, r"f", 0.1, 0.05)
    dm.draw_formula(ctx, r"\bar{f}", 0.9, 0.05)

    dm.draw_formula(ctx, r"\gamma", 0.9, 0.45)


def cmds_initial_state_radiation(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_initial_state_radiation_1, x=0, y=0, width=0.5, height=1)
    dm.group(ctx, cmds_initial_state_radiation_2, x=0.5, y=0, width=0.5, height=1)

    # Labels
    dm.draw_circle(ctx, dm.Point(ctx, 0.25, 0.9), 20, fill_opacity=0)
    dm.draw_circle(ctx, dm.Point(ctx, 0.75, 0.9), 20, fill_opacity=0)

    dm.draw_formula(ctx, "\mathrm{A}", 0.25, 0.9, fontsize=25)
    dm.draw_formula(ctx, "\mathrm{B}", 0.75, 0.9, fontsize=25)


def cmds_isr_and_vacuum_polarization(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_initial_state_radiation_1, x=0/3, y=0, width=1/3, height=1)
    dm.group(ctx, cmds_initial_state_radiation_2, x=1/3, y=0, width=1/3, height=1)
    dm.group(ctx, cmds_vacuum_polarization, x=2/3, y=0, width=1/3, height=1)

    dm.draw_circle(ctx, dm.Point(ctx, 1/6, 0.95), 20, fill_opacity=0)
    dm.draw_circle(ctx, dm.Point(ctx, 3/6, 0.95), 20, fill_opacity=0)
    dm.draw_circle(ctx, dm.Point(ctx, 5/6, 0.95), 20, fill_opacity=0)

    dm.draw_formula(ctx, "\mathrm{A}", 1/6, 0.95, fontsize=25)
    dm.draw_formula(ctx, "\mathrm{B}", 3/6, 0.95, fontsize=25)
    dm.draw_formula(ctx, "\mathrm{C}", 5/6, 0.95, fontsize=25)


def cmds_tree_level_collage(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_introduction_t_channel_bhabha, x=0, y=0, width=0.5, height=0.5)
    dm.group(ctx, cmds_introduction_photon_creation, x=0, y=1/2, width=0.5, height=0.5)
    dm.group(ctx, cmds_introduction_charged_fermions, x=2/4, y=0, width=0.25, height=1)
    dm.group(ctx, cmds_introduction_w_production, x=3/4, y=0, width=0.25, height=1)

    dm.draw_arrow(ctx, dm.Point(ctx, 0.5, 0.7), dm.Point(ctx, 0.5, 0.3))
    dm.draw_formula(ctx, r"t", x=0.5, y=0.25)

    dm.draw_circle(ctx, dm.Point(ctx, 0.25, 0.45), 20, fill_opacity=0)
    dm.draw_circle(ctx, dm.Point(ctx, 0.25, 0.95), 20, fill_opacity=0)
    dm.draw_circle(ctx, dm.Point(ctx, 0.625, 0.95), 20, fill_opacity=0)
    dm.draw_circle(ctx, dm.Point(ctx, 0.875, 0.95), 20, fill_opacity=0)

    dm.draw_formula(ctx, "\mathrm{A}", 0.25, 0.45, fontsize=25)
    dm.draw_formula(ctx, "\mathrm{B}", 0.25, 0.95, fontsize=25)
    dm.draw_formula(ctx, "\mathrm{C}", 0.625, 0.95, fontsize=25)
    dm.draw_formula(ctx, "\mathrm{D}", 0.875, 0.95, fontsize=25)


def cmds_introduction_t_channel_bhabha(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.3, 0.5)
    vx_2 = dm.Vertex(ctx, 0.7, 0.5)

    out_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_2, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, vx_1, out_1)
    dm.fermion_line(ctx, vx_2, out_2, is_anti_particle=True)

    dm.draw_formula(ctx, r"e^-", 0.05, 0.9)
    dm.draw_formula(ctx, r"e^+", 0.95, 0.9)

    dm.draw_formula(ctx, r"\gamma", 0.5, 0.4)

    dm.draw_formula(ctx, r"e^-", 0.05, 0.1)
    dm.draw_formula(ctx, r"e^+", 0.95, 0.1)


def cmds_introduction_photon_creation(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.3, 0.5)
    vx_2 = dm.Vertex(ctx, 0.7, 0.5)

    out_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_2, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.fermion_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.boson_line(ctx, vx_1, out_1)
    dm.boson_line(ctx, vx_2, out_2)

    dm.draw_formula(ctx, r"e^-", 0.05, 0.9)
    dm.draw_formula(ctx, r"e^+", 0.95, 0.9)

    dm.draw_formula(ctx, r"e", 0.5, 0.4)

    dm.draw_formula(ctx, r"\gamma", 0.05, 0.1)
    dm.draw_formula(ctx, r"\gamma", 0.95, 0.1)


def cmds_introduction_charged_fermions(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.5, 0.7)
    vx_2 = dm.Vertex(ctx, 0.5, 0.3)

    out_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_1, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, vx_2, out_1)
    dm.fermion_line(ctx, vx_2, out_2, is_anti_particle=True)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.5)

    dm.draw_formula(ctx, r"f", 0.1, 0.05)
    dm.draw_formula(ctx, r"\bar{f}", 0.9, 0.05)


def cmds_introduction_w_production(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.5, 0.7)
    vx_2 = dm.Vertex(ctx, 0.5, 0.3)

    out_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_1, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.boson_line(ctx, vx_2, out_1)
    dm.boson_line(ctx, vx_2, out_2)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.5)

    dm.draw_formula(ctx, r"W^+", 0.1, 0.05)
    dm.draw_formula(ctx, r"W^-", 0.9, 0.05)


def cmds_introduction_higgs(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    pass


def cmds_vacuum_polarization(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.5, 0.8)
    vx_2 = dm.Vertex(ctx, 0.5, 0.6)
    vx_3 = dm.Vertex(ctx, 0.5, 0.4)
    vx_4 = dm.Vertex(ctx, 0.5, 0.2)

    out_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_1, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.fermion_line_curved(ctx, vx_2, vx_3, curvature="right")
    dm.fermion_line_curved(ctx, vx_2, vx_3, curvature="left", is_anti_particle=True)

    dm.vertex(ctx, vx_2)
    dm.vertex(ctx, vx_3)

    dm.boson_line(ctx, vx_3, vx_4)

    dm.vertex(ctx, vx_4)

    dm.fermion_line(ctx, vx_4, out_1)
    dm.fermion_line(ctx, vx_4, out_2, is_anti_particle=True)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.3)
    dm.draw_formula(ctx, r"\gamma", 0.6, 0.7)

    dm.draw_formula(ctx, r"f", 0.1, 0.05)
    dm.draw_formula(ctx, r"\bar{f}", 0.9, 0.05)


def cmds_virtual_photon_process(ctx: svg_high_level.Context, show_momenta: bool = False):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.5, 0.7)
    vx_2 = dm.Vertex(ctx, 0.5, 0.4)

    vx_3 = dm.Vertex(ctx, 0.3, 0.25)
    vx_4 = dm.Vertex(ctx, 0.7, 0.25)

    out_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_1, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, vx_2, vx_3)
    dm.fermion_line(ctx, vx_2, vx_4, is_anti_particle=True)

    dm.vertex(ctx, vx_3)

    dm.boson_line(ctx, vx_4, vx_3)

    dm.vertex(ctx, vx_4)

    dm.fermion_line(ctx, vx_3, out_1)
    dm.fermion_line(ctx, vx_4, out_2, is_anti_particle=True)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.55)

    dm.draw_formula(ctx, r"q", 0.1, 0.05)
    dm.draw_formula(ctx, r"\bar{q}", 0.9, 0.05)

    dm.draw_formula(ctx, r"\gamma", 0.5, 0.28)

    if show_momenta:
        dm.draw_arrow(ctx, dm.Point(ctx, 0.85, 0.8), dm.Point(ctx, 0.65, 0.7))
        dm.draw_arrow(ctx, dm.Point(ctx, 0.15, 0.8), dm.Point(ctx, 0.35, 0.7))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.4, 0.65), dm.Point(ctx, 0.4, 0.45))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.65, 0.4), dm.Point(ctx, 0.65 + 0.4 / 3, 0.3))
        dm.draw_arrow(ctx, dm.Point(ctx, 0.35, 0.4), dm.Point(ctx, 0.35 - 0.4 / 3, 0.3))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.85, 0.25), dm.Point(ctx, 0.85 + 0.4 / 3, 0.15))
        dm.draw_arrow(ctx, dm.Point(ctx, 0.15, 0.25), dm.Point(ctx, 0.15 - 0.4 / 3, 0.15))

        dm.draw_arrow(ctx, dm.Point(ctx, 0.65, 0.18), dm.Point(ctx, 0.35, 0.18))

        dm.draw_formula(ctx, r"p_1", 0.2, 0.7)
        dm.draw_formula(ctx, r"p_2", 0.8, 0.7)
        dm.draw_formula(ctx, r"p_1 + p_2", 0.25, 0.55)
        dm.draw_formula(ctx, r"k", 0.5, 0.15)
        dm.draw_formula(ctx, r"k_1 - k", 0.15, 0.37)
        dm.draw_formula(ctx, r"k_2 + k", 0.85, 0.37)
        dm.draw_formula(ctx, r"k_1", 0.05, 0.225)
        dm.draw_formula(ctx, r"k_2", 0.95, 0.225)


def cmds_real_photon_emission_process_1(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.Vertex(ctx, 0.5, 0.7)
    vx_2 = dm.Vertex(ctx, 0.5, 0.4)
    vx_3 = dm.Vertex(ctx, 0.3, 0.25)

    out_1 = dm.Vertex(ctx, 0.1, 0.1)
    out_2 = dm.Vertex(ctx, 0.9, 0.1)
    out_3 = dm.Vertex(ctx, 0.5, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_1, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, vx_2, vx_3)
    dm.fermion_line(ctx, vx_2, out_2, is_anti_particle=True)

    dm.vertex(ctx, vx_3)

    dm.boson_line(ctx, vx_3, out_3, start_with_dale=True)

    dm.fermion_line(ctx, vx_3, out_1)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.55)

    dm.draw_formula(ctx, r"q", 0.1, 0.05)
    dm.draw_formula(ctx, r"\bar{q}", 0.9, 0.05)

    dm.draw_formula(ctx, r"\gamma", 0.5, 0.05)


def cmds_real_photon_emission_process_2(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    dm.set_background(ctx, 255, 255, 255, 1)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.9)
    in_2 = dm.ExtPoint(ctx, 0.9, 0.9)

    vx_1 = dm.ExtPoint(ctx, 0.5, 0.7)
    vx_2 = dm.ExtPoint(ctx, 0.5, 0.4)
    vx_3 = dm.ExtPoint(ctx, 0.7, 0.25)

    out_1 = dm.ExtPoint(ctx, 0.1, 0.1)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.1)
    out_3 = dm.ExtPoint(ctx, 0.5, 0.1)

    dm.fermion_line(ctx, in_1, vx_1)
    dm.fermion_line(ctx, in_2, vx_1, is_anti_particle=True)

    dm.vertex(ctx, vx_1)

    dm.boson_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_2)

    dm.fermion_line(ctx, vx_2, out_1)
    dm.fermion_line(ctx, vx_2, vx_3, is_anti_particle=True)

    dm.vertex(ctx, vx_3)

    dm.boson_line(ctx, out_3, vx_3)

    dm.fermion_line(ctx, vx_3, out_2, is_anti_particle=True)

    dm.draw_formula(ctx, r"e^-", 0.1, 0.95)
    dm.draw_formula(ctx, r"e^+", 0.9, 0.95)

    dm.draw_formula(ctx, r"\gamma", 0.6, 0.55)

    dm.draw_formula(ctx, r"q", 0.1, 0.05)
    dm.draw_formula(ctx, r"\bar{q}", 0.9, 0.05)

    dm.draw_formula(ctx, r"\gamma", 0.5, 0.05)


def cmds_nlo_qed(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_virtual_photon_process, x=0, y=0, width=1/3, height=1)
    dm.group(ctx, cmds_real_photon_emission_process_1, x=1/3, y=0, width=1/3, height=1)
    dm.group(ctx, cmds_real_photon_emission_process_2, x=2/3, y=0, width=1/3, height=1)

    # Labels
    dm.draw_circle(ctx, dm.Point(ctx, 1/6, 0.9), 20, fill_opacity=0)
    dm.draw_circle(ctx, dm.Point(ctx, 3/6, 0.9), 20, fill_opacity=0)
    dm.draw_circle(ctx, dm.Point(ctx, 5/6, 0.9), 20, fill_opacity=0)

    dm.draw_formula(ctx, "\mathrm{A}", 1/6, 0.9, fontsize=25)
    dm.draw_formula(ctx, "\mathrm{B}", 3/6, 0.9, fontsize=25)
    dm.draw_formula(ctx, "\mathrm{C}", 5/6, 0.9, fontsize=25)


def cmds_nlo_qcd(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_virtual_gluon_process, x=0, y=0, width=1/3, height=1)
    dm.group(ctx, cmds_real_gluon_emission_process_1, x=1/3, y=0, width=1/3, height=1)
    dm.group(ctx, cmds_real_gluon_emission_process_2, x=2/3, y=0, width=1/3, height=1)

    # Labels
    dm.draw_circle(ctx, dm.Point(ctx, 1/6, 0.9), 20, fill_opacity=0)
    dm.draw_circle(ctx, dm.Point(ctx, 3/6, 0.9), 20, fill_opacity=0)
    dm.draw_circle(ctx, dm.Point(ctx, 5/6, 0.9), 20, fill_opacity=0)

    dm.draw_formula(ctx, "\mathrm{A}", 1/6, 0.9, fontsize=25)
    dm.draw_formula(ctx, "\mathrm{B}", 3/6, 0.9, fontsize=25)
    dm.draw_formula(ctx, "\mathrm{C}", 5/6, 0.9, fontsize=25)


if __name__ == "__main__":
    main()
