
import math

import latex_to_svg
import svg_handler
import svg_high_level


def draw_diagram(width: int,
                 height: int,
                 commands: callable,
                 file_path: str) -> None:
    ctx = svg_high_level.Context(width=width, height=height)

    commands(ctx)

    ctx.write(file_path=file_path)


def group(context: svg_high_level.Context,
          commands: callable,
          x: float,
          y: float,
          width: float,
          height: float,
          rotation_angle: float = 0) -> None:
    # TODO: Maybe transfer line_color, font_color, line_width, fontsize etc. from context to context_group
    x *= context.scaling_x
    y *= context.scaling_y

    width *= context.scaling_x
    height *= context.scaling_y

    context_group = svg_high_level.Context(width=width, height=height)

    commands(context_group)

    transform_string = f"translate({x},{y}) rotate({rotation_angle})"

    group_tag = svg_handler.Group(transform=transform_string)

    for child in context_group.svg.root_tag.children:
        group_tag.append_child_tag(child)

    context.svg.root_tag.append_child_tag(group_tag)


def draw_formula(context: svg_high_level.Context,
                 formula: str,
                 x: float,
                 y: float,
                 fontsize: float = None,
                 font_color: tuple[float, float, float] = None,
                 center_x: bool = True,
                 center_y: bool = True) -> None:
    # Use context defaults when not overwritten
    if fontsize is None:
        fontsize = context.fontsize

    if font_color is None:
        font_color = context.font_color

    x *= context.scaling_x
    y *= context.scaling_y

    latex_tag = latex_to_svg.latex_to_svg(formula, fontsize, color_rgb_256=font_color, x=x, y=y,
                                          center_x=center_x, center_y=center_y)

    context.svg.root_tag.append_child_tag(latex_tag)


def draw_text(context: svg_high_level.Context,
              text: str,
              x: float,
              y: float,
              fontsize: float = None,
              font_color: tuple[float, float, float] = None,
              center_text: bool = False) -> None:
    # Use context defaults when not overwritten
    if fontsize is None:
        fontsize = context.fontsize

    if font_color is None:
        font_color = context.font_color

    x *= context.scaling_x
    y *= context.scaling_y

    if center_text:
        text_anchor = "middle"
    else:
        text_anchor = "start"

    context.draw_text(text_string=text, x=x, y=y, font_size=fontsize, text_anchor=text_anchor)
    # TODO: Add fontcolor to text


def set_background(context: svg_high_level.Context,
                   r: float,
                   g: float,
                   b: float,
                   a: float) -> None:
    context.draw_rectangle(0, 0, context.width, context.height, fill_color_rgb=(r, g, b), fill_opacity=a)


def _draw_line(context: svg_high_level.Context,
               x1: float,
               y1: float,
               x2: float,
               y2: float,
               line_width=None,
               line_color=None) -> None:
    if line_width is None:
        line_width = context.line_width
    if line_color is None:
        line_color = context.line_color

    context.path_init(stroke_color_rgb=line_color, stroke_width=line_width, fill_opacity=0)
    context.path_move_to(x1, y1)
    context.path_line_to(x2, y2)
    context.path_close()
    context.path_finish()


def _draw_full_circle(context: svg_high_level.Context,
                      cx: float,
                      cy: float,
                      r: float,
                      line_width: float = None,
                      line_color: tuple[float, float, float] = None,
                      fill_color: tuple[float, float, float] = None,
                      fill_opacity: float = None,
                      line_opacity: float = None) -> None:
    if line_width is None:
        line_width = context.line_width
    if line_color is None:
        line_color = context.line_color

    context.draw_circle(cx, cy, r, fill_color_rgb=fill_color, stroke_color_rgb=line_color, fill_opacity=fill_opacity, opacity=line_opacity, stroke_width=line_width)


