def RectangleArea(self, A, B, C, D, E, F, G, H):
    height = max(min(D, H) - max(B, F), 0)
    weight = max(min(G, C) - max(A, E), 0)
    return (C - A) * (D - B) + (G - E) * (H - F) - height * weight
