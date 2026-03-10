def summarize_text(text, max_points=8):

    sentences = text.split(".")
    
    points = []

    for s in sentences:
        s = s.strip()

        if len(s) > 40:
            points.append(s)

        if len(points) == max_points:
            break

    return points