def _draw_triangle(context: svg_high_level.Context,
                   xm: float,
                   ym: float,
                   angle: float,
                   is_anti_particle: bool) -> None:
    size = context.line_width * 4

    if not is_anti_particle:
        p1 = (size / 2, 0)
        p2 = (- size / 2, size / 2)
        p3 = (- size / 2, -size / 2)
    else:
        p1 = (- size / 2, 0)
        p2 = (size / 2, - size / 2)
        p3 = (size / 2, size / 2)

    p1_rotated = rotate_vector_2d(p1, angle)
    p2_rotated = rotate_vector_2d(p2, angle)
    p3_rotated = rotate_vector_2d(p3, angle)

    context.path_init(fill_color_rgb=context.line_color)
    context.path_move_to(xm + p1_rotated[0], ym + p1_rotated[1])
    context.path_line_to(xm + p2_rotated[0], ym + p2_rotated[1])
    context.path_line_to(xm + p3_rotated[0], ym + p3_rotated[1])
    context.path_close()

    context.path_finish()


def _draw_cross(context: svg_high_level.Context,
                xm: float,
                ym: float,
                angle: float) -> None:
    # TODO: Maybe do it like in Peskin and Schroeder and make a circle around the cross and dont show the underlying line

    size = context.line_width * 6

    p1 = (- size / 2, - size / 2)
    p2 = (+ size / 2, + size / 2)
    p3 = (- size / 2, + size / 2)
    p4 = (+ size / 2, - size / 2)

    p1_rotated = rotate_vector_2d(p1, angle)
    p2_rotated = rotate_vector_2d(p2, angle)
    p3_rotated = rotate_vector_2d(p3, angle)
    p4_rotated = rotate_vector_2d(p4, angle)

    context.path_init(stroke_color_rgb=context.line_color, stroke_width=context.line_width)
    context.path_move_to(xm + p1_rotated[0], ym + p1_rotated[1])
    context.path_line_to(xm + p2_rotated[0], ym + p2_rotated[1])

    context.path_move_to(xm + p3_rotated[0], ym + p3_rotated[1])
    context.path_line_to(xm + p4_rotated[0], ym + p4_rotated[1])

    context.path_finish()


class Point:
    def __init__(self,
                 context: svg_high_level.Context,
                 x: float,
                 y: float) -> None:
        self.x = x * context.scaling_x
        self.y = y * context.scaling_y


class Vertex(Point):
    def __init__(self,
                 context: svg_high_level.Context,
                 x: float,
                 y: float) -> None:
        super().__init__(context, x, y)


class ExtPoint(Point):
    def __init__(self,
                 context: svg_high_level.Context,
                 x: float,
                 y: float) -> None:
        super().__init__(context, x, y)


def vertex(context: svg_high_level.Context,
           p: Point,
           is_counterterm=False) -> None:
    x, y = p.x, p.y

    size = context.line_width * 1.5

    if not is_counterterm:
        _draw_full_circle(context=context, cx=x, cy=y, r=size)
    else:
        _draw_cross(context=context, xm=x, ym=y, angle=0)


def fermion_line(context: svg_high_level.Context,
                 p1: Point,
                 p2: Point,
                 is_anti_particle: bool = False,
                 draw_arrow: bool = True,
                 is_counterterm: bool = False) -> None:
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    _draw_line(context, x1, y1, x2, y2)

    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2

    angle = get_angle(p1, p2)

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle)

    if is_counterterm:
        _draw_cross(context, xm, ym, angle)

    # TODO: shift the triangle if cross is placed


