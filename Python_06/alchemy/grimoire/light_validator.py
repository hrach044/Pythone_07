def validate_ingredients(ingredients: str) -> str:
    allowed = ["earth", "air", "fire", "water"]

    is_valid = any(item in ingredients.lower() for item in allowed)
    if is_valid:
        status = "VALID"
    else:
        status = "INVALID"
    return f"{ingredients} - {status}"
