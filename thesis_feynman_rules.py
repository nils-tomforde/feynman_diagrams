
import diagram_maker as dm
import svg_high_level

FORMULA_FONTSIZE = 25


def main():
    # Propagators
    dm.draw_diagram(width=512, height=512, commands=cmds_fm_rules_propagators, file_path=".\\output\\thesis\\feynman_rules\\feynman_rules_propagators.svg")

    # Vertices
    dm.draw_diagram(width=512, height=512, commands=cmds_fm_rules_vertices, file_path=".\\output\\thesis\\feynman_rules\\feynman_rules_vertices.svg")

    # External particles
    dm.draw_diagram(width=512, height=512, commands=cmds_fm_rules_external_particles, file_path=".\\output\\thesis\\feynman_rules\\feynman_rules_external_particles.svg")

# Propagators


def cmds_fm_rules_propagators(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_fm_rules_fermion_propagator, x=0, y=0, width=2/3, height=1/4)
    dm.group(ctx, cmds_fm_rules_fermion_propagator_description, x=2/3, y=0, width=1/3, height=1/4)
    dm.draw_text(ctx, text="Fermion:", x=0.05, y=0.05, fontsize=12)

    dm.group(ctx, cmds_fm_rules_photon_propagator, x=0, y=1/4, width=2/3, height=1/4)
    dm.group(ctx, cmds_fm_rules_photon_propagator_description, x=2/3, y=1/4, width=1/3, height=1/4)
    dm.draw_text(ctx, text="Photon:", x=0.05, y=0.05 + 1/4, fontsize=12)

    dm.group(ctx, cmds_fm_rules_gluon_propagator, x=0, y=2/4, width=2/3, height=1/4)
    dm.group(ctx, cmds_fm_rules_gluon_propagator_description, x=2/3, y=2/4, width=1/3, height=1/4)
    dm.draw_text(ctx, text="Gluon:", x=0.05, y=0.05 + 2/4, fontsize=12)

    dm.group(ctx, cmds_fm_rules_z_propagator, x=0, y=3/4, width=2/3, height=1/4)
    dm.group(ctx, cmds_fm_rules_z_propagator_description, x=2/3, y=3/4, width=1/3, height=1/4)
    dm.draw_text(ctx, text="Z boson:", x=0.05, y=0.05 + 3/4, fontsize=12)


def cmds_fm_rules_fermion_propagator(ctx: svg_high_level.Context):
    ctx.set_fontsize(15)
    ctx.set_line_width(2)

    vx_1 = dm.Vertex(ctx, 0.1, 0.5)
    vx_2 = dm.Vertex(ctx, 0.9, 0.5)

    dm.fermion_line(ctx, vx_1, vx_2)

    dm.vertex(ctx, vx_1)
    dm.vertex(ctx, vx_2)

    dm.draw_formula(ctx, r"f", 0.5, 0.25)

    dm.draw_arrow(ctx, dm.Point(ctx, 0.4, 0.7), dm.Point(ctx, 0.6, 0.7))
    dm.draw_formula(ctx, r"q", 0.5, 0.8)


def cmds_fm_rules_fermion_propagator_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"= \frac{i \left( q \not + m_f \right)}{q^2 - m_f^2 + i 0}", x=0.1, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


def cmds_fm_rules_photon_propagator(ctx: svg_high_level.Context):
    ctx.set_fontsize(15)
    ctx.set_line_width(2)

    vx_1 = dm.Vertex(ctx, 0.1, 0.5)
    vx_2 = dm.Vertex(ctx, 0.9, 0.5)

    dm.boson_line(ctx, vx_1, vx_2, number_of_waves=8)

    dm.vertex(ctx, vx_1)
    dm.vertex(ctx, vx_2)

    dm.draw_formula(ctx, r"\gamma", 0.5, 0.25)

    dm.draw_arrow(ctx, dm.Point(ctx, 0.4, 0.7), dm.Point(ctx, 0.6, 0.7))
    dm.draw_formula(ctx, r"q", 0.5, 0.8)

    dm.draw_formula(ctx, r"\mu", 0.05, 0.5)
    dm.draw_formula(ctx, r"\nu", 0.95, 0.5)


def cmds_fm_rules_photon_propagator_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"= \frac{- i g_{\mu \nu}}{q^2 + i 0}", x=0.1, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


