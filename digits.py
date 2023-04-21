def main():
    ip= input("enter ip address:")
def validate(ip):
    # Split the address into its four components
    components = ip.split(".")
    # Check that the address has exactly four components
    if len(components) != 4:
        return False
    # Check that each component is a number between 0 and 255, inclusive
    for component in components:
        try:
            num = int(component)
            if num < 0 or num > 255:
                return False
        except ValueError:
            return False
    # If all checks passed, the address is valid
    return True
