def normalize(originalValue, minValue, maxValue):
    """
    Normalize a given value within a specified range.

    Parameters:
    - originalValue: The value that you want to normalize.
    - minValue: The minimum value in the range.
    - maxValue: The maximum value in the range.

    Returns:
    The normalized value as a percentage, where 0 corresponds to the minimum value,
    100 corresponds to the maximum value, and values in between represent the
    relative position of originalValue within the specified range.
    """
    # Calculate the difference between the original value and the minimum value,
    # representing how far the original value is from the minimum.
    difference_from_min = originalValue - minValue
    
    # Represents the total range between the maximum and minimum values.
    total_range = maxValue - minValue
    
    # Calculate the relative position of the original value within the total range.
    relative_position = difference_from_min / total_range
    
    # Scale the result to a percentage, where 0 corresponds to the minimum value,
    # 100 corresponds to the maximum value.
    normalized_value = relative_position * 100
    
    # Return the normalized value.
    return abs(normalized_value)