def cmds_fm_rules_gluon_propagator(ctx: svg_high_level.Context):
    ctx.set_fontsize(15)
    ctx.set_line_width(2)

    vx_1 = dm.Vertex(ctx, 0.1, 0.5)
    vx_2 = dm.Vertex(ctx, 0.9, 0.5)

    dm.gluon_line(ctx, vx_2, vx_1, number_of_loops=14, center=False)

    dm.vertex(ctx, vx_1)
    dm.vertex(ctx, vx_2)

    dm.draw_formula(ctx, r"g", 0.5, 0.25)

    dm.draw_arrow(ctx, dm.Point(ctx, 0.4, 0.7), dm.Point(ctx, 0.6, 0.7))
    dm.draw_formula(ctx, r"q", 0.5, 0.8)

    dm.draw_formula(ctx, r"\mu,a", 0.05, 0.5)
    dm.draw_formula(ctx, r"\nu,b", 0.95, 0.5)


def cmds_fm_rules_gluon_propagator_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"= \frac{- i g_{\mu \nu} \delta^{a b}}{q^2 + i 0}", x=0.1, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


def cmds_fm_rules_z_propagator(ctx: svg_high_level.Context):
    ctx.set_fontsize(15)
    ctx.set_line_width(2)

    vx_1 = dm.Vertex(ctx, 0.1, 0.5)
    vx_2 = dm.Vertex(ctx, 0.9, 0.5)

    dm.boson_line(ctx, vx_1, vx_2, number_of_waves=8)

    dm.vertex(ctx, vx_1)
    dm.vertex(ctx, vx_2)

    dm.draw_formula(ctx, r"Z^0", 0.5, 0.25)

    dm.draw_arrow(ctx, dm.Point(ctx, 0.4, 0.7), dm.Point(ctx, 0.6, 0.7))
    dm.draw_formula(ctx, r"q", 0.5, 0.8)

    dm.draw_formula(ctx, r"\mu", 0.05, 0.5)
    dm.draw_formula(ctx, r"\nu", 0.95, 0.5)


def cmds_fm_rules_z_propagator_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"= \frac{- i \left( g_{\mu \nu} - \frac{q_\mu q_\nu}{m_Z^2} \right)}{q^2 - m_Z^2 + i 0}", x=0.1, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


# Vertices

def cmds_fm_rules_vertices(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.group(ctx, cmds_fm_rules_photon_fermion_fermion_vertex, x=0, y=0, width=1/2, height=1/3)
    dm.group(ctx, cmds_fm_rules_photon_fermion_fermion_vertex_description, x=1/2, y=0, width=1/2, height=1/3)

    dm.group(ctx, cmds_fm_rules_gluon_quark_quark_vertex, x=0, y=1/3, width=1/2, height=1/3)
    dm.group(ctx, cmds_fm_rules_gluon_quark_quark_vertex_description, x=1/2, y=1/3, width=1/2, height=1/3)

    dm.group(ctx, cmds_fm_rules_z_fermion_fermion_vertex, x=0, y=2/3, width=1/2, height=1/3)
    dm.group(ctx, cmds_fm_rules_z_fermion_fermion_vertex_description, x=1/2, y=2/3, width=1/2, height=1/3)


def cmds_fm_rules_photon_fermion_fermion_vertex(ctx: svg_high_level.Context):
    ctx.set_fontsize(15)
    ctx.set_line_width(2)

    vx = dm.Vertex(ctx, 0.5, 0.5)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.5)

    out_1 = dm.ExtPoint(ctx, 0.9, 0.2)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.8)

    dm.fermion_line(ctx, in_1, vx)
    dm.fermion_line(ctx, vx, out_1)
    dm.boson_line(ctx, vx, out_2, start_with_dale=True)

    dm.vertex(ctx, vx)

    dm.draw_formula(ctx, r"f", 0.3, 0.4)
    dm.draw_formula(ctx, r"f", 0.7, 0.2)
    dm.draw_formula(ctx, r"\gamma", 0.7, 0.8)

    dm.draw_formula(ctx, r"\mu", 0.95, 0.8)


def cmds_fm_rules_photon_fermion_fermion_vertex_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"= i Q_f e \gamma^\mu", x=0.05, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


def cmds_fm_rules_gluon_quark_quark_vertex(ctx: svg_high_level.Context):
    ctx.set_fontsize(15)
    ctx.set_line_width(2)

    vx = dm.Vertex(ctx, 0.5, 0.5)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.5)

    out_1 = dm.ExtPoint(ctx, 0.9, 0.2)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.8)

    dm.fermion_line(ctx, in_1, vx)
    dm.fermion_line(ctx, vx, out_1)
    dm.gluon_line(ctx, vx, out_2, center=False)

    dm.vertex(ctx, vx)

    dm.draw_formula(ctx, r"q", 0.3, 0.4)
    dm.draw_formula(ctx, r"q", 0.7, 0.2)
    dm.draw_formula(ctx, r"g", 0.7, 0.8)

    dm.draw_formula(ctx, r"i", 0.95, 0.2)
    dm.draw_formula(ctx, r"j", 0.05, 0.5)
    dm.draw_formula(ctx, r"\mu , a", 0.975, 0.8)