def fermion_line_curved(context: svg_high_level.Context,
                        p1: Point,
                        p2: Point,
                        curvature: str,
                        is_anti_particle: bool = False,
                        draw_arrow: bool = True,
                        is_counterterm: bool = False) -> None:
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    # TODO: Consider: Could also make curvature always in the same direction. Switch direction by reversing p1 and p2

    draw_arc(context, p1, p2, curvature)

    distance = get_distance(p1, p2)
    angle = get_angle(p1, p2)

    if curvature == "right":
        arc_middle_rel_p1 = (distance / 2, - distance / 2)  # position of the middle of the arc relative to point 1
    elif curvature == "left":
        arc_middle_rel_p1 = (distance / 2, distance / 2)
    else:
        raise  # TODO: Add meaningful exception

    arc_middle_rel_p1_rotated = rotate_vector_2d(arc_middle_rel_p1, angle)

    xm = x1 + arc_middle_rel_p1_rotated[0]
    ym = y1 + arc_middle_rel_p1_rotated[1]

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle)
    if is_counterterm:
        _draw_cross(context, xm, ym, angle)


def boson_line(context: svg_high_level.Context,
               p1: Point,
               p2: Point,
               is_anti_particle: bool = False,
               draw_arrow: bool = False,
               is_counterterm: bool = False,
               start_with_dale: bool = False,
               number_of_waves: int = 6) -> None:
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y
    # TODO: Make wave density constant
    # TODO: Add possibility to change whether wave starts with hill or dale

    shift_size = 5 * context.line_width

    if start_with_dale:
        shift_size *= -1

    distance = get_distance(p1, p2)

    step_size = distance / (2 * number_of_waves)

    angle = get_angle(p1, p2)

    context.path_init(stroke_color_rgb=context.line_color, stroke_width=context.line_width, fill_opacity=0)
    context.path_move_to(x1, y1)

    for i in range(2 * number_of_waves):
        if i % 2 == 0:
            shift = - shift_size
        else:
            shift = shift_size

        p1 = (step_size / 3, shift)
        p2 = (2 * step_size / 3, shift)
        p3 = (step_size, 0)

        p1_rotated = rotate_vector_2d(p1, angle)
        p2_rotated = rotate_vector_2d(p2, angle)
        p3_rotated = rotate_vector_2d(p3, angle)

        context.path_rel_cubic_bezier(p1_rotated[0], p1_rotated[1],
                                      p2_rotated[0], p2_rotated[1],
                                      p3_rotated[0], p3_rotated[1])

    context.path_finish()

    if draw_arrow or is_counterterm:
        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle)

    if is_counterterm:
        _draw_cross(context, xm, ym, angle)


def boson_line_curved(context: svg_high_level.Context,
                      p1: Point,
                      p2: Point,
                      curvature: str,
                      start_with_dale: bool = False,
                      is_anti_particle: bool = False,
                      draw_arrow: bool = False,
                      is_counterterm: bool = False) -> None:
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    number_of_waves = 6
    shift_size = 5 * context.line_width

    distance = get_distance(p1, p2)
    step_size = distance / (2 * number_of_waves + 1)

    angle = get_angle(p1, p2)

    context.path_init(stroke_color_rgb=context.line_color, stroke_width=context.line_width, fill_opacity=0)
    context.path_move_to(x1, y1)

    if start_with_dale:
        shift_size *= -1

    for i in range(2 * number_of_waves + 1):  # Add one to symmetrize
        if i % 2 == 0:
            shift = - shift_size
        else:
            shift = shift_size

        angle_arc = i * math.pi / (2 * number_of_waves + 1)
        angle_arc_next = (i + 1) * math.pi / (2 * number_of_waves + 1)

        x = (- math.cos(angle_arc_next) + math.cos(angle_arc)) * distance / 2
        y = (- math.sin(angle_arc_next) + math.sin(angle_arc)) * distance / 2

        p3 = (x, y)
        p3_rotated = rotate_vector_2d(p3, angle)

        distance_to_next_point = math.sqrt(x**2 + y**2)

        if shift < 0:
            p1 = (distance_to_next_point / 3, shift)
            p2 = (2 * distance_to_next_point / 3, shift)
        else:  # shorten the shifts of inner curves (they are shorter because they lie inside the circle!)
            p1 = (distance_to_next_point / 3, shift * (step_size / distance_to_next_point))
            p2 = (2 * distance_to_next_point / 3, shift * (step_size / distance_to_next_point))

        p1_rotated = rotate_vector_2d(p1, math.pi / 2 - (angle_arc + angle_arc_next) / 2 + angle)
        p2_rotated = rotate_vector_2d(p2, math.pi / 2 - (angle_arc + angle_arc_next) / 2 + angle)

        context.path_rel_cubic_bezier(p1_rotated[0], p1_rotated[1],
                                      p2_rotated[0], p2_rotated[1],
                                      p3_rotated[0], p3_rotated[1])

    context.path_line_to(x2, y2)

    context.path_finish()


