import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
    gradient = np.array(gradient, dtype=float)
    magnitude = np.linalg.norm(gradient)
	if magnitude == 0:
        return {
            "magnitude": 0.0,
            "direction": [0.0] * gradient.shape[0],
            "descent_direction": [0.0] * gradient.shape[0]
        }
    direction = gradient / magnitude
    descent_direction = -direction
    return {
        "magnitude": magnitude,
        "direction": direction.tolist(),
        "descent_direction": descent_direction.tolist()
    }