def cmds_fm_rules_gluon_quark_quark_vertex_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"= i g_s \gamma^\mu T_{ij}^a", x=0.05, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


def cmds_fm_rules_z_fermion_fermion_vertex(ctx: svg_high_level.Context):
    ctx.set_fontsize(15)
    ctx.set_line_width(2)

    vx = dm.Vertex(ctx, 0.5, 0.5)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.5)

    out_1 = dm.ExtPoint(ctx, 0.9, 0.2)
    out_2 = dm.ExtPoint(ctx, 0.9, 0.8)

    dm.fermion_line(ctx, in_1, vx)
    dm.fermion_line(ctx, vx, out_1)
    dm.boson_line(ctx, vx, out_2, start_with_dale=True)

    dm.vertex(ctx, vx)

    dm.draw_formula(ctx, r"f", 0.3, 0.4)
    dm.draw_formula(ctx, r"f", 0.7, 0.2)
    dm.draw_formula(ctx, r"Z^0", 0.7, 0.8)

    dm.draw_formula(ctx, r"\mu", 0.95, 0.8)


def cmds_fm_rules_z_fermion_fermion_vertex_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"= - \frac{i g}{2 c_w} \gamma^\mu \left(V_f - A_f \gamma^5 \right)", x=0.05, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


# External particles

def cmds_fm_rules_external_particles(ctx: svg_high_level.Context):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)

    dm.draw_text(ctx, text="Incoming", x=1/4, y=0.05, fontsize=16, center_text=True)
    dm.draw_text(ctx, text="Outgoing", x=3/4, y=0.05, fontsize=16, center_text=True)

    dm.draw_text(ctx, text="Fermions", x=1/2, y=0.13, fontsize=16, center_text=True)

    dm.group(ctx, lambda ctx_: cmds_fm_rules_external_fermion_in(ctx_, is_antiparticle=False), x=0, y=0.1, width=1 / 4, height=1 / 4)
    dm.group(ctx, cmds_fm_rules_external_fermion_in_description, x=1/4, y=0.1, width=1/4, height=1/4)

    dm.group(ctx, lambda ctx_: cmds_fm_rules_external_fermion_out(ctx_, is_antiparticle=False), x=2 / 4, y=0.1, width=1 / 4, height=1 / 4)
    dm.group(ctx, cmds_fm_rules_external_fermion_out_description, x=3/4, y=0.1, width=1/4, height=1/4)

    dm.draw_text(ctx, text="Antifermions", x=1/2, y=0.33, fontsize=16, center_text=True)

    dm.group(ctx, lambda ctx_: cmds_fm_rules_external_fermion_in(ctx_, is_antiparticle=True), x=0, y=0.3, width=1 / 4, height=1 / 4)
    dm.group(ctx, cmds_fm_rules_external_antifermion_in_description, x=1/4, y=0.3, width=1/4, height=1/4)

    dm.group(ctx, lambda ctx_: cmds_fm_rules_external_fermion_out(ctx_, is_antiparticle=True), x=2 / 4, y=0.3, width=1 / 4, height=1 / 4)
    dm.group(ctx, cmds_fm_rules_external_antifermion_out_description, x=3/4, y=0.3, width=1/4, height=1/4)

    dm.draw_text(ctx, text="Photons", x=1/2, y=0.53, fontsize=16, center_text=True)

    dm.group(ctx, cmds_fm_rules_external_photon_in, x=0, y=0.5, width=1/4, height=1/4)
    dm.group(ctx, cmds_fm_rules_external_photon_in_description, x=1/4, y=0.5, width=1/4, height=1/4)

    dm.group(ctx, cmds_fm_rules_external_photon_out, x=2/4, y=0.5, width=1/4, height=1/4)
    dm.group(ctx, cmds_fm_rules_external_photon_out_description, x=3/4, y=0.5, width=1/4, height=1/4)

    dm.draw_text(ctx, text="Gluons", x=1/2, y=0.73, fontsize=16, center_text=True)

    dm.group(ctx, cmds_fm_rules_external_gluon_in, x=0, y=0.7, width=1/4, height=1/4)
    dm.group(ctx, cmds_fm_rules_external_gluon_in_description, x=1/4, y=0.7, width=1/4, height=1/4)

    dm.group(ctx, cmds_fm_rules_external_gluon_out, x=2/4, y=0.7, width=1/4, height=1/4)
    dm.group(ctx, cmds_fm_rules_external_gluon_out_description, x=3/4, y=0.7, width=1/4, height=1/4)


