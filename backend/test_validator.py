from tools.code_validator import CodeValidatorTool

# Test the custom tool
validator = CodeValidatorTool()

# Test valid code
valid_code = """
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []
"""

# Test invalid code
invalid_code = """
def two_sum(nums, target):
    for i in range(len(nums))  # Missing colon
        return i
"""

print("Testing valid code:")
print(validator._run(valid_code))

print("\nTesting invalid code:")
print(validator._run(invalid_code))