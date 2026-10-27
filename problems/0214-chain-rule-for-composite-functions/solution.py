import numpy as np
def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
	"""
	Compute derivative of composite functions using chain rule.
	
	Args:
		functions: List of function names (applied right to left)
		          Available: 'square', 'sin', 'exp', 'log'
		x: Point at which to evaluate derivative
	
	Returns:
		Derivative value at x
	
	Example:
		['sin', 'square'] represents sin(x²)
		['exp', 'sin', 'square'] represents exp(sin(x²))
	"""
	# My Solution
	def apply_and_derivate(function: str, u: float):
		if function == "square":
			return u * u, 2 * u
		if function == "sin":
			return np.sin(u), np.cos(u)
		if function == "exp":
			return np.exp(u), np.exp(u)
		if function == "log":
			return np.log(u), 1 / u
		raise ValueError(f"Unknown function: {f}")
	
	value = x
	h_x = 1
	for func in functions[::-1]:
		value, local_derivative = apply_and_derivate(func, value)
		h_x *= local_derivative
	return h_x