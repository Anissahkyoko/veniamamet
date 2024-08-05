import numpy as np

def make_2x3(mat: np.ndarray) -> np.ndarray:
    """
    Reshapes the input matrix to a shape of (2, 3).
    
    Parameters:
        mat (np.ndarray): Input matrix.
        
    Returns:
        np.ndarray: Reshaped matrix of shape (2, 3).
        
    Raises:
        ValueError: If the input matrix cannot be reshaped to (2, 3).
    """
    if mat.size != 6:
        raise ValueError("The input matrix must have exactly 6 elements to be reshaped to (2, 3).")
    
    return mat.reshape((2, 3))

# Example usage
if __name__ == "__main__":
    mat = np.array([1, 2, 3, 4, 5, 6])
    reshaped_mat = make_2x3(mat)
    print(reshaped_mat)
