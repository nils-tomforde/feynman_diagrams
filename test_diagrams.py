
import diagram_maker as dm
import svg_high_level


def main():
    # Propagators
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, type="photon"), file_path=".\\output\\tests\\test_photon.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, type="gluon_centered"), file_path=".\\output\\tests\\test_gluon_centered.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, type="gluon_uncentered"), file_path=".\\output\\tests\\test_gluon_uncentered.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, type="scalar"), file_path=".\\output\\tests\\test_scalar.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, type="double_line"), file_path=".\\output\\tests\\test_double_line.svg")


def cmds_test_propagator(ctx: svg_high_level.Context, type: str):

    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)
    dm.grid(ctx)

    vx_a1 = dm.Vertex(ctx, 0.1, 0.1)
    vx_a2 = dm.Vertex(ctx, 0.2, 0.1)

    vx_b1 = dm.Vertex(ctx, 0.1, 0.3)
    vx_b2 = dm.Vertex(ctx, 0.3, 0.3)

    vx_c1 = dm.Vertex(ctx, 0.1, 0.5)
    vx_c2 = dm.Vertex(ctx, 0.5, 0.5)

    vx_d1 = dm.Vertex(ctx, 0.1, 0.7)
    vx_d2 = dm.Vertex(ctx, 0.7, 0.7)

    vx_e1 = dm.Vertex(ctx, 0.1, 0.9)
    vx_e2 = dm.Vertex(ctx, 0.9, 0.9)

    vx_f1 = dm.Vertex(ctx, 0.4, 0.1)
    vx_f2 = dm.Vertex(ctx, 0.6, 0.3)

    vx_g1 = dm.Vertex(ctx, 0.7, 0.3)
    vx_g2 = dm.Vertex(ctx, 0.9, 0.1)

    vx_h1 = dm.Vertex(ctx, 0.9, 0.3)
    vx_h2 = dm.Vertex(ctx, 0.9, 0.7)

    if type == "photon":
        dm.boson_line(ctx, vx_a1, vx_a2)
        dm.boson_line(ctx, vx_b1, vx_b2)
        dm.boson_line(ctx, vx_c1, vx_c2)
        dm.boson_line(ctx, vx_d1, vx_d2)
        dm.boson_line(ctx, vx_e1, vx_e2)
        dm.boson_line(ctx, vx_f1, vx_f2)
        dm.boson_line(ctx, vx_g1, vx_g2)
        dm.boson_line(ctx, vx_h1, vx_h2)

    elif type == "gluon_centered":
        dm.gluon_line(ctx, vx_a1, vx_a2)
        dm.gluon_line(ctx, vx_b1, vx_b2)
        dm.gluon_line(ctx, vx_c1, vx_c2)
        dm.gluon_line(ctx, vx_d1, vx_d2)
        dm.gluon_line(ctx, vx_e1, vx_e2)
        dm.gluon_line(ctx, vx_f1, vx_f2)
        dm.gluon_line(ctx, vx_g1, vx_g2)
        dm.gluon_line(ctx, vx_h1, vx_h2)

    elif type == "gluon_uncentered":
        dm.gluon_line(ctx, vx_a1, vx_a2, center=False)
        dm.gluon_line(ctx, vx_b1, vx_b2, center=False)
        dm.gluon_line(ctx, vx_c1, vx_c2, center=False)
        dm.gluon_line(ctx, vx_d1, vx_d2, center=False)
        dm.gluon_line(ctx, vx_e1, vx_e2, center=False)
        dm.gluon_line(ctx, vx_f1, vx_f2, center=False)
        dm.gluon_line(ctx, vx_g1, vx_g2, center=False)
        dm.gluon_line(ctx, vx_h1, vx_h2, center=False)

    elif type == "scalar":
        dm.scalar_line(ctx, vx_a1, vx_a2)
        dm.scalar_line(ctx, vx_b1, vx_b2)
        dm.scalar_line(ctx, vx_c1, vx_c2)
        dm.scalar_line(ctx, vx_d1, vx_d2)
        dm.scalar_line(ctx, vx_e1, vx_e2)
        dm.scalar_line(ctx, vx_f1, vx_f2)
        dm.scalar_line(ctx, vx_g1, vx_g2)
        dm.scalar_line(ctx, vx_h1, vx_h2)

    elif type == "double_line":
        dm.double_line(ctx, vx_a1, vx_a2)
        dm.double_line(ctx, vx_b1, vx_b2)
        dm.double_line(ctx, vx_c1, vx_c2)
        dm.double_line(ctx, vx_d1, vx_d2)
        dm.double_line(ctx, vx_e1, vx_e2)
        dm.double_line(ctx, vx_f1, vx_f2)
        dm.double_line(ctx, vx_g1, vx_g2)
        dm.double_line(ctx, vx_h1, vx_h2)

    dm.vertex(ctx, vx_a1)
    dm.vertex(ctx, vx_a2)

    dm.vertex(ctx, vx_b1)
    dm.vertex(ctx, vx_b2)

    dm.vertex(ctx, vx_c1)
    dm.vertex(ctx, vx_c2)

    dm.vertex(ctx, vx_d1)
    dm.vertex(ctx, vx_d2)

    dm.vertex(ctx, vx_e1)
    dm.vertex(ctx, vx_e2)

    dm.vertex(ctx, vx_f1)
    dm.vertex(ctx, vx_f2)

    dm.vertex(ctx, vx_g1)
    dm.vertex(ctx, vx_g2)

    dm.vertex(ctx, vx_h1)
    dm.vertex(ctx, vx_h2)


if __name__ == "__main__":
    main()
