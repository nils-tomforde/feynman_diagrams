import thesis_diagrams
import thesis_diagrams_nnlo
import thesis_feynman_rules
import thesis_other_graphics

import diagram_maker as dm
import svg_high_level


def main():
    dm.draw_diagram(width=256, height=512, commands=lambda ctx: thesis_diagrams.cmds_standard_process(ctx, "fermions", True), file_path=".\\output\\presentation\\diagrams\\diagram_tree_level_fermions_momenta.svg")
    dm.draw_diagram(width=256, height=512, commands=lambda ctx: thesis_diagrams.cmds_virtual_gluon_process(ctx, True), file_path=".\\output\\presentation\\diagrams\\diagram_virtual_momenta.svg")
    dm.draw_diagram(width=512, height=512, commands=lambda ctx: thesis_diagrams.cmds_real_gluon_emission_both(ctx, True), file_path=".\\output\\presentation\\diagrams\\diagrams_emission_momenta.svg")




if __name__ == "__main__":
    main()
