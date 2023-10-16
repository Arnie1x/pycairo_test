import cairo
import functions as draw

with cairo.SVGSurface("example.svg", 2000, 2000) as surface:
    ctx = cairo.Context(surface)
    ctx.paint()

    gradient_1 = cairo.LinearGradient(0.0, 0.0, 600.0, 400.0)
    gradient_1.add_color_stop_rgba(1, 0.7, 0, 0, 1)  # First stop, 50% opacity
    gradient_1.add_color_stop_rgba(0, 0.9, 0.7, 0.2, 1)  # Last stop, 100% opacity

    gradient_2 = cairo.LinearGradient(0.0, 0.0, 600.0, 400.0)
    gradient_2.add_color_stop_rgba(1, 0.2, 0.3, 0.8, 1)  # First stop, 50% opacity
    gradient_2.add_color_stop_rgba(0, 0.5, 0.1, 0.6, 1)  # Last stop, 100% opacity

    draw.rectangle(ctx, 250, 500, 1500, 1000)
    draw.color(ctx, True, 1, 1, 1, 1)
    # draw.gradient(ctx, True, gradient_2)

    draw.circle(ctx, 1000, 1000, 120, 0, 360)
    draw.gradient(ctx, True, gradient_1)

    # ctx.stroke()
    # ctx.scale(600, 400)
    surface.write_to_png('example.png')
