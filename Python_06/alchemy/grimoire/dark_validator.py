from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()

    is_valid = any(item in ingredients.lower() for item in allowed)
    if is_valid:
        status = "VALID"
    else:
        status = "INVALID"
    return f"{ingredients} - {status}"