def gluon_line(context: svg_high_level.Context,
               p1: Point,
               p2: Point,
               center: bool = True,
               is_anti_particle: bool = False,
               draw_arrow: bool = False,
               is_counterterm: bool = False,
               number_of_loops: int = 8) -> None:
    # TODO: Make loops density continuous
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    distance = get_distance(p1, p2)
    if center:
        step_size = distance / (number_of_loops + 2)
    else:
        step_size = distance / number_of_loops

    loop_width = step_size  # 0.05 ist ein guter Wert
    loop_height = 8 * context.line_width

    angle = get_angle(p1, p2)

    context.path_init(stroke_color_rgb=context.line_color, stroke_width=context.line_width, fill_opacity=0)
    context.path_move_to(x1, y1)

    if center:
        # starting connection
        ps1 = (loop_width, 0)
        ps2 = (0, - loop_height / 2)
        ps3 = (loop_width, - loop_height / 2)

        # ending connection
        pe1 = (loop_width, 0)
        pe2 = (0, loop_height / 2)
        pe3 = (loop_width, loop_height / 2)

        ps1_rotated = rotate_vector_2d(ps1, angle)
        ps2_rotated = rotate_vector_2d(ps2, angle)
        ps3_rotated = rotate_vector_2d(ps3, angle)

        pe1_rotated = rotate_vector_2d(pe1, angle)
        pe2_rotated = rotate_vector_2d(pe2, angle)
        pe3_rotated = rotate_vector_2d(pe3, angle)

    # loop first half
    pa1 = (loop_width, 0)
    pa2 = (loop_width, loop_height)
    pa3 = (loop_width / 2, loop_height)

    # loop second half
    pb1 = (- loop_width / 2, 0)
    pb2 = (- loop_width / 2, - loop_height)
    pb3 = (loop_width / 2, - loop_height)

    pa1_rotated = rotate_vector_2d(pa1, angle)
    pa2_rotated = rotate_vector_2d(pa2, angle)
    pa3_rotated = rotate_vector_2d(pa3, angle)

    pb1_rotated = rotate_vector_2d(pb1, angle)
    pb2_rotated = rotate_vector_2d(pb2, angle)
    pb3_rotated = rotate_vector_2d(pb3, angle)

    if center:
        context.path_rel_cubic_bezier(ps1_rotated[0], ps1_rotated[1],
                                      ps2_rotated[0], ps2_rotated[1],
                                      ps3_rotated[0], ps3_rotated[1])

    for i in range(number_of_loops):
        context.path_rel_cubic_bezier(pa1_rotated[0], pa1_rotated[1],
                                      pa2_rotated[0], pa2_rotated[1],
                                      pa3_rotated[0], pa3_rotated[1])
        context.path_rel_cubic_bezier(pb1_rotated[0], pb1_rotated[1],
                                      pb2_rotated[0], pb2_rotated[1],
                                      pb3_rotated[0], pb3_rotated[1])

    if center:
        context.path_rel_cubic_bezier(pe1_rotated[0], pe1_rotated[1],
                                      pe2_rotated[0], pe2_rotated[1],
                                      pe3_rotated[0], pe3_rotated[1])

    context.path_finish()

    if draw_arrow or is_counterterm:
        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle)

    if is_counterterm:
        _draw_cross(context, xm, ym, angle)


