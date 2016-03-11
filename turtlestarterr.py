import turtle

def draw_side(t, side_len, num_bumps):
    if num_bumps == 0:
        t.forward(side_len)
    else:
        draw_side(t, side_len/3.0, num_bumps-1)
        t.left(-60)
        draw_side(t, side_len/3.0, num_bumps-1)
        t.left(120)
        draw_side(t, side_len/3.0, num_bumps-1)
        t.left(-60)
        draw_side(t, side_len/3.0, num_bumps-1)

    
