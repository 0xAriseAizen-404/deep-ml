import numpy as np

def cross_product(a, b):
    return [a[1]*b[2] - a[2]*b[1], 
    a[2]*b[0] - a[0]*b[2],
    a[0]*b[1] - a[1]*b[0]]
    
    # Cross Product of two vectors, is a Area of the paralellogram formed by those two vectors in 2D or 3D.
    # A X B = (-1)^(z) * Area of the Paralellogram
    # -1^z is basically a sign representing the positive or negative of the area
    # z = 1, if the Vector B is on right side (or Clockwise) of Vector A = Negative
    # z = 2, if the Vector B is on left side (or Anti-Clockwise) of Vector A = Positive
    # positive if BBB is anticlockwise from AAA
    # negative if BBB is clockwise from AAA
    # zero if they are collinear
    # 
    # how to find that area of the paralellogram,
    # its nothing but the Determinant formed from those two vectors in a space, right.
    # A = [a1 a2]
    # B = [b1 b2]
    # A X B = -1^z * (a1b2 - a2b1)
    # 
    # => Why Determinant Gives Area
    # The absolute value of a determinant measures how much area is scaled by the transformation.
    # Area of parallelogram = ∣det(M)∣​
    # 
    # => In 3D Space
    # there is another information in terms of Cross product.
    # here in 3D space, two vectors A and B, its cross product gives Area of the Paralellogram, i.e, their Determinant
    # but, that Area of the Paralellogram or Determinant of those two vectors, will also nothing but the Magnitude of the Vector which is perpendicular to those both vectors, and its Direction is given by Right-Hand-Thumb-Rule, Pointing Vector A in Point Finger direction and Pointing Vector B in Middle Finger direction and the direction of Right Hand Thumb finger gives the direction of that Vector A X B.
    # So, A X B = A Vector perpendicular to both vectors & having right-hand-thumb-rule direction
    # |A X B| = Area of the Paralellogram or Determinant of two vectors A & B
    # Vector representation of the A X B can be get with,
    # [i a1 b1]
    # [j a2 b2]
    # [k a3 b3]
    # Determinant along column 0,
    # A X B = i(a2b3-a3b2) - j(a3b1-a1b3) + k(a1b2-a2b1) = Vector Representation of A X B
    # |A X B| = sqrt((a2b3-a3b2)**2 + (a3b1-a1b3)**2 + (a1b2-a2b1)**2) = Area of the Paralellogram A X B = Magnitude of A X B
    # |A X B| = |A||B|Sin(theta)
    # 
    # In 2D:
    # A × B = a1b2 - a2b1
    # which is exactly the determinant:
    # | a1  b1 |
    # | a2  b2 |
    # Hence, Area = |Determinant|
    # In 3D:
    # A and B together form a 3×2 matrix:
    # | a1 b1 |
    # | a2 b2 |
    # | a3 b3 |
    # A determinant is defined only for square matrices.
    # Since a 3×2 matrix is NOT square,
    # "Determinant of A and B" is NOT defined.
    # Therefore, |A × B| ≠ Determinant(A,B)
    # The cross product vector is built using several 2×2 determinants, but its magnitude itself is not a determinant.

"""
========================================
CROSS PRODUCT OF TWO VECTORS
========================================

----------------------------------------
1. Cross Product in 2D
----------------------------------------

Let,

A = [a1, a2]
B = [b1, b2]

The 2D cross product is defined as:

A × B = a1b2 - a2b1

This is a SCALAR (single number), not a vector.

Interpretation:

A × B > 0  => B is Anti-Clockwise (Left) of A
A × B < 0  => B is Clockwise (Right) of A
A × B = 0  => A and B are Collinear

Area of the parallelogram formed by A and B:

Area = |A × B|
      = |a1b2 - a2b1|

This value is also equal to the determinant:

| a1  b1 |
| a2  b2 |

Therefore,

A × B = ± Area

where the sign indicates orientation.

Also,

A × B = |A||B|sin(θ)

and

Area = |A||B|sin(θ)



----------------------------------------
2. Cross Product in 3D
----------------------------------------

Let,

A = [a1, a2, a3]
B = [b1, b2, b3]

The cross product is a VECTOR.

It can be computed using:

| i   j   k  |
| a1 a2 a3 |
| b1 b2 b3 |

Expanding along the first row:

A × B

= i(a2b3 - a3b2)
- j(a1b3 - a3b1)
+ k(a1b2 - a2b1)

or

A × B

= (a2b3 - a3b2,
   a3b1 - a1b3,
   a1b2 - a2b1)



----------------------------------------
3. Meaning of A × B in 3D
----------------------------------------

The vector A × B contains:

1. Magnitude
2. Direction

Direction:
- Perpendicular to both A and B
- Determined by the Right-Hand Rule

Right-Hand Rule:
- Index Finger  -> A
- Middle Finger -> B
- Thumb         -> A × B

Thus,

A × B = (Area of Parallelogram) × (Unit Normal Vector)



----------------------------------------
4. Magnitude of A × B
----------------------------------------

|A × B|

= √[(a2b3-a3b2)^2
   +(a3b1-a1b3)^2
   +(a1b2-a2b1)^2]

This magnitude equals the area of the parallelogram formed by A and B.

Therefore,

|A × B|
= Area of Parallelogram
= |A||B|sin(θ)



----------------------------------------
5. Important Note About Determinants
----------------------------------------

In 2D:

A × B

= a1b2 - a2b1

which is exactly the determinant:

| a1  b1 |
| a2  b2 |

Hence,

Area = |Determinant|


In 3D:

A and B together form a 3×2 matrix:

| a1 b1 |
| a2 b2 |
| a3 b3 |

A determinant is defined only for square matrices.

Since a 3×2 matrix is NOT square,

"Determinant of A and B" is NOT defined.

Therefore,

|A × B| ≠ Determinant(A,B)

The cross product vector is built using several 2×2 determinants, but its magnitude itself is not a determinant.



----------------------------------------
6. Final Summary
----------------------------------------

2D:

A × B = a1b2 - a2b1

|A × B| = Area of Parallelogram

Sign of (A × B) gives orientation:
+ => Anti-Clockwise
- => Clockwise


3D:

A × B = Vector perpendicular to A and B

Direction:
- Right-Hand Rule

Magnitude:

|A × B|
= Area of Parallelogram
= |A||B|sin(θ)

The cross product vector stores:
- Area (magnitude)
- Normal direction (orientation in space)
"""