def gluon_line_curved(context: svg_high_level.Context,
                      p1: Point,
                      p2: Point,
                      center: bool = True,
                      is_anti_particle: bool = True,
                      draw_arrow: bool = True,
                      is_counterterm: bool = False) -> None:
    # TODO: Improve this function! Results are not smooth!

    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    number_of_loops = 8

    distance = get_distance(p1, p2)

    if center:
        step_size = distance / (number_of_loops + 2)
    else:
        step_size = distance / number_of_loops

    loop_width = step_size

    loop_height = 8 * context.line_width

    angle = get_angle(p1, p2)

    context.path_init(stroke_color_rgb=context.line_color, stroke_width=context.line_width, fill_opacity=0)
    context.path_move_to(x1, y1)

    for i in range(number_of_loops):

        angle_arc = i * math.pi / number_of_loops
        angle_arc_next = (i + 1) * math.pi / number_of_loops

        x = (- math.cos(angle_arc_next) + math.cos(angle_arc)) * distance / 2
        y = (- math.sin(angle_arc_next) + math.sin(angle_arc)) * distance / 2

        p3 = (x, y)
        p3_rotated = rotate_vector_2d(p3, angle)

        distance_to_next_point = math.sqrt(x**2 + y**2)

        # loop first half
        pa1 = (distance_to_next_point, 0)
        pa2 = (distance_to_next_point, loop_height)
        pa3 = (distance_to_next_point / 2, loop_height)

        # loop second half
        pb1 = (- distance_to_next_point / 2, 0)
        pb2 = (- distance_to_next_point / 2, - loop_height)
        pb3 = (distance_to_next_point / 2, - loop_height)

        pa1_rotated = rotate_vector_2d(pa1, math.pi / 2 - (angle_arc + angle_arc_next) / 2 + angle)
        pa2_rotated = rotate_vector_2d(pa2, math.pi / 2 - (angle_arc + angle_arc_next) / 2 + angle)
        pa3_rotated = rotate_vector_2d(pa3, math.pi / 2 - (angle_arc + angle_arc_next) / 2 + angle)

        pb1_rotated = rotate_vector_2d(pb1, math.pi / 2 - (angle_arc + angle_arc_next) / 2 + angle)
        pb2_rotated = rotate_vector_2d(pb2, math.pi / 2 - (angle_arc + angle_arc_next) / 2 + angle)
        pb3_rotated = rotate_vector_2d(pb3, math.pi / 2 - (angle_arc + angle_arc_next) / 2 + angle)

        context.path_rel_cubic_bezier(pa1_rotated[0], pa1_rotated[1],
                                      pa2_rotated[0], pa2_rotated[1],
                                      pa3_rotated[0], pa3_rotated[1])

        context.path_rel_cubic_bezier(pb1_rotated[0], pb1_rotated[1],
                                      pb2_rotated[0], pb2_rotated[1],
                                      pb3_rotated[0], pb3_rotated[1])

        # context.path_rel_line_to(p3_rotated[0], p3_rotated[1])

    context.path_finish()


def scalar_line(context: svg_high_level.Context,
                p1: Point,
                p2: Point,
                is_anti_particle: bool = False,
                draw_arrow: bool = False,
                is_counterterm: bool = False) -> None:
    # TODO: Maybe use stroke dasharray instead
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    number_of_dashes = 6

    distance = get_distance(p1, p2)
    step_size = distance / (2 * number_of_dashes - 1)

    angle = get_angle(p1, p2)

    context.path_init(stroke_color_rgb=context.line_color, stroke_width=context.line_width, fill_opacity=0)
    context.path_move_to(x1, y1)

    for i in range(2 * number_of_dashes - 1):
        p = (step_size, 0)

        p_rotated = rotate_vector_2d(p, angle)

        if i % 2 == 1:
            context.path_rel_move_to(p_rotated[0], p_rotated[1])
        else:
            context.path_rel_line_to(p_rotated[0], p_rotated[1])

    context.path_finish()

    if draw_arrow or is_counterterm:
        xm = (x2 + x1) / 2
        ym = (y2 + y1) / 2

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle)
    if is_counterterm:
        _draw_cross(context, xm, ym, angle)


