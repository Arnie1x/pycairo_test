import cairo

with cairo.SVGSurface("example.svg", 600, 400) as surface:
    ctx = cairo.Context(surface)
    ctx.paint()

    gradient_1 = cairo.LinearGradient(0.0, 0.0, 600.0, 400.0)
    gradient_1.add_color_stop_rgba(1, 0.7, 0, 0, 1)  # First stop, 50% opacity
    gradient_1.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)  # Last stop, 100% opacity

    gradient_2 = cairo.LinearGradient(0.0, 0.0, 600.0, 400.0)
    gradient_2.add_color_stop_rgba(1, 0.2, 0.3, 0.8, 1)  # First stop, 50% opacity
    gradient_2.add_color_stop_rgba(0, 0.5, 0.1, 0.6, 1)  # Last stop, 100% opacity

    ctx.rectangle(0, 0, 600, 400)
    ctx.set_source(gradient_2)
    ctx.fill()

    ctx.arc(300, 200, 120, 0, 2 * 22 / 7)
    # ctx.set_source_rgba(0.4, 0.6, 1, 1)
    ctx.set_source(gradient_1)
    ctx.fill()


    # ctx.stroke()
    # ctx.scale(600, 400)
    surface.write_to_png('example.png')
