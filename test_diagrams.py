
import diagram_maker as dm
import svg_high_level


def main():
    # Propagators / Lines
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, mode="photon"), file_path=".\\output\\tests\\test_photon.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, mode="gluon_centered"), file_path=".\\output\\tests\\test_gluon_centered.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, mode="gluon_uncentered"), file_path=".\\output\\tests\\test_gluon_uncentered.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, mode="scalar"), file_path=".\\output\\tests\\test_scalar.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, mode="ghost"), file_path=".\\output\\tests\\test_ghost.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, mode="double_line"), file_path=".\\output\\tests\\test_double_line.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, mode="fermion"), file_path=".\\output\\tests\\test_fermion.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, mode="anti_fermion"), file_path=".\\output\\tests\\test_anti_fermion.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: cmds_test_propagator(ctx, mode="arrow"), file_path=".\\output\\tests\\test_arrow.svg")


def cmds_test_propagator(ctx: svg_high_level.Context, mode: str):

    ctx.set_fontsize(20)
    ctx.set_line_width(2)
    ctx.set_line_color((0, 0, 0))
    ctx.set_font_color((0, 0, 0))

    dm.set_background(ctx, 255, 255, 255, 1)
    dm.grid(ctx)

    vtc_a = dm.Vertex(ctx, 0.1, 0.1), dm.Vertex(ctx, 0.2, 0.1)
    vtc_b = dm.Vertex(ctx, 0.1, 0.3), dm.Vertex(ctx, 0.3, 0.3)
    vtc_c = dm.Vertex(ctx, 0.1, 0.5), dm.Vertex(ctx, 0.5, 0.5)
    vtc_d = dm.Vertex(ctx, 0.1, 0.7), dm.Vertex(ctx, 0.7, 0.7)
    vtc_e = dm.Vertex(ctx, 0.1, 0.9), dm.Vertex(ctx, 0.9, 0.9)
    vtc_f = dm.Vertex(ctx, 0.4, 0.1), dm.Vertex(ctx, 0.6, 0.3)
    vtc_g = dm.Vertex(ctx, 0.7, 0.3), dm.Vertex(ctx, 0.9, 0.1)
    vtc_h = dm.Vertex(ctx, 0.9, 0.3), dm.Vertex(ctx, 0.9, 0.7)

    vtc = [vtc_a, vtc_b, vtc_c, vtc_d, vtc_e, vtc_f, vtc_g, vtc_h]

    for vtc_i in vtc:
        vx_1, vx_2 = vtc_i

        if mode == "photon":
            dm.boson_line(ctx, vx_1, vx_2)

        elif mode == "gluon_centered":
            dm.gluon_line(ctx, vx_1, vx_2)

        elif mode == "gluon_uncentered":
            dm.gluon_line(ctx, vx_1, vx_2, center=False)

        elif mode == "scalar":
            dm.scalar_line(ctx, vx_1, vx_2)

        elif mode == "ghost":
            dm.ghost_line(ctx, vx_1, vx_2)

        elif mode == "double_line":
            dm.double_line(ctx, vx_1, vx_2)

        elif mode == "fermion":
            dm.fermion_line(ctx, vx_1, vx_2)

        elif mode == "anti_fermion":
            dm.fermion_line(ctx, vx_1, vx_2, is_anti_particle=True)

        elif mode == "arrow":
            dm.draw_arrow(ctx, vx_1, vx_2)

        if mode != "arrow":
            dm.vertex(ctx, vx_1)
            dm.vertex(ctx, vx_2)


if __name__ == "__main__":
    main()