def cmds_fm_rules_external_fermion_in(ctx: svg_high_level, is_antiparticle: bool):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.5)
    vx = dm.Vertex(ctx, 0.9, 0.5)

    dm.vertex(ctx, vx)

    dm.fermion_line(ctx, in_1, vx, is_anti_particle=is_antiparticle)

    if not is_antiparticle:
        dm.draw_formula(ctx, r"f", 0.5, 0.32)
    else:
        dm.draw_formula(ctx, r"\bar{f}", 0.5, 0.32)


def cmds_fm_rules_external_fermion_in_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"=\, u \left(p\right)", x=0.1, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


def cmds_fm_rules_external_antifermion_in_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"=\, \bar{v} \left(p\right)", x=0.1, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


def cmds_fm_rules_external_fermion_out(ctx: svg_high_level, is_antiparticle: bool):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    vx = dm.Vertex(ctx, 0.1, 0.5)
    out_1 = dm.ExtPoint(ctx, 0.9, 0.5)

    dm.vertex(ctx, vx)

    dm.fermion_line(ctx, vx, out_1, is_anti_particle=is_antiparticle)

    if not is_antiparticle:
        dm.draw_formula(ctx, r"f", 0.5, 0.32)
    else:
        dm.draw_formula(ctx, r"\bar{f}", 0.5, 0.32)


def cmds_fm_rules_external_fermion_out_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"=\, \bar{u} \left(p\right)", x=0.1, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


def cmds_fm_rules_external_antifermion_out_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"=\, v \left(p\right)", x=0.1, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


def cmds_fm_rules_external_photon_in(ctx: svg_high_level):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.5)
    vx = dm.Vertex(ctx, 0.9, 0.5)

    dm.vertex(ctx, vx)

    dm.boson_line(ctx, in_1, vx)

    dm.draw_formula(ctx, r"\gamma", 0.5, 0.32)
    dm.draw_formula(ctx, r"\mu", 1, 0.5)


def cmds_fm_rules_external_photon_in_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"=\, \epsilon_\mu \left(p\right)", x=0.1, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


def cmds_fm_rules_external_photon_out(ctx: svg_high_level):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    vx = dm.Vertex(ctx, 0.1, 0.5)
    out_1 = dm.ExtPoint(ctx, 0.9, 0.5)

    dm.vertex(ctx, vx)

    dm.boson_line(ctx, vx, out_1)

    dm.draw_formula(ctx, r"\gamma", 0.5, 0.32)
    dm.draw_formula(ctx, r"\mu", 0, 0.5)


def cmds_fm_rules_external_photon_out_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"=\, \epsilon_\mu^\ast \left(p\right)", x=0.1, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


def cmds_fm_rules_external_gluon_in(ctx: svg_high_level):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    in_1 = dm.ExtPoint(ctx, 0.1, 0.5)
    vx = dm.Vertex(ctx, 0.9, 0.5)

    dm.vertex(ctx, vx)

    dm.gluon_line(ctx, in_1, vx, center=False, number_of_loops=6)

    dm.draw_formula(ctx, r"g", 0.5, 0.32)
    dm.draw_formula(ctx, r"\mu", 1, 0.5)


def cmds_fm_rules_external_gluon_in_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"=\, \epsilon_\mu \left(p\right)", x=0.1, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


def cmds_fm_rules_external_gluon_out(ctx: svg_high_level):
    ctx.set_fontsize(20)
    ctx.set_line_width(2)

    vx = dm.Vertex(ctx, 0.1, 0.5)
    out_1 = dm.ExtPoint(ctx, 0.9, 0.5)

    dm.vertex(ctx, vx)

    dm.gluon_line(ctx, vx, out_1, center=False, number_of_loops=6)

    dm.draw_formula(ctx, r"g", 0.5, 0.32)
    dm.draw_formula(ctx, r"\mu", 0, 0.5)


def cmds_fm_rules_external_gluon_out_description(ctx: svg_high_level.Context):
    dm.draw_formula(ctx, formula=r"=\, \epsilon_\mu^\ast \left(p\right)", x=0.1, y=0.5, fontsize=FORMULA_FONTSIZE, center_x=False)


if __name__ == "__main__":
    main()