def ghost_line(context: svg_high_level.Context,
               p1: Point,
               p2: Point,
               is_anti_particle: bool = False,
               draw_arrow: bool = True,
               is_counterterm: bool = False) -> None:
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    number_of_dots = 20

    distance = get_distance(p1, p2)
    step_size = distance / number_of_dots

    angle = get_angle(p1, p2)

    current_position_x = x1
    current_position_y = y1

    for i in range(number_of_dots):
        p = (step_size, 0)

        p_rotated = rotate_vector_2d(p, angle)

        current_position_x += p_rotated[0]
        current_position_y += p_rotated[1]

        _draw_full_circle(context, current_position_x, current_position_y, context.line_width * 0.5)

    if draw_arrow or is_counterterm:
        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle=is_anti_particle)

    if is_counterterm:
        _draw_cross(context, xm, ym, angle)


def ghost_line_curved(context: svg_high_level.Context,
                      p1: Point,
                      p2: Point,
                      curvature: str,
                      is_antiparticle: bool = False,
                      draw_arrow: bool = True,
                      is_counterterm: bool = False,
                      number_of_dots: int = 20) -> None:
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    distance = get_distance(p1, p2)
    angle = get_angle(p1, p2)

    curvature_radius = distance / 2

    for i in range(1, number_of_dots):
        angle_i = i * math.pi / number_of_dots

        x = - math.cos(angle_i) * distance / 2 + distance / 2
        y = - math.sin(angle_i) * distance / 2

        if curvature == "left":
            y *= -1
        elif curvature == "right":
            pass
        else:
            raise

        p = (x, y)
        p_rotated = rotate_vector_2d(p, angle)

        _draw_full_circle(context, x1 + p_rotated[0], y1 + p_rotated[1], r=context.line_width*0.5)

    if curvature == "left":
        m_shift = rotate_vector_2d((0, distance / 2), angle)
    elif curvature == "right":
        m_shift = rotate_vector_2d((0, - distance / 2), angle)
    else:
        raise

    xm = (x1 + x2) / 2 + m_shift[0]
    ym = (y1 + y2) / 2 + m_shift[1]

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle=is_antiparticle)

    if is_counterterm:
        _draw_cross(context, xm, ym, angle)


def double_line(context: svg_high_level.Context,
                p1: Point,
                p2: Point,
                is_anti_particle: bool = False,
                draw_arrow: bool = False,
                is_counterterm: bool = False) -> None:
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    shift = 1.5 * context.line_width

    # TODO: Shift is here hardcoded in y !!! this must also respect the angle of the line!

    _draw_line(context, x1, y1 + shift / 2, x2, y2 + shift / 2)
    _draw_line(context, x1, y1 - shift / 2, x2, y2 - shift / 2)

    if draw_arrow or is_counterterm:
        angle = get_angle(p1, p2)

        xm = (x1 + x2) / 2
        ym = (y1 + y2) / 2

    if draw_arrow:
        _draw_triangle(context, xm, ym, angle, is_anti_particle)

    if is_counterterm:
        _draw_cross(context, xm, ym, angle)


def draw_arrow(context: svg_high_level.Context,
               p1: Point,
               p2: Point) -> None:
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y
    angle = get_angle(p1, p2)

    _draw_line(context, x1, y1, x2, y2)
    _draw_triangle(context, x2, y2, angle=angle, is_anti_particle=False)


def draw_circle(context: svg_high_level.Context,
                p: Point,
                radius: float,
                line_width: float = None,
                line_color: tuple[float, float, float] = None,
                fill_color: tuple[float, float, float] = None,
                fill_opacity: float = None,
                line_opacity: float = None) -> None:
    cx, cy = p.x, p.y

    _draw_full_circle(context, cx=cx, cy=cy, r=radius, line_width=line_width, line_color=line_color,
                      fill_color=fill_color, fill_opacity=fill_opacity, line_opacity=line_opacity)


