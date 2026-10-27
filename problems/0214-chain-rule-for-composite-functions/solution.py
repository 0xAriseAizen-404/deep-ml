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
	def derivate_function(function: str, u: float):
		if function == "square":
			return u * u, 2 * u
		elif function == "sin":
			return np.sin(u), np.cos(u)
		elif function == "exp":
			return np.exp(u), np.exp(u)
		elif function == "log":
			return np.log(u), 1 / u
		return u, 1
	
	org_func = x
	h_x = 1
	for func in functions[::-1]:
		org_func, derv_func = derivate_function(func, org_func)
		h_x *= derv_func
	return h_x