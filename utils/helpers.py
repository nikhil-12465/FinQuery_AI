def format_large_number(value):
    """
    Convert large numbers into readable format
    """

    try:

        value = float(value)

        if value >= 1_000_000_000_000:
            return f"${value/1_000_000_000_000:.2f} T"

        elif value >= 1_000_000_000:
            return f"${value/1_000_000_000:.2f} B"

        elif value >= 1_000_000:
            return f"${value/1_000_000:.2f} M"

        else:
            return f"${value:,.0f}"

    except:
        return "N/A"


def safe_float(value):

    try:
        return float(value)
    except:
        return 0