def grid(context: svg_high_level.Context) -> None:
    # vertical lines
    for x in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        _draw_line(context,
                   x * context.scaling_x, 0 * context.scaling_y,
                   x * context.scaling_x, 1 * context.scaling_y,
                   line_color=(100, 100, 100),
                   line_width=1)

        draw_text(context, str(x), x=x+0.01, y=0.04, fontsize=8)

    # horizontal lines
    for y in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
        _draw_line(context,
                   0 * context.scaling_x, y * context.scaling_y,
                   1 * context.scaling_x, y * context.scaling_y,
                   line_color=(100, 100, 100),
                   line_width=1)

        draw_text(context, str(y), x=0.01, y=y+0.02, fontsize=8)


def draw_arc(context: svg_high_level.Context,
             p1: Point,
             p2: Point,
             curvature: str) -> None:
    # curvature: "right" or "left"
    x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y

    distance = get_distance(p1, p2)
    arc_radius = distance / 2

    angle = get_angle(p1, p2)

    context.path_init(stroke_color_rgb=context.line_color, stroke_width=context.line_width, fill_opacity=0)
    context.path_move_to(x1, y1)

    factor = (4 / 3) * (math.sqrt(2) - 1)
    # see https://stackoverflow.com/questions/1734745/how-to-create-circle-with-bézier-curves

    # first Bézier curve (coordinates relative to start)
    if curvature == "right":
        c11 = (0, - factor * arc_radius)
        c12 = ((1 - factor) * arc_radius, - arc_radius)
        p1 = (arc_radius, - arc_radius)
    elif curvature == "left":
        c11 = (0, factor * arc_radius)
        c12 = ((1 - factor) * arc_radius, arc_radius)
        p1 = (arc_radius, arc_radius)
    else:
        raise  # TODO: Add meaningful exception

    c11_rotated = rotate_vector_2d(c11, angle)
    c12_rotated = rotate_vector_2d(c12, angle)
    p1_rotated = rotate_vector_2d(p1, angle)

    context.path_rel_cubic_bezier(c11_rotated[0], c11_rotated[1],
                                  c12_rotated[0], c12_rotated[1],
                                  p1_rotated[0], p1_rotated[1])

    # second Bézier curve (coordinates relative to end of first Bézier curve)
    if curvature == "right":
        c21 = (factor * arc_radius, 0)
        c22 = (arc_radius, (1 - factor) * arc_radius)
        p2 = (arc_radius, arc_radius)
    elif curvature == "left":
        c21 = (factor * arc_radius, 0)
        c22 = (arc_radius, (factor - 1) * arc_radius)
        p2 = (arc_radius, - arc_radius)
    else:
        raise  # TODO: Add meaningful exception

    c21_rotated = rotate_vector_2d(c21, angle)
    c22_rotated = rotate_vector_2d(c22, angle)
    p2_rotated = rotate_vector_2d(p2, angle)

    context.path_rel_cubic_bezier(c21_rotated[0], c21_rotated[1],
                                  c22_rotated[0], c22_rotated[1],
                                  p2_rotated[0], p2_rotated[1])

    context.path_finish()


def get_distance(p1: Point, p2: Point) -> float:
    distance = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    return distance


def get_angle(p1: Point, p2: Point) -> float:
    angle = - math.atan2(p2.y - p1.y, p2.x - p1.x)
    return angle


def rotate_vector_2d(vec_in: tuple[float, float],
                     angle: float) -> tuple[float, float]:
    x_out = math.cos(angle) * vec_in[0] + math.sin(angle) * vec_in[1]
    y_out = - math.sin(angle) * vec_in[0] + math.cos(angle) * vec_in[1]

    vec_out = (x_out, y_out)

    return vec_out
